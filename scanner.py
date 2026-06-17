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
open_ports = []

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.settimeout(1)

        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"[OPEN] Puerto {port}")
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