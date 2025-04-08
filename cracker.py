from pywifi import *


def getWifiadapters():
    wifi = PyWiFi()
    get_wifi_adapters = wifi.interfaces()
    adapters = []

    for _apapters in get_wifi_adapters:
        adapters.append(_apapters)

    if len(adapters) == 0:
        return 'No adapter is found!'
    else:
        return adapters

def connector(ssid,password):
    pass


if __name__ == '__main__':
    print(getWifiadapters())