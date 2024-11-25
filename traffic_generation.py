from scapy.all import sendp, Ether, IP, UDP

def generate_traffic(src_ip, dst_ip, iface, packets=10):
    for i in range(packets):
        pkt = Ether() / IP(src=src_ip, dst=dst_ip) / UDP(dport=80, sport=1024)
        sendp(pkt, iface=iface)
    print(f"Generated {packets} packets from {src_ip} to {dst_ip} on interface {iface}")

if __name__ == '__main__':
    generate_traffic('192.168.1.10', '192.168.1.20', 'eth0', packets=20)
