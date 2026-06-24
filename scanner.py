import sys
import socket
import datetime
import time
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
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3389: "RDP"
}

open_ports = []

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
    
def save_report(target, open_ports, scan_duration, services):
    now = datetime.datetime.now()

    filename = f"reports/scan_{now.strftime('%Y%m%d_%H%M%S')}.txt"

    with open(filename, "w") as file:
        file.write("================================\n")
        file.write("        NETWORK SCANNER REPORT\n")
        file.write("================================\n\n")

        file.write(f"Target: {target}\n\n")

        file.write("Open ports:\n")

        if open_ports:
            for port in open_ports:
                file.write(f"- Port {port} - {services.get(port, 'Unknown')}\n")
        else:
            file.write("No open ports found\n")

        file.write(f"\nScan duration: {scan_duration:.2f} seconds\n")
        file.write(f"Scan completed: {now.strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write("\n================================\n")

    print(f"\nReporte guardado: {filename}")

with ThreadPoolExecutor(max_workers=50) as executor:
    results = executor.map(lambda port: scan_port(target, port), ports)

    for result in results:
        if result:
            open_ports.append(result)

for port in sorted(open_ports):
    print(f"[OPEN] Puerto {port} - {services.get(port, 'Unknown')}")

open_ports.sort()

end_time = time.time()

scan_duration = end_time - start_time

print("================================")
print("Escaneo finalizado")
print(f"Puertos abiertos encontrados: {len(open_ports)}")
print(f"Tiempo de escaneo: {scan_duration:.2f} segundos")
print("================================")

save_report(target, open_ports, scan_duration, services)