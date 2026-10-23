# Switch Rack Mounting & Configuration Checklist

## 1. Physical Hardware Installation
- [ ] Mount switch securely into 19" rack frame using appropriate cage nuts/screws.
- [ ] Connect redundant power supplies (PDU A / PDU B).
- [ ] Dress and organize patch cables using horizontal/vertical cable managers.

## 2. Base Configuration & Management
- [ ] Set hostname and domain parameters.
- [ ] Configure Management Interface / Management VLAN.
- [ ] Enable SSH (v2) and disable telnet/unsecure protocols.
- [ ] Set up console authentication and admin passwords.

## 3. Port & VLAN Provisioning
- [ ] **Access Ports:** Set switchport mode access and assign to designated VLAN.
- [ ] **AP Ports:** Enable PoE/PoE+ and configure native/tagged VLANs as needed.
- [ ] **Trunk Ports:** Set switchport mode trunk, enable 802.1Q encapsulation, and restrict allowed VLANs.

## 4. Post-Cutover Verification
- [ ] Verify uplink status and trunk negotiate correctly.
- [ ] Test connectivity (gateway ping, DNS lookup, remote SSH session via PuTTY).
- [ ] Back up running configuration to remote location.
