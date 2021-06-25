#!/usr/bin/env python3

import subprocess as sp
import sys
import os
import random


def parse_mac(m):
        return_mac=""
        i=0
        for char in m:
                if i == 2:
                        i=0
                        return_mac+=":"
                return_mac += str(char)
                i+=1
        return return_mac

def adjust_mac_len(m):
	tmp_mac = m.strip(":")
	inp_len = len(tmp_mac)
	ret_mac = ""
	if len(tmp_mac) > 12:
		ret_mac=tmp_mac[:12]
	else:
		ret_mac = tmp_mac
		i = 0
		app = 12 - len(tmp_mac)
		while i < app:
			ret_mac = ret_mac + str(random.choice('0123456789abcdef'))
			i += 1
	return parse_mac(ret_mac)

def chngmac():
	mac=sys.argv[1].lower()
	sp.run([ "sudo", "ip", "link", "set", "wlan0", "down" ])
	if mac == "":
		sp.run([ "sudo", "macchanger", "-r", "-p", "wlan0" ])
	else:
		if len(mac) != 12 or len(mac) != 17:
			mac = adjust_mac_len(mac)
		elif mac[2] != ":":
			mac=parse_mac(mac)
		sp.run([ "sudo", "macchanger", "-m", mac, "-p", "wlan0" ])
	sp.run([ "sudo", "ip", "link", "set", "wlan0", "up" ])

if __name__ == "__main__":
	chngmac()
