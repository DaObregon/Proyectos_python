import wifi

def scan_wifi():
    wifi_list = wifi.Cell.all('wlan0')
    
    for cell in wifi_list:
        print(f"SSID: {cell.ssid}, BSSID: {cell.address}")

scan_wifi()
