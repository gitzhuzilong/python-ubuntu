
def get_zean(dict_ltep,list_ci,bts):
	str_zean = ''
	for i in range(0,len(list_ci)):
		k1 = str(list_ci[i])+'3'
		k2 = str(list_ci[i])+'4'
		k3 = str(list_ci[i])+'7'
		str1 = ''
		str2 = ''
		str3 = ''
		str_zean = ''
		for i in range(0,len(list_ci)):
			if dict_ltep.__contains__(k1):
				str1 = "ZEAN:BTS=%s::MCC=460,MNC=00,TAC=6277:FREQ=%s,LTEMB=5,LTECP=%s,LTERUT=8,LTERLT=6,LTERXM=-124,::;"%(bts+i,dict_ltep[k1]['freq'],dict_ltep[k1]['ltecp'])
				# str_zean = str1+'\n'
			if dict_ltep.__contains__(k2):
				str2 = "ZEAN:BTS=%s::MCC=460,MNC=00,TAC=6277:FREQ=%s,LTEMB=5,LTECP=%s,LTERUT=8,LTERLT=6,LTERXM=-124,::;"%(bts+i,dict_ltep[k2]['freq'],dict_ltep[k2]['ltecp'])
				# str_zean = str1+'\n'
			if dict_ltep.__contains__(k3):
				str3 = "ZEAN:BTS=%s::MCC=460,MNC=00,TAC=6277:FREQ=%s,LTEMB=5,LTECP=%s,LTERUT=8,LTERLT=6,LTERXM=-124,::;"%(bts+i,dict_ltep[k3]['freq'],dict_ltep[k3]['ltecp'])
			str_z = str1+'\n'+str2+'\n'+str3+'\n'
			str_zean+=str_z
	return str_zean


		