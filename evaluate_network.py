import datetime
import matplotlib.pyplot as plt
import pyshark
from tcp_metrics import analyze_tcp_metrics
from icmp_metrics import analyze_icmp_metrics

def plot_tcp_metrics(metrics):
    """
    Visualize TCP metrics such as retransmissions and RTT.

    Args:
        metrics (dict): TCP metrics including retransmissions and RTT.
    """
    labels = ["Retransmissions", "Average RTT (ms)"]
    values = [metrics["retransmissions"], metrics["average_rtt"]]

    fig, axes = plt.subplots(1, 2, figsize=(12, 6))  # Create 1 row, 2 columns of subplots

    # Plot Retransmissions
    axes[0].bar(["Retransmissions"], [metrics["retransmissions"]], color="skyblue")
    axes[0].set_title("Retransmissions")
    axes[0].set_ylabel("Count")
    axes[0].set_xlabel("Metric")
    axes[0].bar_label(axes[0].containers[0], label_type="edge")  # Add labels to the bars

    # Plot Average RTT
    axes[1].bar(["Average RTT (ms)"], [metrics["average_rtt"]], color="lightgreen")
    axes[1].set_title("Average RTT")
    axes[1].set_ylabel("Milliseconds (ms)")
    axes[1].set_xlabel("Metric")
    axes[1].bar_label(axes[1].containers[0], label_type="edge")  # Add labels to the bars

    # Adjust layout
    plt.tight_layout()
    plt.show()
    
def plot_icmp_metrics(metrics):
    """
    Visualize ICMP metrics such as latency count and loss rate.

    Args:
        metrics (dict): ICMP metrics including average latency and loss rate.
    """
    labels = ["Latency Count (ms)", "Loss Rate (%)"]
    values = [metrics.get("latency_count", 0), metrics.get("loss_rate", 0)]

    fig, axes = plt.subplots(1, 2, figsize=(12, 6))  # Create 1 row, 2 columns of subplots

    # Plot Latency Count
    axes[0].bar(["Latency Count"], [metrics.get("latency_count", 0)], color="lightblue")
    axes[0].set_title("Latency Count")
    axes[0].set_ylabel("Count (ms)")
    axes[0].set_xlabel("Metric")
    axes[0].bar_label(axes[0].containers[0], label_type="edge")  # Add labels to the bars

    # Plot Loss Rate
    axes[1].bar(["Loss Rate"], [metrics.get("loss_rate", 0)], color="lightgreen")
    axes[1].set_title("Loss Rate")
    axes[1].set_ylabel("Percentage (%)")
    axes[1].set_xlabel("Metric")
    axes[1].bar_label(axes[1].containers[0], label_type="edge")  # Add labels to the bars

    # Adjust layout
    plt.tight_layout()
    plt.show()


def calculate_udp_metrics(file_name, sent_packets):
    """
    Calculate throughput, packet loss, duration, and average packet size from a filtered UDP traffic file.

    Args:
        file_name (str): Path to the filtered UDP traffic file.
        sent_packets (int): Number of packets sent.

    Returns:
        dict: Calculated metrics (throughput, packet loss, duration, average packet size).
    """
    captured_packets = 0
    total_bytes = 0
    timestamps = []

    with open(file_name, "r") as f:
        for line in f:
            if "Protocol: UDP" in line:
                captured_packets += 1
                length = int(line.split("Length:")[1].split(",")[0].strip())
                total_bytes += length

                # Parse the timestamp
                time_str = line.split("Time:")[1].split(",")[0].strip()
                try:
                    timestamp = datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S.%f")
                    timestamps.append(timestamp)
                except ValueError:
                    print(f"Invalid timestamp format: {time_str}")

    duration = (timestamps[-1] - timestamps[0]).total_seconds() if len(timestamps) > 1 else 0
    throughput = (total_bytes * 8) / (duration * 10**6) if duration > 0 else 0
    packet_loss = max(0, ((sent_packets - captured_packets) / sent_packets) * 100)
    avg_packet_size = total_bytes / captured_packets if captured_packets > 0 else 0

    return {
        "Throughput (Mbps)": round(throughput, 4),
        "Packet Loss (%)": round(packet_loss, 2),
        "Duration (seconds)": round(duration, 2),
        "Avg Packet Size (bytes)": round(avg_packet_size, 2),
    }

def calculate_icmp_latency(pcap_file):
    """
    Calculate ICMP latency by analyzing Echo Request and Echo Reply times.

    Args:
        pcap_file (str): Path to the input .pcapng file.

    Returns:
        list: List of latencies (in milliseconds).
    """
    latencies = []

    try:
        cap = pyshark.FileCapture(pcap_file, display_filter="icmp")

        request_times = {}
        for packet in cap:
            try:
                if hasattr(packet.icmp, "type"):
                    # Echo Request
                    if packet.icmp.type == "8":
                        request_id = packet.icmp.id
                        request_seq = packet.icmp.seq
                        request_times[(request_id, request_seq)] = float(packet.sniff_timestamp)

                    # Echo Reply
                    elif packet.icmp.type == "0":
                        reply_id = packet.icmp.id
                        reply_seq = packet.icmp.seq
                        if (reply_id, reply_seq) in request_times:
                            latency = (float(packet.sniff_timestamp) - request_times[(reply_id, reply_seq)]) * 1000
                            latencies.append(latency)
            except AttributeError:
                continue

        cap.close()
    except FileNotFoundError:
        print(f"Error: File {pcap_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return latencies

def plot_udp_metrics(metrics):
    """
    Visualize UDP network performance metrics using subplots with fixed y-limits for specific metrics.

    Args:
        metrics (dict): Dictionary containing throughput, packet loss, duration, and average packet size.
    """
    metric_names = list(metrics.keys())
    metric_values = list(metrics.values())

    # Define fixed y-limits for each metric
    y_limits = {
        "Throughput (Mbps)": (0, 0.035),
        "Packet Loss (%)": (0, 100),
        "Duration (seconds)": (0, 50),
        "Avg Packet Size (bytes)": (0, 100),
    }

    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    axes = axes.flatten()

    for i, (name, value) in enumerate(metrics.items()):
        axes[i].bar(name, value, alpha=0.7, color="skyblue")
        axes[i].set_title(name)
        axes[i].set_ylim(y_limits[name])  # Apply fixed y-limits
        axes[i].set_ylabel("Value")
        axes[i].grid(axis="y", linestyle="--", alpha=0.5)
        axes[i].text(0, value * 1.05, f"{value}", ha="center", va="bottom", fontsize=10, color="black")

    plt.tight_layout()
    plt.show()

def visualize_packet_distribution(metrics):
    """
    Visualize packet type distributions.
    """
    labels = list(metrics.keys())
    values = list(metrics.values())

    plt.figure(figsize=(8, 6))
    plt.bar(labels, values, color='skyblue')
    plt.title("Packet Type Distribution")
    plt.xlabel("Protocol")
    plt.ylabel("Count")
    plt.show()

def visualize_latency_histogram(latencies):
    """
    Visualize latency histogram.
    """
    plt.figure(figsize=(8, 6))
    plt.hist(latencies, bins=20, color='lightgreen', edgecolor='black')
    plt.title("Latency Histogram")
    plt.xlabel("Latency (ms)")
    plt.ylabel("Frequency")
    plt.show()

if __name__ == "__main__":
    # Updated parameters to align with simplified traffic setup
    file_name = "financial_traffic_details.txt"
    sent_packets = 5000  # Number of packets sent in traffic generation

    # Calculate metrics
    metrics = calculate_udp_metrics(file_name, sent_packets)
    
    # Calculate latencies
    latencies = calculate_icmp_latency("financial_traffics.pcapng")
    print(f"Calculated ICMP Latencies: {latencies}")
    
    print("Calculated UDP Metrics:")
    for k, v in metrics.items():
        print(f"{k}: {v}")

    # Plot the metrics
    plot_udp_metrics(metrics)
    
    # Analyze TCP metrics
    tcp_metrics = analyze_tcp_metrics("financial_traffics.pcapng")
    print("TCP Metrics:", tcp_metrics)

    # Visualize TCP metrics
    plot_tcp_metrics(tcp_metrics)

    # Analyze ICMP metrics
    icmp_metrics = analyze_icmp_metrics("financial_traffics.pcapng")
    print("ICMP Metrics:", icmp_metrics)

    # Visualize ICMP metrics
    plot_icmp_metrics(icmp_metrics)

