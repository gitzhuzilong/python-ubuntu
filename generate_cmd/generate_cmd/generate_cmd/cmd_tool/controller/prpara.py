
def get_zeua(bts,dict_para,dict_trx,list_ci):
	str_zeua=''
	for j in range(len(list_ci)):
		# trx = dict_trx[list_ci[j]]['trx']
		# for i in range(0,int(trx)):
		str_2 = "ZEUA:BTS=%s:LDW=%s,LUW=%s,QDW=%s,QUW=%s,:;\n" % (bts+j,dict_para[list_ci[j]]['ldw'],dict_para[list_ci[j]]['luw'],dict_para[list_ci[j]]['qdw'],dict_para[list_ci[j]]['quw'])
		str_zeua += str_2
	return str_zeua

def get_zeug(bts,dict_para,dict_trx,list_ci):
	str_zeug=''
	for j in range(len(list_ci)):
		# trx = dict_trx[list_ci[j]]['trx']
		# for i in range(0,int(trx)):
		str_1 = "ZEUG:BTS=%s:INC=%s,INT=%s,PD0=%s,PD1=%s,PD2=%s,:;\n" % (bts+j,dict_para[list_ci[j]]['inc'],dict_para[list_ci[j]]['int1'],dict_para[list_ci[j]]['pd0'],dict_para[list_ci[j]]['pd1'],dict_para[list_ci[j]]['pd2'])
		str_zeug += str_1
	return str_zeug

def get_zeum(bts,dict_para,dict_trx,list_ci):
	str_zeum=''
	for j in range(len(list_ci)):
		# trx = dict_trx[list_ci[j]]['trx']
		# for i in range(0,int(trx)):
		str_3 = "ZEUM:BTS=%s:GAMMA=%s,PCWS=%s,:;\n" % (bts+j,dict_para[list_ci[j]]['gamma'],dict_para[list_ci[j]]['pcws'])
		str_zeum += str_3
	return str_zeum

def get_zeus(bts,dict_para,dict_trx,list_ci):
	str_zeus=''
	for j in range(len(list_ci)):
		# trx = dict_trx[list_ci[j]]['trx']
		# for i in range(0,int(trx)):
			str_2 = "ZEUS:BTS=%s:UDP=%s,UDN=%s,UUR=%s,UUP=%s,UUN=%s,LDR=%s,LUR=%s,;\n" % (bts+j,dict_para[list_ci[j]]['udp'],dict_para[list_ci[j]]['udn'],dict_para[list_ci[j]]['uur1'],dict_para[list_ci[j]]['uup'],dict_para[list_ci[j]]['uun'],dict_para[list_ci[j]]['ldr'],dict_para[list_ci[j]]['lur'])
			str_zeus += str_2
	return str_zeus
	
def get_zeuq(bts,dict_para,dict_trx,list_ci):
	str_zeuq=''
	for j in range(len(list_ci)):
		# trx = dict_trx[list_ci[j]]['trx']
		# for i in range(0,int(trx)):
			# str_2 = "ZEUQ:BTS=%s:UDR=%s,UDP=%s,UDN=%s,UUR=%s,UUP=%s,UUN=%s,UDR=%s,LDP=%s,LDN=%s,LUP=%s,LUN=%s,LQP=%s,LQN=%s,;\n" % (bts+j,dict_para[list_ci[j]]['udr'],dict_para[list_ci[j]]['udp'],dict_para[list_ci[j]]['udn'],dict_para[list_ci[j]]['uur2'],dict_para[list_ci[j]]['uup'],dict_para[list_ci[j]]['uun'],dict_para[list_ci[j]]['udr'],dict_para[list_ci[j]]['ldp'],dict_para[list_ci[j]]['ldn'],dict_para[list_ci[j]]['lup'],dict_para[list_ci[j]]['lun'],dict_para[list_ci[j]]['lqp'],dict_para[list_ci[j]]['lqn'])
			str_2 = "ZEUQ:BTS=%s:UDR=%s,UDP=%s,UDN=%s,UUR=%s,UUP=%s;\n" % (bts+j,dict_para[list_ci[j]]['udr'],dict_para[list_ci[j]]['udp'],dict_para[list_ci[j]]['udn'],dict_para[list_ci[j]]['uur2'],dict_para[list_ci[j]]['uup'])
			str_zeuq += str_2
	str_zeuq += '\n'		
	for j in range(len(list_ci)):
		# trx = dict_trx[list_ci[j]]['trx']
		# for i in range(0,int(trx)):
			# str_2 = "ZEUQ:BTS=%s:UDR=%s,UDP=%s,UDN=%s,UUR=%s,UUP=%s,UUN=%s,UDR=%s,LDP=%s,LDN=%s,LUP=%s,LUN=%s,LQP=%s,LQN=%s,;\n" % (bts+j,dict_para[list_ci[j]]['udr'],dict_para[list_ci[j]]['udp'],dict_para[list_ci[j]]['udn'],dict_para[list_ci[j]]['uur2'],dict_para[list_ci[j]]['uup'],dict_para[list_ci[j]]['uun'],dict_para[list_ci[j]]['udr'],dict_para[list_ci[j]]['ldp'],dict_para[list_ci[j]]['ldn'],dict_para[list_ci[j]]['lup'],dict_para[list_ci[j]]['lun'],dict_para[list_ci[j]]['lqp'],dict_para[list_ci[j]]['lqn'])
			str_2 = "ZEUQ:BTS=%s:UUN=%s,UDR=%s,LDP=%s,LDN=%s,LUP=%s,LUN=%s,LQP=%s,LQN=%s,;\n" % (bts+j,dict_para[list_ci[j]]['uun'],dict_para[list_ci[j]]['udr'],dict_para[list_ci[j]]['ldp'],dict_para[list_ci[j]]['ldn'],dict_para[list_ci[j]]['lup'],dict_para[list_ci[j]]['lun'],dict_para[list_ci[j]]['lqp'],dict_para[list_ci[j]]['lqn'])
			str_zeuq += str_2
	return str_zeuq



