from scapy.all import sniff, UDP, DNS, DNSQR, IP

def process_dns_packet(packet):
    if UDP in packet and DNS in packet and DNSQR in packet:
        queried_domain = packet[DNSQR].qname.decode('utf-8')
        source_ip = packet[IP].src if IP in packet else "Unknown"
        print(f"Source IP: {source_ip}, Queried Domain: {queried_domain}")
    else:
        print("Not a DNS packet")

# Sniff DNS traffic on the network interface "Wi-Fi"
sniff(filter="udp port 53", prn=process_dns_packet, iface="Wi-Fi")
