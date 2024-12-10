import pyshark

def extract_udp_traffic(pcap_file, output_file, src_ip, dst_ip):
    """
    Extract UDP traffic from a given .pcapng file and save details to a text file.

    Args:
        pcap_file (str): Path to the input .pcapng file.
        output_file (str): Path to the output text file.
        src_ip (str): Source IP to filter.
        dst_ip (str): Destination IP to filter.
    """
    print(f"Analyzing {pcap_file} to extract UDP traffic from {src_ip} to {dst_ip}...")
    traffic_details = []

    try:
        # Open the .pcapng file with a UDP filter
        cap = pyshark.FileCapture(pcap_file, display_filter="udp")

        for packet in cap:
            try:
                source = packet.ip.src if hasattr(packet, "ip") else "N/A"
                destination = packet.ip.dst if hasattr(packet, "ip") else "N/A"

                if source == src_ip and destination == dst_ip:
                    protocol = packet.transport_layer if hasattr(packet, "transport_layer") else "N/A"
                    length = packet.length if hasattr(packet, "length") else "N/A"
                    time = packet.sniff_time

                    traffic_details.append(
                        f"Time: {time}, Protocol: {protocol}, Length: {length}, "
                        f"Source: {source}, Destination: {destination}"
                    )
            except AttributeError:
                continue

        cap.close()
        with open(output_file, "w") as f:
            f.write("Filtered UDP Traffic Details:\n")
            f.write("=" * 40 + "\n")
            for detail in traffic_details:
                f.write(detail + "\n")

        print(f"Filtered UDP traffic details saved to {output_file}.")
    except FileNotFoundError:
        print(f"Error: File {pcap_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    
    pcap_file = "financial_traffics.pcapng"             # Example capture file
    output_file = "financial_udp_traffic_details.txt"   # Output file name
    src_ip = "192.168.50.190"                           # Single source IP
    dst_ip = "192.168.50.1"                             # Single destination IP

    # Extract UDP traffic details
    extract_udp_traffic(pcap_file, output_file, src_ip, dst_ip)
