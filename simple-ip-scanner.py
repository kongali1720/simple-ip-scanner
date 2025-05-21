#!/usr/bin/env python3
"""
Simple IP Scanner
Scan IP range dan cek IP aktif dengan ping.
"""

import subprocess
import platform
import threading

def ping_ip(ip):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', ip]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        print(f"{ip} is active")

def scan_range(start_ip, end_ip):
    start = int(start_ip.split('.')[-1])
    base = '.'.join(start_ip.split('.')[:-1]) + '.'
    threads = []
    for i in range(start, end_ip + 1):
        ip = base + str(i)
        t = threading.Thread(target=ping_ip, args=(ip,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    print("Simple IP Scanner by Kongali1720")
    start_ip = input("Start IP (e.g. 192.168.1.1): ")
    end_last = int(input("End IP last number (e.g. 254): "))
    scan_range(start_ip, end_last)
