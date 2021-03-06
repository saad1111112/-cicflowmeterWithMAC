#!/usr/bin/env python
#Edit by Saad Alabdulsalam

from .packet_direction import PacketDirection


def get_packet_flow_key(packet, direction) -> tuple:
	if "TCP" in packet:
		protocol = "TCP"
	elif "UDP" in packet:
        	protocol = "UDP"
	else:
		raise Exception("Only TCP protocols are supported.")

	if direction == PacketDirection.FORWARD:
		dest_ip = packet["IP"].dst
		src_ip = packet["IP"].src
		src_port = packet[protocol].sport
		dest_port = packet[protocol].dport
		src_ether= packet["Ether"].src
	else:
		dest_ip = packet["IP"].src
		src_ip = packet["IP"].dst
		src_port = packet[protocol].dport
		dest_port = packet[protocol].sport
		src_ether= packet["Ether"].src
	return dest_ip, src_ip, src_port, dest_port, src_ether
