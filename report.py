
import json
from reportlab.platypus import SimpleDocTemplate, Paragraph

def generate_pdf(cves, filename="report.pdf"):
    doc = SimpleDocTemplate(filename)
    content = []

    for cve in cves:
        text = f"{cve['id']} - {cve['severity']}<br/>{cve['description']}<br/><br/>"
        content.append(Paragraph(text))

    doc.build(content)
    print("[INFO] PDF saved:", filename)

def save_json(cves, filename="output.json"):
    with open(filename, "w") as f:
        json.dump(cves, f, indent=4)
    print("[INFO] JSON saved:", filename)
