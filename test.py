from scapy.all import ARP, Ether, srp
from socket import gethostbyaddr

def hostname(ip):
    try:
        return gethostbyaddr(ip)
    except:
        return 'Local Network'

def arp_scan(ip_range):
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    result = srp(packet, timeout=2, verbose=0)[0]

    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    for device in devices:
        print(f"IP: {device['ip']} | MAC: {device['mac']} | name : {hostname(device['ip'])}")

# Example usage
arp_scan("192.168.28.0/24")
