import requests
import os
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)

ATLAS_DATA_URL = "https://raw.githubusercontent.com/mitre-atlas/atlas-data/main/dist/v6/ATLAS-latest.yaml"
OUTPUT_FILE = "ATLAS-latest.yaml"


def update_atlas_data():
    """Downloads the latest ATLAS YAML, following pointers if necessary."""
    url = ATLAS_DATA_URL
    logging.info(f"Fetching latest ATLAS data from {url}...")

    try:
        while True:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            content = response.text.strip()

            if len(content) < 100 and content.endswith(".yaml") and " " not in content:
                logging.info(f"Following pointer: {content}")
                if "/" in content:
                    url = f"https://raw.githubusercontent.com/mitre-atlas/atlas-data/main/dist/{content}"
                else:
                    base = url.rsplit("/", 1)[0]
                    url = f"{base}/{content}"
            else:
                with open(OUTPUT_FILE, "wb") as f:
                    f.write(response.content)
                logging.info(
                    f"Successfully updated {OUTPUT_FILE} ({len(response.content)} bytes)."
                )
                break
    except Exception as e:
        logging.error(f"Failed to update ATLAS data: {e}")


if __name__ == "__main__":
    update_atlas_data()
