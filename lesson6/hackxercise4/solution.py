from scapy.all import rdpcap
from scapy.layers.inet import IP


def show_source_destination_ip_address():
    packets = rdpcap(recording_path)
    fourth_packet, sixth_packet = packets[3], packets[5]
    print(fourth_packet[IP].src)
    print(sixth_packet[IP].dst)


recording_path = 'tcpdump.pcap'
show_source_destination_ip_address()
