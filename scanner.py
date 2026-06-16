import socket

print("================================")
print("      Network Scanner")
print("================================")

target = input("Ingrese la IP objetivo: ")

print(f"Escaneando: {target}")

def scan_port(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"Puerto {port} abierto")
    else:
        print(f"Puerto {port} cerrado")

    sock.close()


scan_port(target, 80)