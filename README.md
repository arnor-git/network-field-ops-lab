
# Network Field Operations Lab

A practical network engineering repository containing wireless access point (AP) deployment procedures, switch provisioning checklists, and a Python-based IP reachability checker.

The project is intended for network engineering practice, lab validation, field installation planning, and repeatable operational checks.

## Repository Contents

```text
network-field-ops-lab/
├── README.md
├── ap-provisioning-guide.md
├── switch-config-checklist.md
└── ap_reachability_checker.py
```

## Tools and Documentation

### 1. AP Provisioning Guide

`ap-provisioning-guide.md`

Covers:
- Pre-deployment surveys and cable identification
- AP mounting and Ethernet connectivity
- PoE compatibility and power budget checks
- Management IP addressing and VLAN configuration
- Controller adoption and wireless validation
- Cutover acceptance and rollback procedures

### 2. Switch Configuration Checklist

`switch-config-checklist.md`

Covers:
- Rack installation and power redundancy
- Secure management access
- Access ports, AP ports, and trunk links
- VLAN and spanning-tree verification
- Post-change testing and configuration backups

The checklist is a vendor-neutral operational guide. Exact commands must be adapted to the switch vendor, model, and operating-system version.

### 3. AP Reachability Checker

`ap_reachability_checker.py`

A Python utility that sends one ICMP echo request to each supplied IP address and reports whether the target responds.

The script supports Windows, macOS, and Linux, subject to the availability of the native `ping` utility and operating-system permissions.

## Requirements

- Python 3.9 or later
- No third-party Python packages required
- Network access to the target subnet
- Permission to perform the required network checks

ICMP traffic may be blocked by a firewall or device policy. A failed ping does not necessarily mean that a device is offline.

## Installation

Clone the repository:

```bash
git clone https://github.com/arnor-git/network-field-ops-lab.git
cd network-field-ops-lab
```

Check the Python version:

```bash
python3 --version
```

## Usage

Run the reachability checker against authorized target IP addresses:

```bash
python3 ap_reachability_checker.py 192.168.10.50 192.168.10.51 192.168.10.52
```

On Windows, use:

```powershell
py ap_reachability_checker.py 192.168.10.50 192.168.10.51
```

Example output:

```text
=== Network Device Reachability Audit ===
[REACHABLE] 192.168.10.50
[UNREACHABLE] 192.168.10.51

Summary: 1 reachable, 1 unreachable, 2 total.
```

The example output is illustrative; actual results depend on the network.

The script exits with status `0` when all targets respond, `1` when one or more targets do not respond, and `2` when an execution error prevents a valid check.

## Recommended Operational Workflow

1. Confirm the approved change window and maintenance scope.
2. Record the existing switch configuration and port assignments.
3. Verify cable labels, VLAN assignments, IP addressing, and PoE requirements.
4. Apply changes using the approved vendor-specific procedure.
5. Validate management access, client connectivity, and wireless services.
6. Record test results and configuration backups.
7. Roll back changes if acceptance criteria are not met.

## Security and Safety

- Only test systems and networks you are authorized to access.
- Do not commit credentials, private keys, customer information, or sensitive network configurations.
- Use SSH and approved authentication controls for device management.
- Restrict management access to authorized administrative networks.
- Review configuration backups before storing or sharing them.

## Limitations

- The reachability checker tests ICMP responsiveness only.
- It does not verify AP controller adoption, wireless association, VLAN correctness, DHCP, DNS, or application availability.
- The documentation does not replace vendor-specific configuration manuals or an approved production change procedure.
- Hardware, firmware, power, and feature compatibility must be verified against the actual equipment.

## Validation Status

The repository provides implementation examples and operational checklists. Production readiness must be established through testing on the intended operating systems, network devices, and deployment environment.

## License

No license is specified in this repository. Add a `LICENSE` file if you intend to grant others permission to use, modify, or redistribute the project.
