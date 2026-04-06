
import argparse
from cve_api import fetch_cves, fetch_cve_by_id
from formatter import format_cve
from report import generate_pdf, save_json

def print_banner():
    print("="*40)
    print("        VulScope CLI Tool")
    print("="*40)

def main():
    print_banner()

    parser = argparse.ArgumentParser(description="VulScope - CVE Lookup Tool")
    parser.add_argument("--keyword", help="Search CVEs by keyword")
    parser.add_argument("--cve-id", help="Search by CVE ID")
    parser.add_argument("--severity", help="Filter by severity (LOW, MEDIUM, HIGH, CRITICAL)")
    parser.add_argument("--pdf", action="store_true", help="Generate PDF report")
    parser.add_argument("--json", action="store_true", help="Save JSON output")

    args = parser.parse_args()

    if not args.keyword and not args.cve_id:
        print("[ERROR] Provide --keyword or --cve-id")
        return

    if args.cve_id:
        raw = fetch_cve_by_id(args.cve_id)
    else:
        raw = fetch_cves(args.keyword)

    if not raw:
        print("[INFO] No CVEs found.")
        return

    formatted = [format_cve(c) for c in raw]

    if args.severity:
        formatted = [c for c in formatted if c["severity"] == args.severity.upper()]

    for cve in formatted:
        print("\n---------------------")
        print(f"ID: {cve['id']}")
        print(f"Severity: {cve['severity']}")
        print(f"Description: {cve['description']}")

    if args.pdf:
        generate_pdf(formatted)

    if args.json:
        save_json(formatted)

if __name__ == "__main__":
    main()
