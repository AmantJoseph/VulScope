
import requests

BASE_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"

def fetch_cves(keyword):
    try:
        res = requests.get(BASE_URL, params={"keywordSearch": keyword, "resultsPerPage": 5}, timeout=10)
        res.raise_for_status()
        return res.json().get("vulnerabilities", [])
    except requests.exceptions.ConnectionError:
        print("[ERROR] No internet connection.")
    except requests.exceptions.Timeout:
        print("[ERROR] Request timed out.")
    except Exception as e:
        print("[ERROR]", e)
    return []

def fetch_cve_by_id(cve_id):
    try:
        res = requests.get(BASE_URL, params={"cveId": cve_id}, timeout=10)
        res.raise_for_status()
        return res.json().get("vulnerabilities", [])
    except Exception as e:
        print("[ERROR]", e)
    return []
