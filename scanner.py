import socket

print("================================")
print("      Network Scanner")
print("================================")

target = input("Ingrese la IP objetivo: ")

print(f"Escaneando: {target}")

ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389]

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.settimeout(1)

        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"[OPEN] Puerto {port}")
        else:
            print(f"[CLOSED] Puerto {port}")

        sock.close()

    except socket.error:
        print(f"Error al conectar con el puerto {port}")


for port in ports:
    scan_port(target, port)