import pyshark

def extract_udp_traffic(pcap_file, output_file, src_ip, dst_ip):
    """
    Extract UDP traffic from a given .pcapng file and save details to a text file.

    Args:
        pcap_file (str): Path to the input .pcapng file.
        output_file (str): Path to the output text file.
        src_ip (str): Source IP to filter (e.g., '192.168.1.9').
        dst_ip (str): Destination IP to filter (e.g., '192.168.1.1').
    """
    print(f"Analyzing {pcap_file} to extract UDP traffic from {src_ip} to {dst_ip}...")
    udp_packets = []

    try:
        # Open the .pcapng file
        cap = pyshark.FileCapture(pcap_file, display_filter="udp")

        # Process packets
        for packet in cap:
            try:
                # Extract source and destination IPs
                source = packet.ip.src
                destination = packet.ip.dst

                # Filter by source and destination IP
                if source == src_ip and destination == dst_ip:
                    # Extract packet details
                    time = packet.sniff_time
                    protocol = packet.transport_layer
                    length = packet.length
                    udp_packets.append(
                        f"Time: {time}, Protocol: {protocol}, Length: {length}, "
                        f"Source: {source}, Destination: {destination}"
                    )
            except AttributeError:
                # Skip packets without IP layer
                continue

        cap.close()

        # Write filtered packets to output file
        with open(output_file, "w") as f:
            f.write("Filtered UDP Traffic:\n")
            f.write("=" * 40 + "\n")
            for packet in udp_packets:
                f.write(packet + "\n")

        print(f"Filtered UDP traffic saved to {output_file}.")

    except FileNotFoundError:
        print(f"Error: File {pcap_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Input .pcapng file and output .txt file
    pcap_file = "traffics.pcapng"  # Path to your .pcapng file
    output_file = "traffics.txt"  # Output file name

    # Filter parameters
    src_ip = "192.168.1.9"  # Source IP
    dst_ip = "192.168.1.1"  # Destination IP

    # Extract UDP traffic
    extract_udp_traffic(pcap_file, output_file, src_ip, dst_ip)
