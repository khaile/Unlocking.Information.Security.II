from scapy.all import rdpcap


def show_mac_address():
    packets = rdpcap(recording_path)
    third_packet = packets[2]
    print(third_packet.src)


recording_path = 'tcpdump.pcap'
show_mac_address()
