
# CS5344 Project 2: Multi-Tier Network Simulation and Performance Analysis

---

## Introduction

This project focuses on designing and simulating a multi-tier network architecture for a large-scale enterprise scenario.
It evaluates network performance with dynamic visualizations through metrics like throughput, packet loss, and duration
while visualizing the architecture using professional tools. The project also incorporates traffic generation using mixed
protocols and analysis to replicate real-world conditions, providing a comprehensive framework for understanding network
behavior in complex scenarios.

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

## Directory Structure

- `evaluate_network.py`: Visualizes and evaluates network performance metrics.
- `icmp_metrics.py`: Calculates ICMP-specific metrics.
- `tcp_metrics.py`: Calculates TCP-specific metrics.
- `traffic_generation.py`: Generates synthetic traffic and supports stress testing.
- `traffic_analysis.py`: Extracts traffic details and performs anomaly detection.
- `network_simulation.py`: Simulates a multi-tier network and supports failure testing.
- `setup_database.py`: Initializes a SQLite database for storing traffic details.
- `query_database.py`: Queries the database with filters for protocol and packet size.

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

- Evaluated network metrics including throughput, packet loss, and duration using a custom Python script.
- Plotted metrics as subplots for clarity and deeper insights.

---

## Key Features and Functionalities

1. **Dynamic Traffic Generation:**
   - Generates synthetic traffic using Scapy with UDP, TCP, and ICMP protocols.
   - Includes stress testing with parameterized traffic loads.

2. **Traffic Analysis:**
   - Extracts and filters traffic details from `.pcapng` files.
   - Calculates ICMP metrics (latency, loss rate) and TCP metrics (retransmissions, RTT).

3. **Performance Visualization:**
   - Visualizes metrics like throughput, latency, and packet loss.
   - Generates histograms and bar charts for detailed analysis.

4. **Anomaly Detection:**
   - Identifies unusual traffic patterns based on z-scores.

5. **Database Integration:**
   - Saves traffic details to a SQLite database for querying.
   - Supports advanced filtering by protocol and packet length.

6. **Network Topology Simulation:**
   - Simulates a multi-tier data center network.
   - Allows for failure scenarios to test network robustness.

---

## Instructions for Running the Project

### Step 1: Set Up the Environment

1. Install the required Python libraries:

   ```bash
   pip install scapy pyshark networkx matplotlib
   ```

2. Ensure Wireshark is installed to capture `.pcapng` files.

### Step 2: Initialize the Database

1. Run the database setup script:

   ```bash
   python setup_database.py
   ```

2. Verify that `network_data.db` is created successfully.

---

### Step 3: Simulate Network Topology

1. Open and execute `network_simulation.py`:

   ```bash
   python network_simulation.py
   ```

2. Visualize the multi-tier network architecture and test node or link failures.

---

### Step 4: Generate Traffic

1. Open `traffic_generation.py`.
2. Set parameters:
   - `src_ip`: Source IP address (e.g., your machine's IP).
   - `dst_ip`: Destination IP address (e.g., router's IP).
   - `iface`: Network interface (e.g., "Wi-Fi").
3. Generate traffic:

   ```bash
   python traffic_generation.py
   ```

---

### Step 5: Capture and Analyze Traffic

1. Capture traffic using Wireshark and save it as `financial_traffics.pcapng`.
2. Run `traffic_analysis.py` to extract and analyze traffic details:

   ```bash
   python traffic_analysis.py
   ```

3. Output:
   - `financial_traffic_details.txt`: Filtered traffic details.
   - Traffic saved to the database for querying.

---

### Step 6: Evaluate Network Performance

1. Run `evaluate_network.py` to calculate and visualize metrics:

   ```bash
   python evaluate_network.py
   ```

2. Metrics visualized:
   - TCP retransmissions and RTT.
   - ICMP latency and loss rate.
   - UDP throughput and packet loss.

---

### Step 7: Query Traffic Details

1. Run `query_database.py` to filter traffic details by protocol or length:

   ```bash
   python query_database.py
   ```

2. Example queries:
   - Retrieve all UDP packets.
   - Filter TCP packets with a length above 50 bytes.

---

## Viewing Output

### 1. Visualized Network Topology

- Output: A graph showing the network architecture layers and connections.
- Location: Displayed on execution of `network_simulation.py`.

### 2. Traffic Analysis

- **File:** `traffic_details.txt` containing filtered packet information.
- **Database:** `network_data.db`

### 3. Performance Metrics

- Metrics: Throughput (Mbps), Packet Loss (%), Duration (seconds), as well as TCP and ICMP metrics.
- Location: Console output and bar charts from `evaluate_network.py`.

---

## Summary and Conclusion

This project successfully simulates and evaluates a large-scale enterprise data center network. By integrating traffic generation,
analysis, and performance evaluation, it provides a robust framework for testing and understanding network behavior. Key takeaways:

- **Design**: Multi-tier architecture with core, distribution, and access layers enhances scalability and performance.
- **Traffic Insights**: Synthetic traffic and Wireshark capture ensure realistic testing.
- **Metrics Evaluation**: Calculated metrics provide actionable insights for optimization.
