"""
Unified LLM Client for the MITRE ATLAS Knowledge Graph project.
"""

import json
import urllib.request
import urllib.error
import re


class LLMClientWrapper:
    """Unified wrapper managing requests to Ollama, OpenAI, or Groq."""

    GROQ_BASE_URL = "https://api.groq.com/openai/v1"

    def __init__(
        self,
        provider="Ollama",
        model="qwen2.5:1.5b",
        endpoint="http://localhost:11434",
        api_key=None,
    ):
        self.provider = provider
        self.model = model
        self.endpoint = endpoint.rstrip("/")
        self.api_key = api_key

    def generate_completion(self, system_prompt, user_prompt, temperature=0.0):
        """Dispatches a chat completion request to the selected provider."""
        if self.provider == "Ollama":
            return self._call_ollama(system_prompt, user_prompt, temperature)
        elif self.provider in ("OpenAI", "Groq"):
            base_url = (
                self.GROQ_BASE_URL
                if self.provider == "Groq"
                else "https://api.openai.com/v1"
            )
            return self._call_openai_compatible(
                base_url, system_prompt, user_prompt, temperature
            )
        else:
            raise ValueError(f"Unknown LLM provider: {self.provider}")

    def generate_structured_json(self, system_prompt, user_prompt):
        """Forcefully extracts JSON from LLM output, useful for AI enrichment."""
        raw = self.generate_completion(system_prompt, user_prompt)
        match = re.search(
            r"```json\s*(\{.*?\}|\[.*?\])\s*```", raw, re.DOTALL | re.IGNORECASE
        )
        if match:
            try:
                return json.loads(match.group(1).strip())
            except:
                pass

        match = re.search(r"(\{.*?\}|\[.*?\])", raw, re.DOTALL)
        if match:
            try:
                return json.loads(match.group(1).strip())
            except:
                pass

        return None

    def generate_correction(self, user_query, failed_cypher, error_msg, system_prompt):
        """Asks the model to fix a syntactically invalid Cypher query."""
        correction_prompt = (
            f"You previously translated the user's question:\n"
            f'"{user_query}"\n\n'
            f"into this Cypher query:\n"
            f"```cypher\n{failed_cypher}\n```\n\n"
            f"However, executing this query against Neo4j returned this error:\n"
            f"{error_msg}\n\n"
            f"Please inspect the error, look at the database schema and "
            f"relationship directions, and output a corrected, valid, "
            f"read-only Cypher query.\n"
            f"Return ONLY the Cypher query wrapped in a single ```cypher "
            f"and ``` block. Ensure all variables used in RETURN or WHERE "
            f"clauses are properly defined in your MATCH clause."
        )
        return self.generate_completion(system_prompt, correction_prompt)

    def _call_ollama(self, system_prompt, user_prompt, temperature):
        """Sends chat request to a local Ollama daemon."""
        url = f"{self.endpoint}/api/chat"
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "stream": False,
            "options": {"temperature": temperature},
        }
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            url, data=data, headers={"Content-Type": "application/json"}, method="POST"
        )
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                body = json.loads(resp.read().decode("utf-8"))
                return body["message"]["content"]
        except urllib.error.URLError as e:
            raise RuntimeError(f"Ollama connection failed at {self.endpoint}: {e}")
        except Exception as e:
            raise RuntimeError(f"Ollama request failed: {e}")

    def check_ollama_connection(self):
        """Returns True if the Ollama daemon is reachable."""
        try:
            with urllib.request.urlopen(f"{self.endpoint}/", timeout=3) as resp:
                return resp.status == 200
        except Exception:
            return False

    def _call_openai_compatible(
        self, base_url, system_prompt, user_prompt, temperature
    ):
        """Sends chat request to any OpenAI-compatible endpoint."""
        if not self.api_key or not self.api_key.strip():
            provider = self.provider
            raise ValueError(f"{provider} API Key is required but was not provided.")

        url = f"{base_url}/chat/completions"
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "temperature": temperature,
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers=headers,
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                body = json.loads(resp.read().decode("utf-8"))
                return body["choices"][0]["message"]["content"]
        except Exception as e:
            raise RuntimeError(f"{self.provider} request failed: {e}")

    def check_health(self):
        """Quick validation of the configured provider's reachability."""
        if self.provider == "Ollama":
            return self.check_ollama_connection()
        elif self.provider in ("OpenAI", "Groq"):
            return bool(self.api_key and len(self.api_key.strip()) > 10)
        return False
