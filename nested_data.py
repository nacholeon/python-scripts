#!/usr/bin/env python
"""Working with nested data hands-on exercise / coding challenge."""


import json
import os


# Get the absolute path for the directory where this file is located "here"
here = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(here, "interfaces.json")) as file:
     #TODO: Parse the contents of the JSON file into a variable
     json_text = file.read()
     json_data = json.loads(json_text)
     print (json_data)

for interfaceX in json_data["ietf-interfaces:interfaces"]["interface"]:
    print (interfaceX["name"])
    print(interfaceX["ietf-ip:ipv4"]["address"][0]["ip"])
    print(interfaceX["ietf-ip:ipv4"]["address"][0]["netmask"])



# TODO: Loop through the interfaces in the JSON data and print out each
# interface's name, ip, and netmask.


for devName in json_data["gatewayList"]
    if 'HSRP' in ["gatewayList"]["devName"]


