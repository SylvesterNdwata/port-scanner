import socket

def scanner(ip, start_port, end_port):
    print(f"Scanning {ip} from {start_port} to {end_port}")

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"[+] port {port} is open")
        sock.close()
    

if __name__ == "__main__":
    target = "127.0.0.1"
    scanner(target, 1, 1024)


