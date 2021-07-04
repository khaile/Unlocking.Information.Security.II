from scapy.all import packet, rdpcap
from scapy.layers.http import *


def show_username_password():
    packet.bind_layers(TCP, HTTP, dport=8000)
    packet.bind_layers(TCP, HTTP, sport=8000)
    packets = rdpcap(recording_path)

    for pkt in packets:
        if pkt.haslayer(HTTPRequest) and pkt.haslayer(Raw):
            print(str(pkt[Raw]))


recording_path = 'tcpdump.pcap'
show_username_password()
