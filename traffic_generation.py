import random
from scapy.all import sendp, Ether, IP, UDP, TCP, ICMP

def generate_traffic(src_ip, dst_ip, iface, packet_count=10):
    """
    Generate synthetic traffic by sending UDP packets from src_ip to dst_ip on the given interface.

    Args:
        src_ip (str): Source IP address.
        dst_ip (str): Destination IP address.
        iface (str): Network interface to use for sending packets.
        packet_count (int): Number of packets to send.
    """
    print(f"Generating {packet_count} packets (randomly, UDP, TCP, or ICMP) from {src_ip} to {dst_ip} on interface {iface}...")
    total_packets = 0
    
    for _ in range(packet_count):
        protocol_choice = random.choice(["UDP", "TCP", "ICMP"])
        if protocol_choice == "UDP":
            packet = Ether() / IP(src=src_ip, dst=dst_ip) / UDP(dport=80, sport=1024)
        elif protocol_choice == "TCP":
            packet = Ether() / IP(src=src_ip, dst=dst_ip) / TCP(dport=80, sport=1024)
        elif protocol_choice == "ICMP":
            packet = Ether() / IP(src=src_ip, dst=dst_ip) / ICMP()
            packet = Ether() / IP(src=src_ip, dst=dst_ip) / ICMP()
        else:
            print("Error in generating packet.")
            continue
        sendp(packet, iface=iface, verbose=False)
        total_packets += 1
        
    print(f"Traffic generation completed. Total packets sent: {total_packets}")

def stress_test(src_ip, dst_ip, iface, protocols, packet_rates):
    """
    Perform scalability testing by sending traffic at various loads.

    Args:
        src_ip (str): Source IP.
        dst_ip (str): Destination IP.
        iface (str): Network interface.
        protocols (list): List of protocols to use.
        packet_rates (list): List of packet rates (packets per second).
    """
    for rate in packet_rates:
        print(f"Generating traffic at {rate} packets/second.")
        for _ in range(rate):
            protocol = random.choice(protocols)
            if protocol == "UDP":
                packet = Ether() / IP(src=src_ip, dst=dst_ip) / UDP(dport=80, sport=1024)
            elif protocol == "TCP":
                packet = Ether() / IP(src=src_ip, dst=dst_ip) / TCP(dport=80, sport=1024)
            elif protocol == "ICMP":
                packet = Ether() / IP(src=src_ip, dst=dst_ip) / ICMP()
            sendp(packet, iface=iface, verbose=False)

if __name__ == "__main__":
    # Network parameters
    src_ip = "192.168.50.190"  # Your Wi-Fi adapter IPv4 address
    dst_ip = "192.168.50.1"    # Default gateway
    iface = "Wi-Fi"            # Network interface name
    packet_count = 5000        # Number of packets to send

    # Generate traffic
    generate_traffic(src_ip, dst_ip, iface, packet_count)
