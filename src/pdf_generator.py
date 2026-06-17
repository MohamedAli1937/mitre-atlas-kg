"""
Styled PDF Report Generator for AI Threat Assessments.
"""

from fpdf import FPDF
import datetime
import os


class ThreatPDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 15)
        self.cell(0, 10, "AI Security Threat Assessment Report", 0, 1, "C")
        self.set_font("Arial", "I", 8)
        self.cell(
            0,
            10,
            f'Generated on: {datetime.date.today().strftime("%B %d, %Y")}',
            0,
            1,
            "R",
        )
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")


def clean_text(text):
    if not text:
        return ""
    text = text.replace("•", "-").replace("\u2013", "-").replace("\u2014", "-")
    return text.encode("latin-1", "replace").decode("latin-1")


def generate_pdf_report(description, components, threats, owasp_mappings, output_path):
    pdf = ThreatPDF()
    pdf.add_page()
    eff_w = pdf.w - 2 * pdf.l_margin

    pdf.set_font("Arial", "B", 12)
    pdf.set_fill_color(240, 240, 240)
    pdf.cell(eff_w, 10, "1. System Overview", 1, 1, "L", fill=True)
    pdf.set_font("Arial", "", 10)
    pdf.multi_cell(eff_w, 8, clean_text(f"Description: {description}"))
    pdf.ln(2)
    pdf.set_font("Arial", "B", 10)
    pdf.cell(
        eff_w, 8, clean_text(f"Identified Components: {', '.join(components)}"), 0, 1
    )
    pdf.ln(10)

    unique_techs = {t["tech_id"] for t in threats}
    pdf.set_font("Arial", "B", 12)
    pdf.cell(eff_w, 10, "2. Executive Summary", 1, 1, "L", fill=True)
    pdf.set_font("Arial", "", 10)
    pdf.multi_cell(
        eff_w,
        8,
        clean_text(
            f"The analysis identified {len(unique_techs)} distinct threats from the MITRE ATLAS framework."
        ),
    )
    pdf.ln(10)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(eff_w, 10, "3. Detailed Threat Analysis", 1, 1, "L", fill=True)
    pdf.ln(5)

    for t in threats:
        pdf.set_font("Arial", "B", 11)
        pdf.set_text_color(200, 0, 0)
        pdf.cell(eff_w, 8, clean_text(f"{t['tech_id']}: {t['tech_name']}"), 0, 1)
        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Arial", "I", 9)
        pdf.cell(eff_w, 6, clean_text(f"Target Component: {t['component']}"), 0, 1)
        ow_list = owasp_mappings.get(t["tech_id"], [])
        if ow_list:
            pdf.cell(eff_w, 6, clean_text(f"OWASP Mapping: {', '.join(ow_list)}"), 0, 1)
        pdf.set_font("Arial", "", 9)
        if t["description"]:
            pdf.multi_cell(
                eff_w, 5, clean_text(f"Description: {t['description'][:500]}...")
            )
        pdf.ln(2)
        valid_mits = [m for m in t["mitigations"] if m.get("id")]
        if valid_mits:
            pdf.set_font("Arial", "B", 9)
            pdf.cell(eff_w, 6, "Recommended Mitigations:", 0, 1)
            pdf.set_font("Arial", "", 9)
            for m in valid_mits:
                m_suffix = m["id"].split(".")[-1] if "." in m["id"] else m["id"]
                m_url = f"https://atlas.mitre.org/mitigations/{m_suffix}"
                pdf.set_text_color(0, 0, 255)
                pdf.write(5, f" - {m['name']}", m_url)
                pdf.set_text_color(0, 0, 0)
                pdf.write(
                    5,
                    clean_text(
                        f" (Owner: {m.get('role', 'Unknown')}) in {m.get('phase', 'General')} phase\n"
                    ),
                )
        pdf.ln(5)
        if pdf.get_y() > 250:
            pdf.add_page()

    pdf.output(output_path)
