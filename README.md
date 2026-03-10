# Packet-Sniffer
a multi-threaded TCP port scanner in Python using socket programming and the concurrent.futures ThreadPoolExecutor to scan target IP address.
Scans 12 of the most commonly used TCP ports (including SSH, HTTP, HTTPS, SMB, RDP, DNS) and reports their status with scan timestamps.

Captures TCP, UDP, and ICMP packets
Shows source and destination IPs and ports

Uses scapy a python library used for capturing and analysing network packets

Example Output
[TCP] 20.42.65.85:443 --> 192.168.0.6:56676
[UDP] 192.168.0.6:53 --> 8.8.8.8:53
[ICMP] 192.168.0.6 --> 8.8.8.8

Disclaimer
For educational purposes only. Only use on networks you have permission to monitor.
