from scapy.all import sendp, Ether, IP, UDP

def generate_traffic(src_ip, dst_ip, iface, packet_count=10):
    """
    Generate synthetic traffic by sending packets from src_ip to dst_ip on the given interface.

    Args:
        src_ip (str): Source IP address.
        dst_ip (str): Destination IP address.
        iface (str): Network interface to use for sending packets.
        packet_count (int): Number of packets to send.
    """
    print(f"Generating {packet_count} packets from {src_ip} to {dst_ip} on interface {iface}...")
    for _ in range(packet_count):
        packet = Ether() / IP(src=src_ip, dst=dst_ip) / UDP(dport=80, sport=1024)
        sendp(packet, iface=iface, verbose=False)
    print("Traffic generation completed.")

if __name__ == "__main__":
    # Update the source and destination IPs based on your network setup
    src_ip = "100.64.250.250"  # Your Wi-Fi interface IPv4 address
    dst_ip = "100.64.250.1"    # Gateway or another reachable device in the same network
    iface = "Wi-Fi"            # Active interface name as detected
    generate_traffic(src_ip, dst_ip, iface, packet_count=20)
