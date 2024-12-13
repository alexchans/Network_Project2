import pyshark
import sqlite3
from icmp_metrics import analyze_icmp_metrics
from tcp_metrics import analyze_tcp_metrics
import numpy as np

def store_in_database(details):
    """
    Store traffic details in the SQLite database.

    Args:
        details (list): List of traffic details as dictionaries.
    """
    try:
        conn = sqlite3.connect("network_data.db")
        cursor = conn.cursor()

        # Insert records
        for detail in details:
            cursor.execute("""
                INSERT INTO traffic_records (time, protocol, length, source, destination)
                VALUES (?, ?, ?, ?, ?)
            """, (detail['time'], detail['protocol'], detail['length'], detail['source'], detail['destination']))

        conn.commit()
        print("Traffic details saved to database.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

def extract_traffic(pcap_file, output_file, src_ip, dst_ip, protocols=["UDP", "TCP", "ICMP"]):
    """
    Extract traffic for specified protocols from a given .pcapng file and save details to a text file.

    Args:
        pcap_file (str): Path to the input .pcapng file.
        output_file (str): Path to the output text file.
        src_ip (str): Source IP to filter.
        dst_ip (str): Destination IP to filter.
        protocols (list): List of protocols to filter (e.g., ["UDP", "TCP", "ICMP"]).
    """
    print(f"Analyzing {pcap_file} to extract traffic for protocols: {', '.join(protocols)}...")
    traffic_details = []

    try:
        # Open the .pcapng file with protocol filter
        cap = pyshark.FileCapture(pcap_file, display_filter=" or ".join([p.lower() for p in protocols]))

        for packet in cap:
            try:
                protocol = packet.transport_layer if hasattr(packet, "transport_layer") else "N/A"
                length = int(packet.length) if hasattr(packet, "length") else "N/A"
                source = packet.ip.src if hasattr(packet, "ip") else "N/A"
                destination = packet.ip.dst if hasattr(packet, "ip") else "N/A"
                time = str(packet.sniff_time)

                traffic_details.append({
                    "time": time,
                    "protocol": protocol,
                    "length": length,
                    "source": source,
                    "destination": destination
                })
            except AttributeError:
                continue

        cap.close()
        with open(output_file, "w") as f:
            f.write("Filtered Traffic Details:\n")
            f.write("=" * 40 + "\n")
            for detail in traffic_details:
                f.write(
                    f"Time: {detail['time']}, Protocol: {detail['protocol']}, "
                    f"Length: {detail['length']}, Source: {detail['source']}, "
                    f"Destination: {detail['destination']}\n"
                )

        store_in_database(traffic_details)
        print(f"Filtered traffic details saved to {output_file} and database.")
    except FileNotFoundError:
        print(f"Error: File {pcap_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def detect_anomalies(metrics, threshold=3):
    """
    Detect anomalies based on z-score.

    Args:
        metrics (list): List of packet sizes or latencies.
        threshold (int): Z-score threshold for anomaly detection.
    """
    import numpy as np

    mean = np.mean(metrics)
    std_dev = np.std(metrics)
    anomalies = [x for x in metrics if abs((x - mean) / std_dev) > threshold]

    print(f"Detected {len(anomalies)} anomalies out of {len(metrics)} samples.")
    return anomalies


if __name__ == "__main__":
    
    pcap_file = "financial_traffics.pcapng"             # Example capture file
    output_file = "financial_traffic_details.txt"       # Output file name
    src_ip = "192.168.50.190"                           # Single source IP
    dst_ip = "192.168.50.1"                             # Single destination IP

    # Extract UDP traffic details
    extract_traffic(pcap_file, output_file, src_ip, dst_ip)
    
    # Analyze ICMP metrics
    icmp_metrics = analyze_icmp_metrics(pcap_file)
    print("ICMP Metrics:", icmp_metrics)

    # Analyze TCP metrics
    tcp_metrics = analyze_tcp_metrics(pcap_file)
    print("TCP Metrics:", tcp_metrics)
    
