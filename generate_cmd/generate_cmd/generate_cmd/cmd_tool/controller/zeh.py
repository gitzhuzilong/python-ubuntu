

def get_zehg(bts,dict_para,dict_trx,list_ci):
	str_zehg=''
	for j in range(len(list_ci)):
		# trx = dict_trx[list_ci[j]]['trx']
		# for i in range(0,int(trx)):
			str1 = "ZEHG:BTS=%s:EIC=%s,EIH=%s,ESD=%s,EFA=%s,EFP=%s,EFH=%s,MIH=%s,:;\n" % (bts+j,dict_para[list_ci[j]]['eic'],dict_para[list_ci[j]]['eih'],dict_para[list_ci[j]]['esd'],dict_para[list_ci[j]]['efa'],dict_para[list_ci[j]]['efp'],dict_para[list_ci[j]]['efh'],dict_para[list_ci[j]]['mih'])
			str_zehg += str1
	return str_zehg

def get_zeha(bts,dict_para,dict_trx,list_ci):
	str_zeha=''
	for j in range(len(list_ci)):
		# trx = dict_trx[list_ci[j]]['trx']
		# for i in range(0,int(trx)):
		str2 = "ZEHA:BTS=%s:LDW=%s,LUW=%s,QDW=%s,QUW=%s,:;\n" % (bts+j,dict_para[list_ci[j]]['ldw'],dict_para[list_ci[j]]['luw'],dict_para[list_ci[j]]['qdw'],dict_para[list_ci[j]]['quw'])
		str_zeha += str2
	return str_zeha

def get_zehs(bts,dict_para,dict_trx,list_ci):
	str_zehs=''
	for j in range(len(list_ci)):
		# trx = dict_trx[list_ci[j]]['trx']
		# for i in range(0,int(trx)):
		str3 = "ZEHS:BTS=%s:LDR=%s,LDP=%s,LDN=%s,LUR=%s,LUP=%s,LUN=%s,:;\n" % (bts+j,dict_para[list_ci[j]]['ldr'],dict_para[list_ci[j]]['ldp'],dict_para[list_ci[j]]['ldn'],dict_para[list_ci[j]]['lur'],dict_para[list_ci[j]]['lup'],dict_para[list_ci[j]]['lun'])
		str_zehs += str3
	return str_zehs

def get_zehq(bts,dict_para,dict_trx,list_ci):
	str_zehq=''
	for j in range(len(list_ci)):
		# trx = dict_trx[list_ci[j]]['trx']
		# for i in range(0,int(trx)):
		str4 = "ZEHQ:BTS=%s:QDP=%s,QDN=%s,QUP=%s,QUN=%s,:;\n" % (bts+j,dict_para[list_ci[j]]['qdp'],dict_para[list_ci[j]]['qdn'],dict_para[list_ci[j]]['qup'],dict_para[list_ci[j]]['qun'])
		str_zehq += str4
	return str_zehq

def get_zehi(bts,dict_para,dict_trx,list_ci):
	str_zehi=''
	for j in range(len(list_ci)):
		# trx = dict_trx[list_ci[j]]['trx']
		# for i in range(0,int(trx)):
		str5 = "ZEHI:BTS=%s:IDR=%s,IUR=%s,:;\n" % (bts+j,dict_para[list_ci[j]]['idr'],dict_para[list_ci[j]]['iur'])
		str_zehi += str5
	return str_zehi

def get_zehn(bts,dict_para,dict_trx,list_ci):
	str_zehn=''
	for j in range(len(list_ci)):
		# trx = dict_trx[list_ci[j]]['trx']
		# for i in range(0,int(trx)):
		str6 = "ZEHN:BTS=%s:AWS=%s,::;\n" % (bts+j,dict_para[list_ci[j]]['aws'])
		str_zehn += str6
	return str_zehn