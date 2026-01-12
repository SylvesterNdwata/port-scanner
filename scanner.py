import socket


class Scanner:
    def __init__(self):
        self.common_ports = {
            21: "FTP",
            22: "SSH", 
            23: "Telnet",
            25: "SMTP",
            53: "DNS",
            80: "HTTP",
            110: "POP3",
            135: "RPC",
            139: "NetBIOS",
            143: "IMAP",
            443: "HTTPS",
            445: "SMB",
            3306: "MySQL",
            3389: "RDP",
            5900: "VNC",
            8080: "HTTP-Proxy"
        }

    def scanner(self, ip, start_port, end_port):
        print(f"Scanning {ip} from {start_port} to {end_port}")

        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)

            result = sock.connect_ex((ip, port))
            if result == 0:
                if port in self.common_ports:
                    print(f"[+] port {port} is open {self.common_ports[port]}")
                else:
                    print(f"[+] port {port} is open")
            sock.close()
    

