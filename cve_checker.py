import requests
def search_cves(product, version):
    query = f"{product} {version}"
    url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch={query}&resultsPerPage=3"

    try:
        response = requests.get(url)
        data = response.json()
        cves = []

        for item in data.get('vulnerabilities', []):
            cves.append({
                'id': item['cve']['id'],
                'description': item['cve']['descriptions'][0]['value'],
                'severity': item['cve'].get('metrics', {}).get('cvssMetricV2', [{}])[0].get('baseSeverity', 'N/A')
            })

        return cves
    except Exception as e:
        print("Error fetching CVEs:", e)
        return []