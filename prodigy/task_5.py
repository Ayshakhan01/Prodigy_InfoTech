import scapy.all as scapy

def packet_callback(packet):
    if packet.haslayer(scapy.IP):
        src_ip = packet[scapy.IP].src
        dst_ip = packet[scapy.IP].dst
        protocol = packet[scapy.IP].proto
        
        print(f"Source IP: {src_ip} --> Destination IP: {dst_ip} Protocol: {protocol}")

# Sniff packets on the network interface
scapy.sniff(prn=packet_callback, store=False)
