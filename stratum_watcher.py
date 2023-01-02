import socket
import json
import hashlib
import binascii
from pprint import pprint
import time
import random
from time import sleep
import threading

host    = 'hk.kaspa.herominers.com'
port    = 1206
KAS_ADDR= ''

print("INFO - stratum watcher ...ok")

# Connect to mining pool
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host,port))

# Set up socket for mining software
s    = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 5555))
s.listen(4)

# Accept connection from mining software
miner, addr = s.accept()
RE_CONNECT = False
RE_CONNECT_TIME = 600

# Function to receive messages from mining software and send to mining pool
def get_from_miner():
    while True:
        global sock, KAS_ADDR
        try:
            miner_msg = miner.recv(1024)
            if miner_msg:
                messages = miner_msg.split(b'\n')
                for message in messages[:-1]:
                    result = b''
                    result += message +b'\n'
                    print(f"<== {result}")
                    sock.sendall(result)

                    response_dict = json.loads(result)
                    if response_dict['method'] == 'mining.authorize':
                        KAS_ADDR = response_dict['params'][0]
                        print(f"KAS_ADDR : {KAS_ADDR}")

        except socket.error:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((host,port))

# Function to receive messages from mining pool and send to mining software
def get_from_pool():
    while True:
        global sock, s, miner, addr, RE_CONNECT
        try:
            if RE_CONNECT != True:
                pool_msg = sock.recv(1024)
                if pool_msg:
                    print(f"==> {pool_msg}")
                    miner.sendall(pool_msg)
            else:
                print(f"Wait reconnect...")
                sleep(1)
        except socket.error:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((host,port))

# Function to reconnect the pool
def reconnect_pool():
    while True:
        global sock, s, miner, addr, RE_CONNECT, RE_CONNECT_TIME, KAS_ADDR
        sleep(RE_CONNECT_TIME)
        RE_CONNECT = True
        sleep(1)
        method = 'mining.authorize'
        password = 'x'
        params = [KAS_ADDR, password]
        request = {'id': 1, 'method': method, 'params': params}
        request_json = json.dumps(request) + '\n'

        print("<== ", end="")
        print(request_json.encode())
        sock.sendall(request_json.encode())
        RE_CONNECT = False

# Start threads to handle communication with mining software and mining pool
t1 = threading.Thread(target = get_from_miner)
t2 = threading.Thread(target = get_from_pool)
t3 = threading.Thread(target = reconnect_pool)
t1.start()
t2.start()
t3.start()

# Keepalive loop to maintain connection with mining pool
while True:
        sleep(30)
