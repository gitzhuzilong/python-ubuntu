# -*- coding:utf-8 -*-
import xlrd
import codecs

def get_zeqs(bts,list_ci):
	str_zeqs=''
	for j in range(len(list_ci)):
			str1 = "ZEQS:BTS=%s:U:;\n" % (bts+j)
			str_zeqs += str1
	return str_zeqs
	print(str_zeqs)