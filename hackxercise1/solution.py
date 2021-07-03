from struct import unpack

packet = b'\x08\x00\x00\x00\xf6\x01\x00\x00\x24\x00\x00\x00\x03\x00\x00\x00\x0c\x00\x00\x00I think, therefore I ' \
         b'am.\xca\xcd\x00\x00'


def show_details():
    sender_id, _receiver_id, _size, _session_id, message_id, message, checksum = unpack('<IIIII24sI', packet)

    unpacked_text = "Sender ID: {0}\nMessage ID: {1}\nMessage: {2}\nChecksum: {3}"
    print(unpacked_text.format(sender_id, message_id, message.decode(), checksum))


show_details()
