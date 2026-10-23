
# Switch Installation and Configuration Checklist

## 1. Scope and Change Control

- [ ] Confirm the approved change request and maintenance window.
- [ ] Verify switch model, hardware revision, firmware, and intended role.
- [ ] Record hostname, management IP, location, rack, and uplink connections.
- [ ] Obtain the approved VLAN, IP addressing, port assignment, and uplink plan.
- [ ] Capture the current running configuration and relevant operational state.
- [ ] Confirm console or out-of-band access is available before making changes.
- [ ] Define acceptance criteria and rollback steps.

## 2. Physical Installation

- [ ] Mount the switch securely using the manufacturer's instructions.
- [ ] Verify rack loading, airflow clearance, and environmental requirements.
- [ ] Connect power supplies to the planned power sources.
- [ ] Verify redundant power feeds where supported and required.
- [ ] Check fan, temperature, and power-supply status.
- [ ] Label uplinks, downlinks, patch-panel connections, and power cables.
- [ ] Confirm cable type, transceiver compatibility, and link speed requirements.

Do not assume that two power supplies provide redundancy if both depend on the same power source.

## 3. Base Configuration and Secure Management

- [ ] Configure the hostname and approved management parameters.
- [ ] Configure the management interface or management VLAN.
- [ ] Verify the management IP address, subnet or prefix, gateway, and routing.
- [ ] Enable SSH using the platform's supported secure configuration.
- [ ] Disable Telnet and other unnecessary insecure management services.
- [ ] Configure individual administrator accounts and least-privilege access.
- [ ] Integrate centralized AAA where supported and required.
- [ ] Protect console access and store credentials using the approved secrets process.
- [ ] Restrict management access to authorized networks and administrator sources.
- [ ] Configure logging, time synchronization, and monitoring as required.
- [ ] Verify firmware and security advisories against the approved baseline.

Avoid placing passwords, private keys, or authentication secrets in this checklist or in version control.

## 4. VLAN and Port Provisioning

### Access Ports

- [ ] Set the port to access mode using the platform's supported syntax.
- [ ] Assign the approved access VLAN.
- [ ] Verify the VLAN exists and is active.
- [ ] Apply required port-security and spanning-tree edge protections.
- [ ] Confirm unused ports are handled according to security policy.

### Wireless Access Point Ports

- [ ] Confirm the AP's required PoE standard and power budget.
- [ ] Identify the AP management VLAN and client VLANs.
- [ ] Configure access or trunk mode according to the approved AP design.
- [ ] Verify native or untagged VLAN behavior where applicable.
- [ ] Allow only required tagged VLANs.
- [ ] Confirm upstream links carry the required VLANs.
- [ ] Verify that the AP can obtain management addressing and reach its controller.
- [ ] Test client VLAN assignment through the AP.

An AP port is not automatically a trunk in every design. The correct mode depends on the AP model, management VLAN configuration, and SSID requirements.

### Trunk Ports

- [ ] Configure trunk mode using vendor-supported commands.
- [ ] Verify the tagging protocol and encapsulation supported by the platform.
- [ ] Configure the approved native or untagged VLAN where applicable.
- [ ] Restrict the allowed VLAN list to the required VLANs.
- [ ] Verify the peer configuration and ensure both ends agree on VLAN behavior.
- [ ] Confirm link speed, duplex, and aggregation settings where relevant.
- [ ] Check for unexpected VLANs, native-VLAN mismatches, and blocked links.

Do not assume trunk negotiation is supported or required. Follow the platform's design and configuration standards.

## 5. Layer 2 and Layer 3 Verification

- [ ] Verify physical and logical link state on relevant interfaces.
- [ ] Confirm expected VLAN membership and operational status.
- [ ] Check spanning-tree state, root placement, and unexpected topology changes.
- [ ] Verify link aggregation membership and consistency where configured.
- [ ] Check MAC address learning on expected ports.
- [ ] Verify gateway reachability from the correct source or VLAN.
- [ ] Verify routing and return paths where Layer 3 functionality is present.
- [ ] Confirm DHCP relay and DNS reachability where applicable.
- [ ] Check interface errors, discards, speed mismatches, and abnormal utilization.

Use vendor-specific operational commands to validate the actual state; a successful configuration command alone is insufficient.

## 6. Post-Cutover Tests

- [ ] Confirm uplinks and required downstream links are operational.
- [ ] Verify management access using an authorized SSH client.
- [ ] Test reachability to the intended gateway and approved services.
- [ ] Verify that clients receive addresses from the correct DHCP scopes.
- [ ] Test DNS resolution and application connectivity.
- [ ] Confirm that intended VLAN segmentation and security policies are enforced.
- [ ] Verify AP adoption and wireless client connectivity where applicable.
- [ ] Check logs, monitoring alerts, interface counters, and spanning-tree events.
- [ ] Compare actual results against the approved acceptance criteria.

A successful ping does not verify SSH access, VLAN correctness, application availability, or overall device health.

## 7. Configuration Backup and Rollback

- [ ] Save the approved configuration using the platform's supported method.
- [ ] Export a post-change configuration backup to an authorized secure location.
- [ ] Confirm that the backup file is readable and associated with the correct device.
- [ ] Protect backups because they may contain sensitive topology or configuration data.
- [ ] Verify the documented restoration procedure and access requirements.
- [ ] Keep the previous configuration available until the change is accepted.
- [ ] Execute rollback if required by the approved change procedure.
- [ ] Re-test critical connectivity and confirm service restoration after rollback.

A backup is not proven recoverable merely because a file was created. Validate the restoration process in an appropriate lab or approved recovery procedure.

## 8. Final Sign-Off

- [ ] Physical installation completed.
- [ ] Management access verified.
- [ ] VLAN and trunk behavior verified.
- [ ] Required connectivity and security tests passed.
- [ ] Monitoring and logging checked.
- [ ] Configuration backup completed.
- [ ] Documentation and port mapping updated.
- [ ] Outstanding issues recorded and assigned.
- [ ] Change owner informed of the outcome.

## Change Record

- Site / rack:
- Switch hostname and model:
- Software version:
- Change reference:
- Engineer:
- Date and maintenance window:
- Ports and VLANs changed:
- Pre-change backup location:
- Post-change backup location:
- Verification results:
- Rollback performed: Yes / No
- Outstanding issues:
- Final status: Passed / Failed / Partially completed
