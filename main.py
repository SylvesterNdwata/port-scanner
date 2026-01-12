import socket
import argparse

def scanner(ip, start_port, end_port):
    print(f"Scanning {ip} from {start_port} to {end_port}")

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"[+] port {port} is open")
        sock.close()
    
def create_parser():
    parser = argparse.ArgumentParser(prog="PortScanner", description="A simple port scanner tool")
    parser.add_argument('ip', type=str, help='Target IP address to scan')
    parser.add_argument("-s", "--start_port", type=int, default=1, help="Starting port number (default: 1)")
    parser.add_argument("-e", "--end_port", type=int, default=1024, help="Ending port number (default: 1024)")
    args = parser.parse_args()

    scanner(ip=args.ip, start_port=args.start_port, end_port=args.end_port)

if __name__ == "__main__":
    create_parser()

