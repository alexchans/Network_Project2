import pyshark

def analyze_traffic(pcap_file):
    cap = pyshark.FileCapture(pcap_file)
    for packet in cap:
        print(f"Packet: {packet.sniff_time}, {packet.highest_layer}")

if __name__ == '__main__':
    analyze_traffic('traffic_capture.pcap')
