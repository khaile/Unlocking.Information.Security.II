from scapy.all import rdpcap
from scapy.layers.inet import TCP


def show_source_destination_ports():
    packets = rdpcap(recording_path)
    fourth_packet, sixth_packet = packets[2], packets[3]
    print(fourth_packet[TCP].dport)
    print(sixth_packet[TCP].sport)


recording_path = 'tcpdump.pcap'
show_source_destination_ports()
