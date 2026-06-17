import sys
import socket

print("================================")
print("      Network Scanner")
print("================================")

if len(sys.argv) < 2:
    print("Uso: python scanner.py <IP>")
    sys.exit()

target = sys.argv[1]

print(f"Escaneando: {target}")

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
            print(f"[OPEN] Puerto {port} - {services.get(port, 'Unknown')}")
            sock.close()
            return port
        else:
            print(f"[CLOSED] Puerto {port}")
            sock.close()
            return None

    except socket.error:
        print(f"Error al conectar con el puerto {port}")


for port in ports:
    result = scan_port(target, port)

    if result:
        open_ports.append(result)

print("================================")
print("Escaneo finalizado")
print(f"Puertos abiertos encontrados: {len(open_ports)}")
print("================================")        