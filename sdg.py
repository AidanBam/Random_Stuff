from scapy.all import sniff, DNS, DNSQR

def process_dns_packet(packet):
    if DNS in packet and packet[DNS].opcode == 0:  # Standard query
        queried_domain = packet[DNSQR].qname.decode('utf-8')
        print("Queried Domain:", queried_domain)

# Sniff DNS traffic on the network
sniff(filter="udp port 53", prn=process_dns_packet)
