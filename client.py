#!/usr/bin/python           # This is client.py file

import socket               # Import socket module
from time import sleep
from threading import Timer
from random import random

s = socket.socket()         # Create a socket object
host = socket.gethostname()  # Get local machine name
port = 12345                # Reserve a port for your service.
s.connect((host, port))
s.setblocking(0)
sl, su, sw = 0, 0, 4
data = list("abcdefghijklmnopqrstuvwxyz")  # Data to be sent
rcvd = [False] * len(data)  # Array to store whether frame has been recieved


def timeout(i):  # Timeout function is called when timer expires
    print "Timeout ", i
    s.send(str(i) + "," + data[i])  # Data is resent
    timers[i] = Timer(5, timeout, args=[i], kwargs=dict())
    timers[i].start()  # Timer is restarted

# Initialize timer array
timers = map(lambda t: Timer(3, timeout, args=[
             t], kwargs=dict()), range(0, len(data)))

while sl < len(data):
    try:
        if su < sl + sw and su < len(data):
            print "Sending", su
            # Only 80% of requests are sent. To signify a noisy channel.
            if random() < 0.8:
                s.send(str(su) + "," + data[su])
            else:
                print "Frame ", su, " lost in transmission"
            timers[su].start()
            su += 1
        sleep(0.5)
        ack = s.recv(1024)
        if ack is not None:
            ack = int(ack.split(",")[0])
            print "ACK", ack
            if ack >= sl and ack < su:  # Check validity of ACK
                rcvd[ack] = True
                print "Timer Cancelled", ack
                timers[ack].cancel()  # Cancel Timer
                if ack == sl:
                    while rcvd[sl]:  # Increment SL
                        sl += 1
                        print "SL is incremented to ", sl
    except Exception as e:
        pass
print "Data Transmitted Successfully"
s.close()
