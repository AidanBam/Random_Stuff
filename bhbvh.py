from scapy.all import sniff, IP, UDP, DNS

def packet_callback(packet):
    if IP in packet and UDP in packet and packet[UDP].dport == 53:
        print("DNS Query Packet: ", packet.summary())
    elif IP in packet and UDP in packet and packet[UDP].sport == 53:
        print("DNS Response Packet: ", packet.summary())
    else:
        print("Packet does not contain a DNS layer")

# Use the correct interface name as identified from the list
packets = sniff(iface='Realtek 8852CE WiFi 6E PCI-E NIC', count=50, prn=packet_callback)