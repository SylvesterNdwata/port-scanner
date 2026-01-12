import argparse
from scanner import Scanner

scan = Scanner()

def create_parser():
    parser = argparse.ArgumentParser(prog="PortScanner", description="A simple port scanner tool")
    parser.add_argument('ip', type=str, help='Target IP address to scan')
    parser.add_argument("-s", "--start_port", type=int, default=1, help="Starting port number (default: 1)")
    parser.add_argument("-e", "--end_port", type=int, default=1024, help="Ending port number (default: 1024)")
    args = parser.parse_args()

    scan.scanner(ip=args.ip, start_port=args.start_port, end_port=args.end_port)


if __name__ == "__main__":
    create_parser()