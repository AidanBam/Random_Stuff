from scapy.all import sniff, UDP, DNS, DNSQR, DNSRR, IP, Ether, get_if_list
import socket
import scapy

def main( ):
    # Start packet sniffing on the specified interface
    start_sniffing( )

def start_sniffing():
    interface_name = "Wi-Fi"  # Replace with your actual interface name
    print(f"Starting packet sniffing on interface {interface_name}...")

    # Dictionary to store unique source-destination pairs
    seen_pairs = {}

    # Sniff DNS packets on the specified interface
    sniff(filter="udp port 52", prn=lambda packet: process_packet(packet, seen_pairs), iface=interface_name, store=0)

def process_packet(packet, seen_pairs):
    if IP in packet:
        if UDP in packet and DNS in packet and (DNSQR in packet or DNSRR in packet):
            if DNSQR in packet:
                queried_domain = packet[ DNSQR ].qname.decode( 'utf-8' ).rstrip( '.' )
                source_ip = packet[ IP ].src
                source_hostname = resolve_ip( source_ip )
                print( f"DNS Query - Source IP: {source_ip}, Source Hostname: {source_hostname}, Queried Domain: {queried_domain}" )
        else:
            print("Not a DNS packet")
    else:
        print("Packet does not contain an IP layer")

        # Process DNS responses
        if DNSRR in packet:
            for i in range( packet[ DNS ].ancount ):
                dnsrr = packet[ DNSRR ][ i ]
                print( f"DNS Response - Queried Domain: {dnsrr.rrname.decode( 'utf-8' ).rstrip( '.' )}, Resolved IP: {dnsrr.rdata}" )

        # Check for unique source-destination pairs
        source_ip = packet[ IP ].src
        dest_ip = packet[ IP ].dst
        pair_key = (source_ip, dest_ip)
        if pair_key not in seen_pairs:
            dest_hostname = resolve_ip( dest_ip )
            print( f"Unique Pair - Source: {source_ip} ({source_hostname}) --> Destination: {dest_ip} ({dest_hostname})" )
            seen_pairs[ pair_key ] = True
        else:
            print( "Not a DNS packet" )


def resolve_ip( ip ):
    try:
        hostname, _, _ = socket.gethostbyaddr( ip )
        return hostname
    except socket.herror:
        return "Unknown"


if __name__ == "__main__":
    main( )