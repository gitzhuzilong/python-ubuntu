
def get_zeqg(bts,dict_para,dict_trx,list_ci):
	str_zeqg=''
	for j in range(len(list_ci)):
		# trx = dict_trx[list_ci[j]]['trx']
		# for i in range(0,int(trx)):
		s1 = "ZEQG:BTS=%s:HYS=%s,RXP=%s,RLT=%s,PRC=%s,:;\n" % (bts+j,dict_para[list_ci[j]]['hys'],dict_para[list_ci[j]]['rxp'],dict_para[list_ci[j]]['rlt'],dict_para[list_ci[j]]['prc'])
		str_zeqg += s1
	return str_zeqg

def get_zeqj(bts,dict_para,dict_trx,list_ci):
	str_zeqj=''
	for j in range(len(list_ci)):
		# trx = dict_trx[list_ci[j]]['trx']
		# for i in range(0,int(trx)):
		s2 = "ZEQJ:BTS=%s:AG=%s,MFR=%s,PER=%s,:;\n" % (bts+j,dict_para[list_ci[j]]['ag'],dict_para[list_ci[j]]['mfr'],dict_para[list_ci[j]]['per'])
		str_zeqj += s2
	return str_zeqj

def get_zeqm(bts,dict_para,dict_trx,list_ci):
	str_zeqm=''
	for j in range(len(list_ci)):
		# trx = dict_trx[list_ci[j]]['trx']
		# for i in range(0,int(trx)):
		if dict_para[list_ci[j]]['timeh']==5:
			timeh=0
		elif dict_para[list_ci[j]]['timeh']==10:
			timeh=1
		elif dict_para[list_ci[j]]['timeh']==15:
			timeh=2
		elif dict_para[list_ci[j]]['timeh']==20:
			timeh=3
		s3 = "ZEQM:BTS=%s:DTX=%s,RET=%s,NY1=%s,SLO=%s,FRL=%s,FRU=%s,NECI=%s,MBR=%s,ESI=%s,AUT=%s,ALT=%s,AML=%s,TGT=%s,EBENA=%s,::PI=%s,REO=%s,TEO=%s,:QSRI=%s,QSRP=%s,FDD=%s,FDM=%s,:::::GPRIO=%s,WPRIO=%s,PSTHR=%s,LPTHR=%s,TIMEH=%s,UTTR=%s,UQRL=%s,:::;\n" % (bts+j,dict_para[list_ci[j]]['dtx'],dict_para[list_ci[j]]['ret'],dict_para[list_ci[j]]['ny1'],dict_para[list_ci[j]]['slo'],dict_para[list_ci[j]]['frl'],dict_para[list_ci[j]]['fru'],dict_para[list_ci[j]]['neci'],dict_para[list_ci[j]]['mbr'],dict_para[list_ci[j]]['esi'],dict_para[list_ci[j]]['aut'],dict_para[list_ci[j]]['alt'],dict_para[list_ci[j]]['aml'],dict_para[list_ci[j]]['tgt'],dict_para[list_ci[j]]['ebena'],dict_para[list_ci[j]]['pi'],dict_para[list_ci[j]]['reo'],dict_para[list_ci[j]]['teo'],dict_para[list_ci[j]]['qsri'],dict_para[list_ci[j]]['qsrp'],dict_para[list_ci[j]]['fdd'],dict_para[list_ci[j]]['fdm'],dict_para[list_ci[j]]['gperio'],dict_para[list_ci[j]]['wprio'],dict_para[list_ci[j]]['psthr'],dict_para[list_ci[j]]['lpthr'],timeh,dict_para[list_ci[j]]['uttr'],dict_para[list_ci[j]]['uqrl'])
		str_zeqm += s3
	return str_zeqm

def get_zeqb(bts,dict_para,dict_trx,list_ci):
	str_zeqb=''
	for j in range(len(list_ci)):
		# trx = dict_trx[list_ci[j]]['trx']
		# for i in range(0,int(trx)):
		s4 = "ZEQB:BTS=%s:MEAS=%s,:;\n" % (bts+j,dict_para[list_ci[j]]['meas'])
		str_zeqb += s4
	return str_zeqb

def get_zeqe(bts,dict_para,dict_trx,list_ci):
	str_zeqe=''
	hop = ''
	for j in range(len(list_ci)):
		# trx = dict_trx[list_ci[j]]['trx']
		# for i in range(0,int(trx)):
		hop = dict_para[list_ci[j]]['hop']
			# print ("****hop**",hop)
		if hop == "N":
			str1 = "ZEQE:BTS=%s:HOP=%s;\n" % (bts+j,dict_para[list_ci[j]]['hop'])
			str_zeqe += str1
		elif hop == "BB":
			str2 = "ZEQE:BTS=%s:HOP=%s,HSN1=%s,HSN2=%s,:;\n" % (bts+j,dict_para[list_ci[j]]['hop'],int(dict_para[list_ci[j]]['hsn1']),int(dict_para[list_ci[j]]['hsn2']))
			str_zeqe += str2
	return str_zeqe

def get_zeqv(bts,dict_para,dict_trx,list_ci):
	str_zeqv=''
	for j in range(len(list_ci)):
		# trx = dict_trx[list_ci[j]]['trx']
		# for i in range(0,int(trx)):
		s6 = "ZEQV:BTS=%s:GENA=%s,CDED=%s,CDEF=%s,BFG=%s,MCA=%s,MCU=%s,DLPC=%s,:::::;\n" % (bts+j,dict_para[list_ci[j]]['gena'],dict_para[list_ci[j]]['cded'],dict_para[list_ci[j]]['cdef'],dict_para[list_ci[j]]['bfg'],dict_para[list_ci[j]]['mca'],dict_para[list_ci[j]]['mcu'],dict_para[list_ci[j]]['dlpc'])
		str_zeqv += s6
	str_zeqv += '\n'
	for j in range(len(list_ci)):
		# trx = dict_trx[list_ci[j]]['trx']
		# for i in range(0,int(trx)):
		ss6 = "ZEQV:SEG=%s:GENA=%s;\n" % (bts+j,dict_para[list_ci[j]]['gena'])
		str_zeqv += ss6
	
	return str_zeqv

def get_zeqy(bts,dict_para,dict_trx,list_ci):
	str_zeqy=''
	for j in range(len(list_ci)):
		# trx = dict_trx[list_ci[j]]['trx']
		# for i in range(0,int(trx)):
		s7 = "ZEQY:BTS=%s:ARLT=%s,AHRLT=%s;\n" % (bts+j,dict_para[list_ci[j]]['arlt'],dict_para[list_ci[j]]['ahrlt'])
		str_zeqy += s7
	return str_zeqy