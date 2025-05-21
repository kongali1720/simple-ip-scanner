import socket
from concurrent.futures import ThreadPoolExecutor
import sys

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        sock.close()
        return port if result == 0 else None
    except:
        return None

def scan_ip(ip, start_port, end_port, max_threads=50):
    open_ports = []
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = [executor.submit(scan_port, ip, port) for port in range(start_port, end_port + 1)]
        for future in futures:
            port = future.result()
            if port:
                open_ports.append(port)
    return open_ports

def main():
    if len(sys.argv) < 4:
        print(f"Usage: python {sys.argv[0]} <ip> <start_port> <end_port> [max_threads]")
        sys.exit(1)

    ip = sys.argv[1]
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])
    max_threads = int(sys.argv[4]) if len(sys.argv) > 4 else 50

    print(f"Scanning {ip} from port {start_port} to {end_port} with {max_threads} threads...")

    open_ports = scan_ip(ip, start_port, end_port, max_threads)

    if open_ports:
        print(f"Open ports on {ip}: {', '.join(map(str, open_ports))}")
    else:
        print(f"No open ports found on {ip}.")

if __name__ == "__main__":
    main()
