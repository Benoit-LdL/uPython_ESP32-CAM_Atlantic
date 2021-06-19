### You should update the wifiCredentials file ###
import wifiCredentials
import network
import utime
import ntptime



def do_connect():
    
    sta_if = network.WLAN(network.STA_IF)
    start = utime.time()
    timed_out = False

    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(wifiCredentials.wifi_config["ssid"], wifiCredentials.wifi_config["password"])
        while not sta_if.isconnected() and \
            not timed_out:        
            if utime.time() - start >= 20:
                timed_out = True
            else:
                pass

    if sta_if.isconnected():
        ntptime.settime()
        print('network config:', sta_if.ifconfig())
    else: 
        print('internet not available')
    
    ###AP MODE
    '''

    ssid = 'LdL-Atlantic'
    password = '12345678'

    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid=ssid, password=password)

    while ap.active() == False:
        pass

    print('AP up and running')
    print(ap.ifconfig())
    '''
do_connect()