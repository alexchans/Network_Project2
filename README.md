
# CS5344 Project 2: Multi-Tier Network Simulation and Performance Analysis

---

## Introduction

This project focuses on designing and simulating a multi-tier network architecture for a large-scale enterprise scenario.
It evaluates network performance through metrics like throughput, packet loss, jitter, and duration while visualizing the
architecture using professional tools. The project also incorporates traffic generation and analysis to replicate real-world
conditions, providing a comprehensive framework for understanding network behavior in complex scenarios.

---

## Motivation

### Why Choose This Project?

The increasing reliance on robust, scalable, and secure network infrastructures in enterprises highlights the need for
detailed simulations and performance evaluations. This project bridges the gap between theoretical knowledge and practical
implementation by providing a hands-on approach to network design and performance testing.

### Usefulness

This project is particularly useful for:

- Network engineers and architects designing large-scale infrastructures.
- Enterprises requiring performance evaluation for existing or proposed networks.
- Students and researchers aiming to understand multi-tier network principles and performance metrics.

### Real-Life Scenario

We chose the scenario of a **large financial institution's data center network**. Such a network must handle:

1. **High Security**: Protect sensitive financial transactions.
2. **Scalability**: Support rapid growth in client data and services.
3. **Performance**: Ensure low latency and high availability for real-time transactions.

The multi-tier network replicates a data center infrastructure with:

- **Core Layer**: High-speed backbone switches for interconnection.
- **Distribution Layer**: Routing and policy enforcement for different departments.
- **Access Layer**: End-user devices, servers, and workstations.

---

## Methodology

### 1. Network Design and Simulation

- Used Python and NetworkX to design a multi-tier architecture with core, distribution, and access layers.
- Visualized the topology to understand connectivity and redundancy.

### 2. Traffic Generation

- Generated synthetic traffic using Scapy with realistic configurations:
  - Mixed protocols (UDP, TCP, ICMP).
  - Multiple source and destination IPs.
  - Varying data sizes and ports.

### 3. Traffic Capture and Analysis

- Captured traffic using Wireshark for detailed protocol-level inspection.
- Used Pyshark to process and filter packets based on specific criteria:
  - Protocol type.
  - Source and destination IPs.
  - Traffic size and timestamp.

### 4. Performance Evaluation

- Evaluated network metrics including throughput, packet loss, jitter, and duration using a custom Python script.
- Plotted metrics as subplots for clarity and deeper insights.

---

## Instructions for Running the Project

### 1. Prerequisites

- Install the following tools:
  - Python 3.8+ with `pip` package manager.
  - Wireshark for traffic capture.
  - Libraries: `scapy`, `pyshark`, `networkx`, `matplotlib`.

  Install dependencies:

  ```bash
  pip install scapy pyshark networkx matplotlib
  ```

### 2. Running the Project

#### Step 1: Network Simulation

1. Open `network_simulation.py`.
2. Run the script to visualize the network topology:

   ```bash
   python network_simulation.py
   ```

3. Review the visualized architecture to ensure it aligns with the real-life scenario.

#### Step 2: Generate Traffic

1. Open `traffic_generation.py`.
2. Edit the `src_ips`, `dst_ips`, and `iface` parameters to match your network configuration.
3. Run the script to generate traffic:

   ```bash
   python traffic_generation.py
   ```

4. Verify traffic is generated successfully.

#### Step 3: Capture Traffic

1. Open Wireshark and select the appropriate network interface.
2. Start traffic capture and save the file as `traffics.pcapng`.

#### Step 4: Analyze Traffic

1. Open `traffic_analysis.py`.
2. Set the `pcap_file` and `output_file` paths.
3. Run the script to extract traffic details:

   ```bash
   python traffic_analysis.py
   ```

#### Step 5: Evaluate Network Performance

1. Open `evaluate_network.py`.
2. Set the `file_name` parameter to the output of the analysis script.
3. Run the script to calculate and visualize performance metrics:

   ```bash
   python evaluate_network.py
   ```

---

## Viewing Output

### 1. Visualized Network Topology

- Output: A graph showing the network architecture layers and connections.
- Location: Displayed on execution of `network_simulation.py`.

### 2. Traffic Analysis

- Output: `traffic_details.txt` containing filtered packet information.

### 3. Performance Metrics

- Metrics: Throughput (Mbps), Packet Loss (%), Duration (seconds), Jitter (ms).
- Location: Console output and bar charts from `evaluate_network.py`.

---

## Summary and Conclusion

This project successfully simulates and evaluates a large-scale enterprise data center network. By integrating traffic generation,
analysis, and performance evaluation, it provides a robust framework for testing and understanding network behavior. Key takeaways:

- **Design**: Multi-tier architecture with core, distribution, and access layers enhances scalability and performance.
- **Traffic Insights**: Synthetic traffic and Wireshark capture ensure realistic testing.
- **Metrics Evaluation**: Calculated metrics provide actionable insights for optimization.

### Future Enhancements

- Implement additional redundancy for failover scenarios.
- Extend metrics to include latency and end-to-end delay.
- Automate the workflow for real-time testing and monitoring.

This project demonstrates the practical application of network concepts, bridging the gap between academic theory and real-world requirements.
