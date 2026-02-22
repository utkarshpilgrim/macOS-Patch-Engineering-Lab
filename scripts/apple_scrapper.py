import requests
from bs4 import BeautifulSoup

def extract_cves_from_apple(url):
    """Scrape Apple's security advisory for CVEs and details."""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    cves = {}
    # Find sections with CVE mentions (adapt based on page structure)
    for section in soup.find_all('h3'):  # Components like 'Admin Framework'
        component = section.text.strip()
        details = section.find_next('p').text.strip() if section.find_next('p') else ''
        cve_match = details.split('CVE-')[1].split(':')[0] if 'CVE-' in details else None
        if cve_match:
            cves[cve_match] = {
                'component': component,
                'impact': details.split('Impact: ')[1].split('.')[0] if 'Impact:' in details else 'Unknown',
                'description': details.split('Description: ')[1] if 'Description:' in details else 'Unknown'
            }
    return cves
