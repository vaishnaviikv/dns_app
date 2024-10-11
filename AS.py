import requests
import socket
import json

localPort   = 53533

soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
soc.bind(('', localPort))

while True:

    message, clientaddress = soc.recvfrom(2048)
    message = message.decode()
    message = json.loads(message)

    if len(message) == 2:
        with open("out.json", "r") as outfile:
            dictionary = json.load(outfile)
        DNS_response = dictionary[message["NAME"]]
        DNS_object = json.dumps(DNS_response)
        soc.sendto(DNS_object.encode(),clientaddress)

    else:
        data = {message["NAME"]: message}
        AS_object = json.dumps(data)
        
        with open("out.json", "w") as outfile:
            outfile.write(AS_object)
        soc.sendto(str(201).encode(), clientaddress)
