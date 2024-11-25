import matplotlib.pyplot as plt

def plot_performance(metrics):
    plt.bar(metrics.keys(), metrics.values())
    plt.title("Network Performance")
    plt.xlabel("Metric")
    plt.ylabel("Value")
    plt.show()

if __name__ == '__main__':
    metrics = {
        "Throughput (Mbps)": 500,
        "Latency (ms)": 20,
        "Packet Loss (%)": 0.5
    }
    plot_performance(metrics)
