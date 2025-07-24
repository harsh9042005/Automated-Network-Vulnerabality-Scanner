def generate_report(ip, results, file="report.txt"):
    with open(file, "w") as f:
        f.write(f"Scan Report for: {ip}\n\n")
        for r in results:
            f.write(f"Port {r['port']} - {r['product']} {r['version']}\n")
            for cve in r.get('cves', []):
                f.write(f"  CVE: {cve['id']} | Severity: {cve['severity']}\n  Desc: {cve['description'][:100]}...\n")
        f.write("\n--- End of Report ---\n")

    print(f"\n✅ Report saved as '{file}' in your project folder.")