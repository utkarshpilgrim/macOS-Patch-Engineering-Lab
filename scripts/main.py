from apple_scraper import extract_cves_from_apple
from nvd_mapper import map_cve_to_nvd
import json

def generate_catalogue(apple_url):
    catalogue = {}
    cves = extract_cves_from_apple(apple_url)
    for cve_id, apple_data in cves.items():
        nvd_data = map_cve_to_nvd(cve_id)
        priority = 'Critical' if float(nvd_data.get('cvss_score', 0)) >= 9.0 else 'High' if >= 7.0 else 'Medium'
        catalogue[cve_id] = {**apple_data, **nvd_data, 'priority': priority}
    with open('../data/sample_catalogue.json', 'w') as f:
        json.dump(catalogue, f, indent=4)
    print("Catalogue generated: data/sample_catalogue.json")

if __name__ == "__main__":
    # Example: Recent macOS Tahoe 26.3
    generate_catalogue("https://support.apple.com/en-us/126348")
