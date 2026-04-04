---
name: nordvpn
description: NordVPN CLI for secure network connections. Use when the user asks to connect/disconnect VPN, check VPN status, configure VPN settings (killswitch, cybersec, autoconnect, DNS), list available countries/servers, or manage NordVPN connections.
prerequisites:
  commands: [nordvpn]
metadata:
  hermes:
    tags: [vpn, network, security, nordvpn]
---

# NordVPN CLI

NordVPN is a VPN client for secure network connections.

## Common Commands

- Connect to fastest server: `nordvpn connect` or `nordvpn c`
- Connect to specific country: `nordvpn connect Chile`
- Connect to specific server (country_code + server_number): `nordvpn connect Chile123`
- Connect to server group: `nordvpn connect --group P2P` or `nordvpn connect --group Obfuscated Servers` or `nordvpn connect --group Double VPN`
- Disconnect: `nordvpn disconnect` or `nordvpn d`
- Check status: `nordvpn status`

## Server Discovery

- List all countries: `nordvpn countries`
- List cities in a country: `nordvpn cities Chile`
- List server groups: `nordvpn groups`
- Account information: `nordvpn account`

## Settings

- View all settings: `nordvpn settings`
- Killswitch on/off: `nordvpn set killswitch on` / `nordvpn set killswitch off`
- CyberSec on/off (blocks ads/malicious): `nordvpn set cybersec on` / `nordvpn set cybersec off`
- Autoconnect on/off: `nordvpn set autoconnect on` / `nordvpn set autoconnect off`
- Autoconnect to specific server: `nordvpn set autoconnect Chile123`
- Custom DNS: `nordvpn set dns 1.1.1.1` / `nordvpn set dns reset`
- Desktop notifications: `nordvpn set notify on` / `nordvpn set notify off`

## Protocols

- Show available: `nordvpn protocols`
- Set NordLynx (fastest): `nordvpn protocol nordlynx`
- Set OpenVPN UDP (most compatible): `nordvpn protocol openvpn_udp`
- Set OpenVPN TCP (restrictive networks): `nordvpn protocol openvpn_tcp`

## Whitelist (Bypass VPN)

- Add IP: `nordvpn whitelist add 192.168.1.1`
- Remove IP: `nordvpn whitelist remove 192.168.1.1`
- Remove all: `nordvpn whitelist remove all`

## Meshnet (Peer-to-Peer VPN)

- Enable: `nordvpn meshnet on`
- Status: `nordvpn meshnet`
- Invite peer: `nordvpn meshnet peer invite <email>`
- List peers: `nordvpn meshnet peer list`
- Disable: `nordvpn meshnet off`

## Account & Service

- Login: `nordvpn login`
- Logout: `nordvpn logout`
- Rate server: `nordvpn rate`
- Service management: `systemctl --user status nordvpn` / `start` / `stop` / `restart`

## Notes

- Killswitch recommended for privacy
- NordLynx is fastest, OpenVPN UDP most compatible
