#!/usr/bin/python           # This is server.py file run this first

import socket               # Import socket module
from time import sleep
from random import random
s = socket.socket()         # Create a socket object
host = socket.gethostname()  # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.

data = [None] * 1024
rl, rw = 0, 4
c, addr = s.accept()
print 'Got connection from', addr
while True:
    try:
        i, d = c.recv(4096).split(",")
        i = int(i)
        print "Recieved Frame ", i, " Data : ", d
        if i < rl + rw:
            data[i] = d
            if random() < 0.8 :        #80% Transmission rate. For Noisy Channel
                c.send(str(i) + ',')
                if(i == rl):
                    while data[rl] is not None:
                        rl += 1         #Increment RL
                        print "RL is incremented to ", rl
            else:
                print "ACK ", i, " not sent or lost"
        else:
            print "Discarded ", i
        sleep(0.5)

    except Exception as e:
        c.close()
        break

print "Recieved Data : ",
for d in data:
    if d is None:
        break
    print d,
