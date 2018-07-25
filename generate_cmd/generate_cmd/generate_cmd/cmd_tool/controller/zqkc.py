# -*- coding: utf-8 -*-

import codecs
#这条指令没有用到Excel
#基站ip起始地址是手动输入的
#etme_ip是手动输入的
def get_zqkc(zqkc_ip,etme_ip): 

	# zqkc_ip = "172.147.255.96"    #这个ip地址是手动输入的
	# etme_ip = "10.0.3.3"          #etme_ip是手动输入的
	
	str1 = ''
	for i in range(1,6):
		string_zdqc = '''ZQKC:ETMA,%s::"%s",26:"%s":PHY:;'''%(i-1,zqkc_ip,etme_ip)
		str1 = str1 + string_zdqc + '\n'
	return str1
