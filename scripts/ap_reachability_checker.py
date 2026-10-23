
#!/usr/bin/env python3
"""Check ICMP reachability of authorized network devices."""

import argparse
import ipaddress
import platform
import shutil
import subprocess
import sys
from typing import Sequence


def parse_ip(value: str) -> str:
    """Validate an IPv4 or IPv6 address."""
    try:
        return str(ipaddress.ip_address(value))
    except ValueError as exc:
        raise argparse.ArgumentTypeError(
            f"{value!r} is not a valid IPv4 or IPv6 address"
        ) from exc


def build_ping_command(ip: str, system: str) -> list[str]:
    """Build a one-packet ping command for the current operating system."""
    is_ipv6 = ipaddress.ip_address(ip).version == 6

    if system == "Windows":
        command = ["ping", "-n", "1", "-w", "2000"]
        if is_ipv6:
            command.append("-6")
        return command + [ip]

    if system == "Darwin":  # macOS: -W uses milliseconds
        command = ["ping", "-n", "-c", "1", "-W", "2000"]
        if is_ipv6:
            command.append("-6")
        return command + [ip]

    if system == "Linux":  # Linux: -W uses seconds
        command = ["ping", "-n", "-c", "1", "-W", "2"]
        if is_ipv6:
            command.append("-6")
        return command + [ip]

    raise RuntimeError(
        f"Unsupported operating system: {system}"
    )


def check_reachability(
    ip_list: Sequence[str],
    system: str | None = None,
) -> tuple[int, int]:
    """Return (reachable_count, unreachable_count)."""
    system = system or platform.system()
    ping_path = shutil.which("ping")

    if ping_path is None:
        raise RuntimeError(
            "The 'ping' utility was not found. "
            "Install or enable the operating-system ping utility."
        )

    print("=== Network Device Reachability Audit ===")

    reachable = 0
    unreachable = 0

    for ip in ip_list:
        command = build_ping_command(ip, system)
        command[0] = ping_path

        try:
            result = subprocess.run(
                command,
                stdin=subprocess.DEVNULL,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                timeout=5,
                check=False,
            )

            if result.returncode == 0:
                print(f"[REACHABLE] {ip}")
                reachable += 1
            else:
                print(f"[UNREACHABLE] {ip}")
                unreachable += 1

        except subprocess.TimeoutExpired:
            print(f"[TIMEOUT] {ip}")
            unreachable += 1

    total = reachable + unreachable
    print(
        f"\nSummary: {reachable} reachable, "
        f"{unreachable} unreachable, {total} total."
    )

    return reachable, unreachable


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Check ICMP reachability of authorized "
            "IPv4 or IPv6 network devices."
        )
    )
    parser.add_argument(
        "ips",
        nargs="+",
        type=parse_ip,
        metavar="IP",
        help="One or more target IP addresses",
    )

    args = parser.parse_args()

    try:
        _, unreachable = check_reachability(args.ips)
        return 1 if unreachable else 0
    except (RuntimeError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
