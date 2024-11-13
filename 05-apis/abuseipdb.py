
# -*- coding: utf-8 -*-
"""

Open the JSON log file titled "network_traffic.json". Write a program that will:
    1. Pull all of the IP addresses from the log
    2. Send each IP address to the abuseIPDB API
    3. Determine whether or not the IP has been flagged for abuse (abuseConfidenceScore > 0)
    4. Add all flagged IPs to a dictionary with the IP being the key, and the abuseConfidenceScore
       being the value
    5. Print the dictionary. 

"""

import requests
from pprint import pprint
import json

payload = {"ipAddress": "241.163.94.187"}
url = "https://api.abuseipdb.com/api/v2/check/"
headers = {
  'Key': '2da6b3b57dbffdf98880bad799338b21328eb9077ce8aeb1d7d2fc32e87c7cea21fa5af9caea1d7c'
}

ip_dictionary = {}
ip_list = []

with open("network_traffic.json") as file:
    data = json.load(file)

for entry in data:
    ip_list.append(entry["source_ip"])
  
print(ip_list)
    


# response = requests.request("GET", url, headers=headers, params=payload)
# print(response.text)