import networkx as nx
import matplotlib.pyplot as plt

class MultiTierNetwork:
    def __init__(self):
        self.network = nx.Graph()

    def build(self):
        # Core, Distribution, and Access layers
        self.network.add_edges_from([("Core", "Dist1"), ("Core", "Dist2")])
        self.network.add_edges_from([("Dist1", "Access1"), ("Dist2", "Access2")])

        # Hosts
        self.network.add_edges_from([("Access1", "Host1"), ("Access1", "Host2")])
        self.network.add_edges_from([("Access2", "Host3"), ("Access2", "Host4")])

    def visualize(self):
        # Draw the network
        pos = nx.spring_layout(self.network)  # Layout for the graph
        nx.draw(self.network, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=10)
        plt.title("Multi-Tier Network Topology")
        plt.show()

if __name__ == "__main__":
    network = MultiTierNetwork()
    network.build()
    network.visualize()
