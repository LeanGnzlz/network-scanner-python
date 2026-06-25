import sys
import socket
import datetime
import time
import json
from concurrent.futures import ThreadPoolExecutor

print("================================")
print("      Network Scanner")
print("================================")

if len(sys.argv) < 2:
    print("Uso: python scanner.py <IP>")
    sys.exit()

target = sys.argv[1]

full_scan = False

if len(sys.argv) > 2 and sys.argv[2] == "--full":
    full_scan = True

print(f"Escaneando: {target}")

start_time = time.time()

if full_scan:
    ports = range(1, 1025)
else:
    ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389]

services = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    135: "MSRPC",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3389: "RDP"
    }

open_ports = []
scan_results = []

banner_ports = [
    21,
    22,
    23,
    25,
    80,
    110,
    143,
    443
]

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.settimeout(1)

        result = sock.connect_ex((target, port))

        if result == 0:
          return port
          
        else:
          return None

    except socket.error:
        print(f"Error al conectar con el puerto {port}")

def grab_banner(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.settimeout(2)

        sock.connect((target, port))

        banner = sock.recv(1024).decode(errors="ignore")

        sock.close()

        return banner.strip()

    except:
        return "No banner detected"

def save_report(target, scan_results, scan_duration, scan_id):
    now = datetime.datetime.now()

    filename = f"reports/scan_{scan_id}.txt"

    with open(filename, "w") as file:
        file.write("================================\n")
        file.write("        NETWORK SCANNER REPORT\n")
        file.write("================================\n\n")

        file.write(f"Target: {target}\n\n")

        file.write("Open ports:\n")

        if scan_results:
            for result in scan_results:
                file.write(f"- Port {result['port']} - {result['service']}\n")
                file.write(f"  Banner: {result['banner']}\n\n")
        else:
            file.write("No open ports found\n")

        file.write(f"\nScan duration: {scan_duration:.2f} seconds\n")
        file.write(f"Scan completed: {now.strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write("\n================================\n")

    print(f"\nReporte guardado: {filename}")

def save_json(target, scan_results, scan_duration, scan_id):
    now = datetime.datetime.now()

    filename = f"reports/scan_{scan_id}.json"

    report = {
        "target": target,
        "scan_duration": round(scan_duration, 2),
        "completed": now.strftime("%Y-%m-%d %H:%M:%S"),
        "open_ports": scan_results
    }

    with open(filename, "w") as file:
        json.dump(report, file, indent=4)

    print(f"Reporte JSON guardado: {filename}")

with ThreadPoolExecutor(max_workers=50) as executor:
    results = executor.map(lambda port: scan_port(target, port), ports)

    for result in results:
        if result:
            open_ports.append(result)

for port in sorted(open_ports):
    
    if port in banner_ports:
     banner = grab_banner(target, port)
    else:
     banner = "Not applicable"

    print(f"[OPEN] Puerto {port} - {services.get(port, 'Unknown')}")
    print(f"       Banner: {banner}")
    
    scan_results.append({
        "port": port,
        "service": services.get(port, "Unknown"),
        "banner": banner
    })

end_time = time.time()

scan_duration = end_time - start_time

scan_id = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

print("================================")
print("Escaneo finalizado")
print(f"Puertos abiertos encontrados: {len(open_ports)}")
print(f"Tiempo de escaneo: {scan_duration:.2f} segundos")
print("================================")

save_report(target, scan_results, scan_duration, scan_id)
save_json(target, scan_results, scan_duration, scan_id)