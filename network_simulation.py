from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSSwitch, RemoteController

class MultiTierTopo(Topo):
    def build(self):
        # Add core switch
        core_switch = self.addSwitch('s1')
        
        # Add distribution switches
        dist_switch1 = self.addSwitch('s2')
        dist_switch2 = self.addSwitch('s3')
        
        # Add access switches
        access_switch1 = self.addSwitch('s4')
        access_switch2 = self.addSwitch('s5')

        # Add hosts
        host1 = self.addHost('h1')
        host2 = self.addHost('h2')
        host3 = self.addHost('h3')
        host4 = self.addHost('h4')

        # Link switches
        self.addLink(core_switch, dist_switch1)
        self.addLink(core_switch, dist_switch2)
        self.addLink(dist_switch1, access_switch1)
        self.addLink(dist_switch2, access_switch2)

        # Link hosts to access switches
        self.addLink(access_switch1, host1)
        self.addLink(access_switch1, host2)
        self.addLink(access_switch2, host3)
        self.addLink(access_switch2, host4)

def simulate_network():
    topo = MultiTierTopo()
    net = Mininet(topo=topo, switch=OVSSwitch, controller=RemoteController)
    net.start()
    print("Network is up!")
    net.pingAll()
    net.stop()

if __name__ == '__main__':
    simulate_network()
