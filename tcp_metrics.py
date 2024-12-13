import pyshark

def analyze_tcp_metrics(pcap_file):
    """
    Analyze TCP retransmissions, round-trip time (RTT), and congestion windows.

    Args:
        pcap_file (str): Path to the input .pcapng file.

    Returns:
        dict: Calculated TCP metrics.
    """
    metrics = {
        "retransmissions": 0,
        "average_rtt": 0,
        "packet_count": 0
    }
    total_rtt = 0

    try:
        cap = pyshark.FileCapture(pcap_file, display_filter="tcp")

        for packet in cap:
            try:
                if hasattr(packet.tcp, "analysis_retransmission"):
                    metrics["retransmissions"] += 1

                if hasattr(packet.tcp, "analysis_ack_rtt"):
                    rtt = float(packet.tcp.analysis_ack_rtt)
                    total_rtt += rtt
                    metrics["packet_count"] += 1
            except AttributeError:
                continue

        cap.close()

        if metrics["packet_count"] > 0:
            metrics["average_rtt"] = total_rtt / metrics["packet_count"]

        return metrics
    except FileNotFoundError:
        print(f"Error: File {pcap_file} not found.")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}

if __name__ == "__main__":
    pcap_file = "financial_traffics.pcapng"
    metrics = analyze_tcp_metrics(pcap_file)
    print("TCP Metrics:", metrics)
