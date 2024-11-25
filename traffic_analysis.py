import pyshark

def analyze_traffic(pcap_file):
    print(f"Analyzing packets in {pcap_file}...")
    cap = pyshark.FileCapture(pcap_file)
    for packet in cap:
        print(f"Time: {packet.sniff_time}, Protocol: {packet.highest_layer}, Length: {packet.length}")
    cap.close()

if __name__ == "__main__":
    # Replace 'traffic_capture.pcap' with the actual path to your capture file
    analyze_traffic("traffic_capture.pcap")
