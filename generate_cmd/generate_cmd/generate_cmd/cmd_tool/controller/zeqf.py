
def get_zeqf(bts,dict_para,dict_trx,list_ci):
	str_zeqf=''
	for j in range(len(list_ci)):
		# trx = dict_trx[list_ci[j]]['trx']
		# for i in range(0,int(trx)):
		# str_2 = "ZEQF:BTS=%s:PLMN=0&&7,DBC=Y,DR=%s,DRM=%s,:;\n" % (bts+j,dict_para[list_ci[j]]['dr'],dict_para[list_ci[j]]['drm'])
		str_2 = "ZEQF:BTS=%s:PLMN=0&&7,DBC=%s,DR=%s,DRM=%s,:;"%(bts+j,dict_para[list_ci[j]]['dbc'],dict_para[list_ci[j]]['dr'],dict_para[list_ci[j]]['drm'],)
		str_zeqf += str_2+'\n'
	return str_zeqf
