
def get_zeqc(cell_id,bts,cell_count,english_name,dict_programme,dict_bts,list_ci):
	str_zeqc = ''
	hop = 'HOP'
	con=0
	dict_16 = {0:'1',1:'2',2:'3',3:'4',4:'5',5:'6',6:'7',7:'8',8:'9',9:'A',10:'B',11:'C',12:'D',13:'E',14:'F',15:'G',16:'H',
	17:'I',18:'J',19:'K',20:'L',21:'M',22:'N',23:'O',24:'P',25:'Q',26:'R',27:'S',28:'T',29:'U'}
	for i in range(0,cell_count):
		con += 1
		# str_zeqc = "ZEQC:BCF=%s,BTS=%s,NAME=%s%s%s,:CI=%s"%(cell_id,str(cell_id+i),english_name,dict_programme[list_ci[i]]['gd'],str(i+1),programme[list_ci[i]]['new_ci'])
		ci = str(dict_programme[list_ci[i]]['new_ci'])
		gd = dict_programme[list_ci[i]]['gd']
		if gd == 'G':
			band = str(900)
		elif gd == 'D':
			band = str(1800)
		ncc = str(dict_programme[list_ci[i]]['ncc'])
		bcc = str(dict_programme[list_ci[i]]['bcc'])

		mcc = str(dict_bts[list_ci[i]]['mcc'])
		mnc = str(dict_bts[list_ci[i]]['mnc'])
		lac = str(dict_bts[list_ci[i]]['lac'])
		if len(mnc) == 1:
			mnc = '0'+mnc
		hop = str(dict_bts[list_ci[i]]['hop'])
		if hop == 'BB':
			hsn1 = str(int(dict_bts[list_ci[i]]['hsn1']))
			hsn2 = str(int(dict_bts[list_ci[i]]['hsn2']))
			str_last = "HOP=%s,HSN1=%s,HSN2=%s,"%(hop,hsn1,hsn2)
		else:
			str_last = ''
		str_1 = '''ZEQC:BCF=%s,BTS=%s,NAME=%s%s,:CI=%s,BAND=%s:NCC=%s,BCC=%s:MCC=%s,MNC=%s,LAC=%s:%s;'''%(cell_id,bts+i,english_name,dict_16[con-1],ci,band,ncc,bcc,mcc,mnc,lac,str_last)
		str_zeqc += (str_1+'\n')
		if hop in str_zeqc:
			str_zeqc = str_zeqc.replace(':;HOP=BB',':HOP=BB')

	return str_zeqc

