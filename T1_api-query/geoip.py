#!/usr/bin/env python3

import requests, ipaddress

ips = ['192.30.255.113','8.8.8.8','1.1.1.1', '192.168.0.1'] # first create a list of IPs

def get_zip(ipaddress):
    url = "https://freegeoip.app/json/"+ipaddress #create the URL for API call
    response = requests.request("GET", url)
    json = response.json() #parse response to json object
    if json['latitude'] == 0: #private IP's report 0 for latitude, we exclude them here
        return False
    return json['latitude']


if __name__ == "__main__":
    iplist = []
    for ip in ips: #iterate through list
        if not get_zip(ip): #if IP is private (lat = 0), then skip to next
            continue
        print(ip+' : '+str(get_zip(ip))) #print requirement
        iplist.append(ip) #add to list of IPs for step 5
    
    while True: #while loop to verify user input
        userIP = input('Enter an IP Address: ')
        try:
            ipaddress.ip_address(userIP) # python3 introduces ipaddress module, which is better than socket in this case
            break
        except:
            print('That isnt an IP address. Try again.')

iplist.append(userIP) #add user IP to list once validated
print(userIP+' : '+str(get_zip(userIP)))
print('The following IP addresses were given location data: '+str(iplist))