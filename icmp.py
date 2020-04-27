#!/usr/bin/env python3

import sys
from scapy.all import *

print("pinging the target....")
ip = sys.argv[1]
icmp = IP(dst=ip)/ICMP()
resp = sr1(icmp,timeout=10)

if resp == None:
    print("This host is down")
else:
    print("This host is up")

