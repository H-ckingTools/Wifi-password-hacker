import pywifi
from pywifi import const
import time

def find_open_networks():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # Use first Wi-Fi interface

    iface.scan()  # Start scanning
    time.sleep(3)  # Wait for scan to complete

    results = iface.scan_results()  # Get scan results
    open_networks = []

    for network in results:
        # If network uses no authentication (open network)
        if network.akm == [const.AKM_TYPE_NONE]:
            open_networks.append(network.ssid)

    if open_networks:
        print("Open (unsecured) Wi-Fi networks found:")
        for ssid in open_networks:
            print(f"  - {ssid}")
    else:
        print("No open Wi-Fi networks found.")

if __name__ == '__main__':
    find_open_networks()
