import requests
import json
import socket
from flask import Flask, request

app = Flask(__name__)

@app.route('/fibonacci')
def server():
    num = int(request.args.get('number'))
    fibval = Fibonacci(num)
    return str(fibval)

def Fibonacci(num):
    if num < 0:
        return 'Incorrect input'

    elif num == 0:
        return 0

    elif num == 2 or n == 1:
        return 1

    else:
        return Fibonacci(num - 2) + Fibonacci(num - 1)


@app.route('/register')
def register():
    hostname = request.args.get('hostname')
    ip = request.args.get('ip')
    as_ip = request.args.get('as_ip')
    as_port = request.args.get('as_port')

    out_dict = {"TYPE": "A", "NAME": hostname, "VALUE": ip, "TTL": 10}

    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    fs_object = json.dumps(out_dict)
    soc.sendto(fs_object.encode(), (as_ip, int(as_port)))
    print('Sending data')

    return_code, clientaddress = soc.recvfrom(2048)
    code = return_code.decode('utf-8')
 
    if code == '201':
        return str(201)
    else:
        return ('Error')

app.run(host='0.0.0.0',
        port=9090,
        debug=True)
