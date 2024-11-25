import matplotlib.pyplot as plt

def plot_metrics(metrics):
    plt.bar(metrics.keys(), metrics.values(), color='lightblue')
    plt.title("Network Performance Metrics")
    plt.xlabel("Metric")
    plt.ylabel("Value")
    plt.show()

if __name__ == "__main__":
    # Sample metrics data
    metrics = {
        "Throughput (Mbps)": 450,
        "Latency (ms)": 25,
        "Packet Loss (%)": 0.2
    }
    plot_metrics(metrics)
