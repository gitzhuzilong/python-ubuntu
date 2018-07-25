
def get_zerm(dict_trx,list_ci,cell_id,bts,n):
	str_zerm = ''
	str1 = ''
	con = 0
	gtrx = []
	for i in range(0,len(list_ci)):
		gtrx.append(dict_trx[list_ci[i]]['gtrx'])
	print ('gtrx::',gtrx)
	gtrx_b = list(reversed(gtrx))

	
	con_list = []
	n1 = 0
	for i in range(0,len(list_ci)):
		for j in range(0,dict_trx[list_ci[i]]['trx']):
			n1 += 1
			con_list.append(n1)

	print ("con_list:",con_list)
	con_list_b = list(reversed(con_list))
	print ("con_list_b:-----%s",con_list_b)  #[10,9,8,7,6,5,4,3,2,1]

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
	print ("p===",p)
	conk = []
	# p = [0,4,7]    #根据[4,3,3]做一个数组[0,4,7]

	for i in range(0,len(list_ci)):
		#conk+=1
		for j in range(0,gtrx_b[i]):

			conk.append(con_list_b[j+p[i]])
	print ("conk===========%s",conk)


	for i in range(0,len(list_ci)):
		for j in range(0,dict_trx[list_ci[i]]['trx']):
			con+=1
			if con not in conk:
				str1 = "ZERM:BTS=%s,TRX=%s:GTRX=N:;"%(bts+i,str(con))
				str_zerm += str1+'\n'		
			if con in conk:
				str1 = "ZERM:BTS=%s,TRX=%s:GTRX=Y:;"%(bts+i,str(con))
				str_zerm += str1+'\n'
	return str_zerm



			
		
	