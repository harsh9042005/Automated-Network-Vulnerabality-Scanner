import nmap

def scan_target(ip):
    scanner = nmap.PortScanner()
    scanner.scan(ip, arguments='-sV')

    results = []

    for host in scanner.all_hosts():
        for proto in scanner[host].all_protocols():
            ports = scanner[host][proto].keys()
            for port in ports:
                info = scanner[host][proto][port]
                results.append({
                    'port': port,
                    'state': info['state'],
                    'name': info.get('name', ''),
                    'product': info.get('product', ''),
                    'version': info.get('version', '')
                })

    return results