def get_zerc(cell_id,bts,n,dict_trx,list_ci,dict_freq,dict_tsc):
	#ccche配置在dict_tsc这个字典里
	cell_count = len(list_ci)
	trx_num = []
	if (len(str(cell_id)) == 2):
		str_cell_id = '0'+str(cell_id)
	else:
		str_cell_id = str(cell_id)
		
	for x in range(0,cell_count):
		trx_num.append(dict_trx[list_ci[x]]['trx'])
	# print ("---------",trx_num)

	freq = []
	for i in range(0,len(list_ci)):
		freq.append(dict_freq[list_ci[i]]['bcch'])
		for j in range(0,trx_num[i]-1):
			key = "tch%s"%(str(j+1))
			freq.append(dict_freq[list_ci[i]][key])
	# print ("freq",freq)


	trx = []
	for i in range(0,len(list_ci)):
		trx.append(dict_trx[list_ci[i]]['trx'])
	# print ("trx   ::::  ",trx)
	trx_use=[]
	trx_use.append(0)
	for x in range(0,len(list_ci)-1):
		trx_use.append(trx_use[x]+trx[x])
	# print ("trx_use  :::",trx_use)
		
	
	# tsc参数用get_dict1_zeqc  dict_tsc
	tsc = []
	for i in range(0,len(list_ci)):
		for j in range(0,trx_num[i]):
			tsc.append(dict_tsc[list_ci[i]]['tsc'])
	# print ("tsc",tsc)

	sdcch = []
	for i in range(0,len(list_ci)):
		sdcch.append(dict_tsc[list_ci[i]]['sdcch'])
	# print ("ssssssss",sdcch)

	last_sdcch = []
	for i in range(0,cell_count):
		last_sdcch.append(sdcch[i]-1)
	# print ("last_sdcch",last_sdcch)

	con1 = 0
	help_ch = []
	for i in range(0,cell_count):
		for j in range(0,last_sdcch[i]):
			help_ch.append(trx_use[i] + j+1)
	# print ("help_ch  : ",help_ch)


	str_zerc = ''
	con = 0
	dict_16 = {0:'1',1:'2',2:'3',3:'4',4:'5',5:'6',6:'7',7:'8',8:'9',9:'A',10:'B',11:'C',12:'D',13:'E',14:'F',15:'G',16:'H',
	17:'I',18:'J',19:'K',20:'L',21:'M',22:'N',23:'O',24:'P',25:'Q',26:'R',27:'S',28:'T',29:'U'}
	#用于补TCHD
	tchd=[]
	for i in range(0,len(list_ci)):
		tchd.append(dict_tsc[list_ci[i]]['tchd'])
		if tchd[i] == trx[i]:
			tchd[i] = trx[i]
		else:
			tchd[i] = trx[i]-1
	# print ('--------tchd-------::',tchd)
	tchd_b = list(reversed(tchd))
	p1 = []
	for i in range(0,len(list_ci)):
		p1.append(dict_trx[list_ci[i]]['trx'])
	pr = list(reversed(p1))      #pr = [4,3,3]
	p=[]
	s1 = 0
	for j in range(0,len(p1)):
		s1 += pr[j]
		p.append(s1)
	p.insert(0,0)
	# print ("p===",p)
	conk = []
	# p = [0,4,7]    #根据[4,3,3]做一个数组[0,4,7]
	con_list = []
	n1 = 0
	for i in range(0,len(list_ci)):
		for j in range(0,dict_trx[list_ci[i]]['trx']):
			n1 += 1
			con_list.append(n1)

	# print ("con_list:",con_list)
	con_list_b = list(reversed(con_list))
	
	for i in range(0,len(list_ci)):
		#conk+=1
		for j in range(0,tchd_b[i]):
			conk.append(con_list_b[j+p[i]])
	# print ("conk===========%s",conk)

	str_ch0="CH0=SDCCH;"
	for i in range(0,cell_count):
		flag = 0
		if sdcch[i] > trx[i]:
			sdcchs = sdcch[i]-trx[i]
		for x in range(0,trx_num[i]):
			flag += 1
			con += 1
			str1 = '''ZERC:BTS=%s,TRX=%s::FREQ=%s,TSC=%s,:DNAME=T%s%s:LEV=-80;\n'''%(bts+i,str(con),freq[con-1],tsc[con-1],str_cell_id,dict_16[con-1])
			if (con-1)==0 or (con-1)== trx_use[i]:  #这个判断是写CH0=MBCCH,
				str1=str1.replace("LEV=-80","LEV=-80,CH0=MBCCH")
				str1 = str1.replace("CH0=MBCCH;",'CH0=MBCCH,CH1=SDCCH;')
				if dict_tsc[list_ci[i]]['ccche']=='0,2':
					str1 = str1.replace("CH1=SDCCH;",'CH1=SDCCH,CH2=CCCHE;')
					if tchd[i] == trx[i]:
						str1 = str1.replace("CH1=SDCCH,CH2=CCCHE;",'CH1=SDCCH,CH2=CCCHE,CH3=TCHD,CH4=TCHD,CH5=TCHD,CH6=TCHD,CH7=TCHD;')
				if dict_tsc[list_ci[i]]['ccche']=='0,2,4':
					str1 = str1.replace("CH1=SDCCH;",'CH1=SDCCH,CH2=CCCHE,CH4=CCCHE;')
					if tchd[i] == trx[i]:
						str1 = str1.replace("CH1=SDCCH,CH2=CCCHE,CH4=CCCHE;",'CH1=SDCCH,CH2=CCCHE,CH3=TCHD,CH4=CCCHE,CH5=TCHD,CH6=TCHD,CH7=TCHD;')
				if dict_tsc[list_ci[i]]['ccche']=='0,2,4,6':
					str1 = str1.replace("CH1=SDCCH;",'CH1=SDCCH,CH2=CCCHE,CH4=CCCHE,CH6=CCCHE;')
					if tchd[i] == trx[i]:
						str1 = str1.replace("CH1=SDCCH,CH2=CCCHE,CH4=CCCHE,CH6=CCCHE;",'CH1=SDCCH,CH2=CCCHE,CH3=TCHD,CH4=CCCHE,CH5=TCHD,CH6=CCCHE,CH7=TCHD;')
			else:
				# print ("---trx---:",trx_num[i]-1)
				if (con-1) in help_ch: #这个地方可能会有bug   
					str1=str1.replace("LEV=-80;","LEV=-80,CH0=SDCCH,CH1=TCHD,CH2=TCHD,CH3=TCHD,CH4=TCHD,CH5=TCHD,CH6=TCHD,CH7=TCHD;")
			#这里开始补TCHD
			if con in conk:
				if str_ch0 in str1:
					str1 = str1.replace("CH0=SDCCH;",'CH0=SDCCH,CH1=TCHD,CH2=TCHD,CH3=TCHD,CH4=TCHD,CH5=TCHD,CH6=TCHD,CH7=TCHD;')
				else:
					str1 = str1.replace("LEV=-80;",'LEV=-80,CH0=TCHD,CH1=TCHD,CH2=TCHD,CH3=TCHD,CH4=TCHD,CH5=TCHD,CH6=TCHD,CH7=TCHD;')
			str_zerc += str1
		# print("ccche::",dict_tsc[list_ci[i]]['ccche'])
		
	return str_zerc


