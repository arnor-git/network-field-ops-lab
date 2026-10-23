> **File path to type in GitHub:** `docs/ap-provisioning-guide.md`

```markdown
# Wireless Access Point (AP) Provisioning & Installation Guide

## 1. Pre-Deployment Audit
- Verify floor plans, AP mounting locations, and coverage requirements.
- Label all drop cables at both the patch panel and AP end.
- Verify switch port PoE standard compatibility (802.3af / 802.3at / 802.3bt).

## 2. Physical Installation & Cabling
- Mount the AP bracket securely on ceiling T-grid rails or structural walls.
- Connect Cat6 ethernet patch cable from local jack to AP primary uplink port.
- Confirm LED status indicators for power, link, and radio state.

## 3. Configuration & Provisioning
- **IP Addressing:** Verify DHCP reservation or assign static management IP.
- **VLAN & SSID Mapping:**
  - Corporate Wireless -> Corporate VLAN
  - Guest Wireless -> Isolated Guest VLAN
- **Controller Adoption:** Verify registration with controller / cloud management platform.
- **Signal & Cutover Test:** Perform RSSI walk-test and verify seamless roaming between adjacent APs.
