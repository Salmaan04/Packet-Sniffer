from scapy.all import sniff, IP, TCP, UDP, ICMP

def process_packet(packet):
    if IP in packet:
        source_ip = packet[IP].src
        destination_ip = packet[IP].dst
        protocol = packet[IP].proto

        if TCP in packet:
            print(f"[TCP] {source_ip}:{packet[TCP].sport} --> {destination_ip}:{packet[TCP].dport}")
        elif UDP in packet:
            print(f"[UDP] {source_ip}:{packet[UDP].sport} --> {destination_ip}:{packet[UDP].dport}")
        elif ICMP in packet:
            print(f"[ICMP] {source_ip} --> {destination_ip}")
        else:
            print(f"[OTHER] {source_ip} --> {destination_ip} | Protocol: {protocol}")

print("Starting packet sniffer... Press CTRL+C to stop.\n")

sniff(prn=process_packet, store=False, count=50)
