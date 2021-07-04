from scapy.all import rdpcap
from scapy.layers.dns import DNSQR, DNSRR


def show_domain_ip_address():
    packets = rdpcap(recording_path)
    for pkt in packets:
        question_type_a = pkt.haslayer(DNSQR) and isinstance(pkt.qd, DNSQR) and pkt.qd.qtype == 1
        answered = pkt.haslayer(DNSRR) and isinstance(pkt.an, DNSRR)
        if question_type_a and answered:
            for i in range(pkt.ancount):
                domain = pkt.an[i].rrname.decode()
                ip = pkt.an[i].rdata
                if isinstance(ip, bytes):
                    ip = ip.decode()
                print("Domain: {0}\nIP: {1}".format(domain, ip))


recording_path = 'tcpdump.pcap'
show_domain_ip_address()
