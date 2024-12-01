import datetime
import matplotlib.pyplot as plt

def calculate_metrics(file_name, sent_packets):
    """
    Calculate throughput, packet loss, and duration from a filtered UDP traffic file.

    Args:
        file_name (str): Path to the filtered UDP traffic file.
        sent_packets (int): Number of packets sent.

    Returns:
        dict: Calculated metrics (throughput, packet loss, duration).
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

    # Calculate duration
    if len(timestamps) > 1:
        duration = (timestamps[-1] - timestamps[0]).total_seconds()
    else:
        duration = 0  # Handle cases with 0 or 1 packet

    # Calculate throughput
    throughput = (total_bytes * 8) / (duration * 10**6) if duration > 0 else 0

    # Calculate packet loss
    packet_loss = max(0, ((sent_packets - captured_packets) / sent_packets) * 100)

    return {
        "Throughput (Mbps)": round(throughput, 2),
        "Packet Loss (%)": round(packet_loss, 2),
        "Duration (seconds)": round(duration, 2)
    }

def plot_metrics(metrics):
    """
    Visualize network performance metrics using bar charts.

    Args:
        metrics (dict): Dictionary containing throughput, packet loss, and duration.
    """
    # Create a bar chart
    plt.bar(metrics.keys(), metrics.values(), alpha=0.7)
    plt.title("Network Performance Metrics")
    plt.ylabel("Value")
    plt.xlabel("Metrics")
    plt.ylim(0, max(metrics.values()) + 10)  # Add some padding to the y-axis
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.show()

if __name__ == "__main__":
    # Input file with filtered UDP packets
    file_name = "traffics.txt"
    sent_packets = 20  # Number of packets sent by traffic_generation.py

    # Calculate metrics
    metrics = calculate_metrics(file_name, sent_packets)

    # Print the calculated metrics
    print("Calculated Metrics:")
    print(metrics)

    # Plot the metrics
    plot_metrics(metrics)
