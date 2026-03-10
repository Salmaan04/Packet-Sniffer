# Packet-Sniffer
A simple network packet sniffer built in Python using Scapy that captures and displays live network traffic in real time.
Features

Captures TCP, UDP, and ICMP packets
Shows source and destination IPs and ports
Runs in the terminal

Usage
pip install scapy
sudo python3 packet_sniffer.py

Example Output
[TCP] 20.42.65.85:443 --> 192.168.0.6:56676
[UDP] 192.168.0.6:53 --> 8.8.8.8:53
[ICMP] 192.168.0.6 --> 8.8.8.8

Disclaimer
For educational purposes only. Only use on networks you have permission to monitor.
