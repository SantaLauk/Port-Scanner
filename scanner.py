
import socket
import sys
import threading
from queue import Queue
import argparse

parser = argparse.ArgumentParser(description="Simple Python Port Scanner")
parser.add_argument("target", help="Target IP or domain")
parser.add_argument("--quick", action="store_true", help="Scan common ports (20-100)")
parser.add_argument("--full", action="store_true", help="Scan full port range (1-1024)")
parser.add_argument("--start", type=int, help="Custom start port")
parser.add_argument("--end", type=int, help="Custom end port")

args = parser.parse_args() 
target = socket.gethostbyname(args.target)

if args.quick:
    start_port = 20
    end_port = 100

elif args.full:
    start_port = 1
    end_port = 1024

elif args.start and args.end:
    start_port = args.start
    end_port = args.end

else:
    start_port = 20
    end_port = 100

services = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL"
}

print(f"Scanning target: {target}")
print(f"Scanning ports {start_port}-{end_port}\n")

port_queue = Queue()

for port in range(start_port, end_port +1):
    port_queue.put(port)

scan_results = []
total_ports = end_port - start_port + 1
scanned_count = 0
lock = threading.Lock()

def scan_port():

    global scanned_count

    while not port_queue.empty():

        port = port_queue.get()

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))

        if result == 0:
            service = services.get(port, "Unknown")
            server = "Unknown"

            try:
                sock.send(b"GET / HTTP/1.0\r\n\r\n")
                banner = sock.recv(1024).decode(errors="ignore")

                for line in banner.split("\n"):
                    if "Server:" in line:
                        server = line.strip()
            except:
                server = "No banner"

            result_line = f"Port {port:<4} is OPEN     {service}   {server}"
            print(result_line)
            scan_results.append(result_line)

        sock.close()

        port_queue.task_done()

        with lock:
            scanned_count += 1
            if scanned_count % 10 == 0 or scanned_count == total_ports:
                print(f"Scanned {scanned_count}/{total_ports} ports...")

for _ in range(50):
    thread = threading.Thread(target=scan_port)
    thread.start()

port_queue.join()