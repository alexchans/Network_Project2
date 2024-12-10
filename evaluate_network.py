import datetime
import matplotlib.pyplot as plt

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
        "Packet Loss (%)": (0, 1),
        "Duration (seconds)": (0, 20),
        "Avg Packet Size (bytes)": (0, 50),
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

if __name__ == "__main__":
    # Updated parameters to align with simplified traffic setup
    file_name = "financial_udp_traffic_details.txt"
    sent_packets = 1000  # Number of packets sent in traffic generation

    # Calculate metrics
    metrics = calculate_udp_metrics(file_name, sent_packets)

    print("Calculated UDP Metrics:")
    for k, v in metrics.items():
        print(f"{k}: {v}")

    # Plot the metrics
    plot_udp_metrics(metrics)
