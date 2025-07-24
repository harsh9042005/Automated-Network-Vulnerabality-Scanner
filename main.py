from scanner import scan_target
from cve_checker import search_cves
from reporter import generate_report

def main():
    ip = input("Enter IP to scan: ")
    print(f"\n[*] Scanning {ip}...")
    results = scan_target(ip)

    for r in results:
        if r['product']:
            print(f"[+] Searching CVEs for {r['product']} {r['version']}")
            r['cves'] = search_cves(r['product'], r['version'])

    generate_report(ip, results)

if __name__ == "__main__":
    main()
