from napalm import get_network_driver

def configure_device(ip, username, password):
    driver = get_network_driver('ios')  # Replace 'ios' with your device OS type
    device = driver(ip, username, password)
    device.open()

    # Example configuration
    config_commands = [
        "interface loopback0",
        "ip address 192.168.1.1 255.255.255.0",
        "no shutdown"
    ]
    device.load_merge_candidate(config=config_commands)
    device.commit_config()
    print(f"Configuration applied to {ip}")
    device.close()

if __name__ == '__main__':
    configure_device('192.168.1.1', 'admin', 'password')
