
def get_zeqv1(bts,dict_para,list_ci):
	str_zeqv1=''
	for j in range(len(list_ci)):
			str1 = "ZEQV:BTS=%s:GENA=%s,RAC=%s,:;\n" % (bts+j,dict_para[list_ci[j]]['gena'],dict_para[list_ci[j]]['rac'])
			str_zeqv1 += str1
	return str_zeqv1

def get_zeqv2(bts,dict_para,list_ci):
	str_zeqv2=''
	for j in range(len(list_ci)):
			str2 = "ZEQV:BTS=%s:EGENA=%s,:::::;\n" % (bts+j,dict_para[list_ci[j]]['egena'])
			str_zeqv2 += str2
	return str_zeqv2
