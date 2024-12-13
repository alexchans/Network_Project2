import pyshark

def analyze_icmp_metrics(pcap_file):
    """
    Analyze ICMP ping latency and loss rate.

    Args:
        pcap_file (str): Path to the input .pcapng file.

    Returns:
        dict: Calculated ICMP metrics.
    """
    metrics = {
        "latency_sum": 0,
        "latency_count": 0,
        "average_latency": 0,
        "loss_rate": 0
    }

    try:
        cap = pyshark.FileCapture(pcap_file, display_filter="icmp")

        request_count = 0
        reply_count = 0
        latencies = []

        for packet in cap:
            try:
                # Check if the packet has an ICMP layer
                if "ICMP" in packet:
                    icmp_layer = packet.icmp

                    # Echo Request
                    if icmp_layer.type == "8":
                        request_count += 1

                    # Echo Reply
                    elif icmp_layer.type == "0":
                        reply_count += 1
                        if hasattr(packet, "sniff_timestamp"):
                            latencies.append(float(packet.sniff_timestamp))
            except AttributeError:
                continue

        cap.close()

        # Calculate metrics
        metrics["latency_count"] = len(latencies)
        metrics["loss_rate"] = ((request_count - reply_count) / request_count) * 100 if request_count > 0 else 0

        if metrics["latency_count"] > 0:
            metrics["average_latency"] = sum(latencies) / metrics["latency_count"]

        return metrics
    except FileNotFoundError:
        print(f"Error: File {pcap_file} not found.")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}


if __name__ == "__main__":
    pcap_file = "financial_traffics.pcapng"  # Example file
    icmp_metrics = analyze_icmp_metrics(pcap_file)
    print("ICMP Metrics:", icmp_metrics)
