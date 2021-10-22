#!/usr/bin/env python

import socket
import numpy as np
import json
import time
import random

HOST = '192.168.54.14' # Standard loopback interface address
PORT = 65431 # Port to listen on (use ports > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024).decode('utf-8')
            print('Received from socket server : ', data)




