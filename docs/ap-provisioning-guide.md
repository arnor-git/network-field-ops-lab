
# Wireless Access Point (AP) Provisioning and Installation Guide

## 1. Purpose and Scope

This guide defines a repeatable process for planning, installing, provisioning, testing, and handing over enterprise wireless access points.

It is vendor-neutral. Always follow the hardware manufacturer's installation instructions and the organization's approved network design.

## 2. Pre-Deployment Checks

- [ ] Confirm the approved change request, maintenance window, and installation scope.
- [ ] Review floor plans, AP locations, expected client density, and coverage requirements.
- [ ] Confirm AP model, serial number, hardware revision, firmware compatibility, and mounting accessories.
- [ ] Verify switch port availability, uplink capacity, and PoE capability.
- [ ] Confirm the AP's power requirements against the switch's supported PoE standard and remaining power budget.
- [ ] Verify the intended management VLAN, management subnet, gateway, DNS, and DHCP configuration.
- [ ] Document corporate and guest SSIDs, their assigned VLANs, and applicable security policies.
- [ ] Label cables at both the patch-panel and AP ends.
- [ ] Record the existing switch-port configuration before making changes.

## 3. Physical Installation and Cabling

- [ ] Mount the AP using the manufacturer's approved bracket and mounting method.
- [ ] Verify that the mounting surface and fixings are suitable for the device.
- [ ] Connect the approved Ethernet cable to the correct AP uplink port.
- [ ] Check cable termination, link status, and physical damage.
- [ ] Confirm that the AP receives sufficient power.
- [ ] Check the device's status indicators or management interface for boot errors.
- [ ] Record the AP location, serial number, switch name, and connected switch port.

Do not assume that a link light alone proves correct VLAN configuration or successful provisioning.

## 4. Management IP Addressing

Use the addressing method specified by the approved network design.

### DHCP

- [ ] Verify that the AP can reach the correct DHCP service.
- [ ] Confirm the assigned IP address, subnet mask or prefix, default gateway, and DNS servers.
- [ ] Use a DHCP reservation if required by the organization's IP management policy.
- [ ] Check for duplicate addresses and incorrect DHCP scopes.

### Static Addressing

- [ ] Confirm the address and prefix against the approved IP address plan.
- [ ] Verify that the address is unused and excluded from conflicting DHCP allocations.
- [ ] Configure the correct gateway and DNS settings.
- [ ] Confirm management reachability from the authorized administration network.

Do not configure a static address or DHCP reservation without checking the authoritative IP address plan.

## 5. VLAN and Switch-Port Configuration

Confirm the intended traffic design before configuring the switch port.

- [ ] Identify the AP management VLAN.
- [ ] Identify client VLANs required by the configured SSIDs.
- [ ] Configure the switch port according to the AP vendor's tagging and management-VLAN requirements.
- [ ] Verify the native or untagged VLAN where applicable.
- [ ] Allow only the VLANs required by the approved design.
- [ ] Confirm that the upstream trunk links carry the required VLANs.
- [ ] Verify that DHCP, DNS, gateway, and controller traffic can reach their required destinations.
- [ ] Confirm that guest traffic is isolated according to the security policy.

A management VLAN and a client VLAN serve different purposes. Some APs use an untagged management VLAN, while others support a tagged management VLAN. The correct behavior depends on the device and its configuration.

Do not copy switch commands between vendors without checking their syntax and semantics.

## 6. Controller Adoption and Provisioning

- [ ] Confirm the AP can resolve and reach the controller or cloud management service.
- [ ] Verify the required DNS records, routing, firewall rules, and time synchronization.
- [ ] Confirm that the AP is authorized to join the correct management domain or organization.
- [ ] Check that the device appears in the controller inventory.
- [ ] Verify that the expected configuration profile and firmware are applied.
- [ ] Confirm that the intended SSIDs, authentication settings, and VLAN assignments are present.
- [ ] Check controller logs for adoption, authentication, or configuration errors.

Use only the controller discovery and onboarding method supported by the specific AP platform.

## 7. Wireless Validation

### Basic Service Checks

- [ ] Confirm that the expected SSIDs are being broadcast.
- [ ] Connect an authorized test client to each required SSID.
- [ ] Verify successful authentication and association.
- [ ] Confirm that the client receives an address from the correct subnet.
- [ ] Test gateway reachability, DNS resolution, and access to approved services.
- [ ] Verify that guest clients cannot reach restricted internal resources.
- [ ] Check radio state, channel assignment, transmit power, and firmware status.

### Coverage and Roaming

- [ ] Perform a walk test at the locations defined in the coverage plan.
- [ ] Record RSSI and, where available, SNR and channel utilization.
- [ ] Compare results with the organization's approved coverage thresholds.
- [ ] Test roaming between adjacent APs using representative client devices.
- [ ] Record handoff behavior, packet loss, latency, and any interruption to active sessions.
- [ ] Investigate interference, weak coverage, and excessive retransmissions.

RSSI alone does not prove successful roaming or acceptable application performance. Acceptance thresholds should be defined before the test.

## 8. Cutover Acceptance Criteria

The AP can be accepted when all applicable requirements below are satisfied:

- [ ] Physical installation and cable labeling are complete.
- [ ] Power and Ethernet link are stable.
- [ ] Management addressing and reachability are correct.
- [ ] Controller adoption and configuration synchronization succeed.
- [ ] Required SSIDs and authentication methods work.
- [ ] Client VLAN assignment and addressing are correct.
- [ ] DNS, gateway, and approved application connectivity pass.
- [ ] Guest isolation and other applicable security controls pass.
- [ ] Coverage and roaming tests meet the agreed thresholds.
- [ ] Test results, device identifiers, and configuration changes are documented.

Mark an item as passed only when the relevant test has actually been performed.

## 9. Troubleshooting

| Symptom | Checks |
|---|---|
| AP has no power | PoE standard, port power budget, cable, power injector if applicable |
| AP has no management IP | VLAN tagging, DHCP scope, DHCP relay, address plan |
| AP is unreachable | Routing, ACLs, firewall policy, ICMP policy, duplicate IP |
| AP does not join controller | DNS, discovery configuration, routing, required ports, time synchronization |
| Client gets the wrong IP | SSID-to-VLAN mapping, trunk allow-list, DHCP scope and relay |
| Client cannot access services | Gateway, DNS, firewall policy, authentication and routing |
| Roaming is poor | Coverage overlap, RF interference, client behavior, configuration and latency |

## 10. Rollback and Handover

If acceptance criteria are not met:

1. Stop further changes and document the observed failure.
2. Notify the change owner and follow the approved rollback decision.
3. Restore the previous switch-port or AP configuration from the verified backup where appropriate.
4. Restore previous VLAN and SSID mappings if required.
5. Verify that affected services have returned to the expected state.
6. Escalate unresolved issues and record the final outcome.

After successful acceptance, document the AP location, serial number, management address, switch and port, firmware, configuration profile, test results, and outstanding issues.

## 11. Change Record

- Change/ticket reference:
- Site and floor:
- AP model and serial number:
- Switch and port:
- Management IP:
- Management VLAN:
- Client VLANs:
- Controller/profile:
- Installation date and engineer:
- Test results:
- Rollback status:
- Outstanding issues:
