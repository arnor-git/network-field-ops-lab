import subprocess
import sys

# Utility script to test IP reachability of newly provisioned APs / switches
target_ips = [
    "192.168.10.50",
    "192.168.10.51",
    "192.168.10.52",
]

def check_reachability(ip_list):
    print("=== Network Device Reachability Audit ===")
    for ip in ip_list:
        # Standard ping command (1 packet, 2 sec timeout)
        res = subprocess.run(["ping", "-c", "1", "-W", "2", ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        status = "ONLINE [REACHABLE]" if res.returncode == 0 else "OFFLINE [UNREACHABLE]"
        print(f"[{status}] {ip}")

if __name__ == "__main__":
    check_reachability(target_ips)
