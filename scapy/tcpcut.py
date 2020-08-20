#!/usr/bin/env python
#
#
# tcpcut.py
#
# This is a script that takes a tcpdump file as input and dumps
# the contents to screen in a format similar to rwcut.
# It supports only nine fields and no prompts for the standard
# pedagogical reason.
#
# Input
# tcpcut.py data_file
#
# Output
# Columnar output to stdout
from scapy.all import *
import sys, time
header = '%15s|%15s|%5s|%5s|%5s|%15s|' % ('sip','dip','sport','dport','proto','bytes')
tfn = sys.argv[1]
pcap_data = rdpcap(tfn)
for i in pcap_data:
    sip = i[IP].src
    dip = i[IP].src
    if i[IP].proto == 6:
        sport = i[TCP].sport
        dport = i[TCP].dport
    elif i[IP].proto == 17:
        sport = i[UDP].sport
        dport = i[UDP].dport
    else:
        sport = 0
        dport = 0
    bytes = i[IP].len
    print("%15s|%15s|%5d|%5d|%5d|%15d" % (sip, dip, sport, dport,i[IP].proto, bytes))
