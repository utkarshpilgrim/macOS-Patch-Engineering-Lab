import requests

def map_cve_to_nvd(cve_id):
    """Query NVD API for CVE details."""
    api_url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?cveId={cve_id}"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()['vulnerabilities'][0]['cve']
        cvss = data.get('metrics', {}).get('cvssMetricV31', [{}])[0]
        return {
            'description': data['descriptions'][0]['value'],
            'cvss_score': cvss.get('cvssData', {}).get('baseScore', 'N/A'),
            'severity': cvss.get('cvssData', {}).get('baseSeverity', 'N/A'),
            'vector': cvss.get('cvssData', {}).get('vectorString', 'N/A'),
            'cwe': data.get('weaknesses', [{}])[0].get('description', [{}])[0].get('value', 'N/A'),
            'exploits': data.get('references', [])  # List of links to exploits/advisories
        }
    return {'error': 'NVD data not found'}
