#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import sys
import platform
from scapy.all import RadioTap, Dot11, Dot11Deauth, wrpcap

# --------------------- Utilities ---------------------
def stdOutput(status):
    if status == "error":
        return "[ERROR] "
    elif status == "info":
        return "[INFO] "
    return ""

def clearScreen():
    print("\033c", end="")  # Clear terminal

# --------------------- Simulation Functions ---------------------
def simulate_deauth(ap_mac, client_mac, output_file="simulated_deauth.pcap"):
    frame = RadioTap()/Dot11(addr1=client_mac, addr2=ap_mac, addr3=ap_mac)/Dot11Deauth(reason=7)
    print(stdOutput("info")+"Simulated Deauthentication Frame:")
    frame.show()
    wrpcap(output_file, [frame])
    print(stdOutput("info")+f"Simulation saved to {output_file}")

def simulate_network_scan():
    fake_clients = [
        "66:77:88:99:AA:01",
        "66:77:88:99:AA:02",
        "66:77:88:99:AA:03"
    ]
    print(stdOutput("info")+"Simulated Network Scan Results:")
    for client in fake_clients:
        print(f"  - Client MAC: {client}")
    return fake_clients

def simulate_shell(client_mac):
    print(stdOutput("info")+f"Simulated shell session opened with {client_mac}")
    print(stdOutput("info")+"Type 'exit' to close simulation.")
    while True:
        cmd = input(f"{client_mac}> ")
        if cmd.lower() == "exit":
            break
        print(stdOutput("info")+f"Simulated output: Executed '{cmd}' successfully.")

# --------------------- Argument Parsing ---------------------
parser = argparse.ArgumentParser(description="Safe Wi-Fi Simulation Tool for Projects")
parser.add_argument('--deauth', help='Simulate a deauth attack', action='store_true')
parser.add_argument('--scan', help='Simulate network scanning', action='store_true')
parser.add_argument('--shell', help='Simulate opening a shell on a client', action='store_true')
parser.add_argument('-a','--ap', metavar="<AP_MAC>", type=str, help='Access Point MAC address')
parser.add_argument('-c','--client', metavar="<CLIENT_MAC>", type=str, help='Client MAC address')
parser.add_argument('-o','--output', metavar="<FILE>", type=str, help='Output file for deauth simulation', default="simulated_deauth.pcap")
args = parser.parse_args()

# --------------------- Python Version Check ---------------------
if float(platform.python_version()[:3]) < 3.6 or float(platform.python_version()[:3]) > 3.12:
    print(stdOutput("error")+"Python version should be between 3.6 to 3.12")
    sys.exit()

# --------------------- Main ---------------------
clearScreen()
if args.deauth:
    ap_mac = args.ap if args.ap else "00:11:22:33:44:55"
    client_mac = args.client if args.client else "66:77:88:99:AA:BB"
    simulate_deauth(ap_mac, client_mac, args.output)

elif args.scan:
    simulate_network_scan()

elif args.shell:
    client_mac = args.client if args.client else "66:77:88:99:AA:BB"
    simulate_shell(client_mac)

else:
    print(stdOutput("error")+"No action specified. Use --deauth, --scan, or --shell")
