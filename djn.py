import sys
from scapy.all import sniff, Ether, IP
import socket

def main():
    # Start packet sniffing on Wi-Fi interface
    start_sniffing()

def start_sniffing():
    interface = "Wi-Fi"
    print(f"Starting packet sniffing on interface {interface}...")

    # Dictionary to store unique source-destination pairs
    seen_pairs = {}

    # Sniff packets
    sniff(iface=interface, prn=lambda x: parse_packet(x, seen_pairs))

def parse_packet(packet, seen_pairs):
    if Ether in packet and IP in packet:
        source_ip = packet[IP].src
        dest_ip = packet[IP].dst

        # Create a unique key for each pair
        pair_key = (source_ip, dest_ip)

        # Check if this pair is already seen
        if pair_key not in seen_pairs:
            # Resolve IP addresses to hostnames
            source_hostname = resolve_ip(source_ip)
            dest_hostname = resolve_ip(dest_ip)

            # Print unique source-destination pairs with hostnames
            print(f"Source: {source_ip} ({source_hostname}) --> Destination: {dest_ip} ({dest_hostname})")

            # Mark this pair as seen
            seen_pairs[pair_key] = True

def resolve_ip(ip):
    try:
        hostname, _, _ = socket.gethostbyaddr(ip)
        return hostname
    except socket.herror:
        return "Unknown"

if __name__ == "__main__":
    main()
