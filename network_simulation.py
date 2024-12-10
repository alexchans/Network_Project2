import networkx as nx
import matplotlib.pyplot as plt

class FinancialDataCenterNetwork:
    def __init__(self):
        self.network = nx.DiGraph()

    def build(self):
        # Adding a realistic financial data center network topology
        # Core Layer
        self.network.add_node("CoreSwitch-FDC1", layer="Core")
        self.network.add_node("CoreSwitch-FDC2", layer="Core")

        # Distribution Layer (Departments)
        departments = ["Accounting", "IT", "HR"]
        for dept in departments:
            self.network.add_node(f"DistSwitch-{dept}", layer="Distribution")
            self.network.add_edge("CoreSwitch-FDC1", f"DistSwitch-{dept}", capacity=10)
            self.network.add_edge("CoreSwitch-FDC2", f"DistSwitch-{dept}", capacity=10)

        # Access Layer (Floors)
        for dept in departments:
            for floor in range(1, 6):  # Five floors per department
                self.network.add_node(f"AccessSwitch-{dept}-Floor{floor}", layer="Access")
                self.network.add_edge(f"DistSwitch-{dept}", f"AccessSwitch-{dept}-Floor{floor}", capacity=1)

        # Host Layer (Workstations)
        for dept in departments:
            for floor in range(1, 6):
                for workstation_id in range(1, 4):  # Three workstations per floor
                    host_name = f"Workstation-{dept}-Floor{floor}-{workstation_id}"
                    self.network.add_node(host_name, layer="Host")
                    self.network.add_edge(f"AccessSwitch-{dept}-Floor{floor}", host_name, capacity=0.1)

    def visualize(self):
        # Custom layout based on layers
        pos = nx.multipartite_layout(self.network, subset_key="layer")
        plt.figure(figsize=(18, 12))
        nx.draw(
            self.network,
            pos,
            with_labels=True,
            node_size=30,
            node_color="lightblue",
            font_size=4,
            font_weight='bold',
            arrows=True,
            arrowsize=5,
            width=0.25,
        )
        plt.title("Financial Data Center Network Topology", fontsize=14)
        plt.show()

if __name__ == "__main__":
    network = FinancialDataCenterNetwork()
    network.build()
    network.visualize()
