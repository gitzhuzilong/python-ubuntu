def get_zers(bts,dict_trx,list_ci):
	str_zers=''
	trxs = 0
	for i in range(len(list_ci)):
		trx = dict_trx[list_ci[i]]['trx']
		for j in range(0,int(trx)):
			trxs += 1
			str1 = "ZERS:BTS=%s,TRX=%s:U;\n" % (bts+i,trxs)
			str_zers += str1
	return str_zers