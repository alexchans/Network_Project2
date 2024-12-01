from scapy.all import sendp, Ether, IP, UDP

def generate_traffic(src_ip, dst_ip, iface, packet_count=10):
    """
    Generate synthetic traffic by sending UDP packets from src_ip to dst_ip on the given interface.

    Args:
        src_ip (str): Source IP address.
        dst_ip (str): Destination IP address.
        iface (str): Network interface to use for sending packets.
        packet_count (int): Number of packets to send.
    """
    print(f"Generating {packet_count} UDP packets from {src_ip} to {dst_ip} on interface {iface}...")
    for _ in range(packet_count):
        packet = Ether() / IP(src=src_ip, dst=dst_ip) / UDP(dport=80, sport=1024)
        sendp(packet, iface=iface, verbose=False)
    print("Traffic generation completed.")

if __name__ == "__main__":
    # Network parameters
    src_ip = "192.168.1.9"   # Your Wi-Fi adapter IPv4 address
    dst_ip = "192.168.1.1"   # Default gateway
    iface = "Wi-Fi"          # Network interface name
    packet_count = 20        # Number of packets to send

    # Generate traffic
    generate_traffic(src_ip, dst_ip, iface, packet_count)
