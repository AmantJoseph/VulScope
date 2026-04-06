
def format_cve(item):
    cve = item.get("cve", {})
    cve_id = cve.get("id", "N/A")

    desc = cve.get("descriptions", [])
    description = desc[0]["value"] if desc else "No description"

    metrics = cve.get("metrics", {})
    severity = "N/A"

    if "cvssMetricV31" in metrics:
        severity = metrics["cvssMetricV31"][0]["cvssData"]["baseSeverity"]

    return {"id": cve_id, "description": description, "severity": severity}
