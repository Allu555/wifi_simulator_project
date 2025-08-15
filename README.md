# Wi-Fi Simulation Tool (Safe)

A safe Python-based project to **simulate Wi-Fi deauthentication attacks, network scans, and shell interactions**.  
Perfect for **educational demonstrations** and projects without affecting real networks.

## Features

- **Simulate deauth attacks** and save frames to `.pcap` files.
- **Simulate scanning a network** for connected clients.
- **Simulate shell access** on client devices.
- Safe: **No real packets are sent**.

## Requirements

- Python 3.6–3.12
- Scapy library

Install dependencies:

```bash
pip install -r requirements.txt


Usage
Simulate a deauthentication attack
python simulator.py --deauth -a 00:11:22:33:44:55 -c 66:77:88:99:AA:BB -o output.pcap

Simulate a network scan
python simulator.py --scan

Simulate opening a shell
python simulator.py --shell -c 66:77:88:99:AA:BB

Notes

Default MAC addresses are used if none are provided.

Simulation saves .pcap files for Wireshark analysis.

Completely safe and legal.
