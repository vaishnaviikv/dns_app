import requests
import json
import socket
from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/fibonacci')
def US_server():

    hostname = request.args.get('hostname')
    fs_port = request.args.get('fs_port')
    number = request.args.get('number')
    as_ip = request.args.get('as_ip')
    as_port = request.args.get('as_port')
    print(hostname, fs_port, number, as_ip, as_port)

    if hostname == '' or fs_port == '' or as_ip == '' or as_port == '' or number == '' or not number.isdigit():
        return abort(400, 'bad format')

    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    US_dict = {'hostname': hostname, 'type': "A"}

    soc.sendto(json.dumps(US_dict).encode(), (as_ip, int(as_port)))
    response, clientaddress = soc.recvfrom(2048)
    query_response = response.decode()
    query_response = json.loads(query_response)
    fs_path = 'http://' + query_response["ip"] + ':' + fs_port + '/fibonacci?' + 'number=' + number
    returnval = requests.get(fs_path)
    return returnval.text


app.run(host='0.0.0.0',
        port=8080,
        debug=True)
