from scapy.all import *

iface = "wlan0"  # Your Wi-Fi card in monitor mode

def find_ap(pkt):
    if pkt.haslayer(Dot11Beacon):  # Beacon frame
        bssid = pkt[Dot11].addr2   # AP's MAC
        ssid = pkt[Dot11Elt].info.decode(errors='ignore')  # Network name
        print(f"SSID: {ssid}, BSSID: {bssid}")

sniff(iface=iface, prn=find_ap, store=0)
