import math
from scapy.layers.inet import *
from scapy.all import *
ipLayer=IP(src='192.168.1.33',dst='192.168.1.1')
# send(ipLayer)
print ("ipLayer: ", ipLayer)
