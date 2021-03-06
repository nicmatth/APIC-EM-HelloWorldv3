#!/usr/bin/env python

import http.client
import json
from apic import APIC_IP, APIC_PORT
connection = http.client.HTTPSConnection(APIC_IP, APIC_PORT, timeout = 30)

# Send synchronously

connection.request('GET', '/api/v0/network-device', None, {})
try:
    response = connection.getresponse()

    # modify to load up the response in JSON syntax.
    str_response = response.readall().decode('utf-8')
    content = json.loads(str_response)
    # Success
    #print(('Response status ' + str(response.status)))

#    # Step1 print the result ####
    # uncomment the next line
    #print("Content is:", content)
#    # end of Step1 #####

#    # ####Step2 pretty print the result
    # uncomment the next line
    #print("Content is:", json.dumps(content,indent=4, separators=(',', ': ')))
#    # end of Step2 #####

    print("=======================\n\n")

#    # ####Step3: allow iteration over the results ####
#    # uncomment the following section
    #devices = content["response"]
#
    #print("Platform", "Serial Number", "Name", "Version")
    #for device in devices:
    #    print(device['platformId'], device['serialNumber'], device['hostname'], device['softwareVersion'], device['id'])
#    #end of Step3 ######

except http.client.HTTPException as e:
    # Exception
    print('Exception during request')
