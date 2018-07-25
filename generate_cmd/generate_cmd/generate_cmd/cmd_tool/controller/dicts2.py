# -*- coding: utf-8 -*-
import xlrd

# list_ci = [61505,61506,61507]
fname = (r"/home/ubuntu/python_code/generatecmd/Nokia2.xlsx")
def dict_ci_zeqg(list_ci):
	# fname = (r"E:\Task_python\06tool\Nokia2.xlsx")
	bk = xlrd.open_workbook(fname)
	shxrange = range(bk.nsheets)
	try:
		sh = bk.sheet_by_name("BTS参数")
	except:
		print ("没有这个sheet")
	nrows = sh.nrows
	ncols = sh.ncols
	dict_ci = {}
	dict_para = {}
	for i in range(6,nrows):
		row_data = sh.row_values(i)
		ci = int(row_data[6])
		#print(ci)
		if ci in list_ci:
			# bts = 28
			#zeqg:
			hys = int(row_data[35])
			rxp = int(row_data[38])
			rlt = int(row_data[39])
			prc = int(row_data[46])
			#zeqj:
			ag = int(row_data[56])
			mfr = int(row_data[57])
			per = int(row_data[58])
			#zeqm:
			dtx = int(row_data[61])
			ret = int(row_data[65])
			ny1 = int(row_data[66])
			slo = int(row_data[67])
			frl = int(row_data[74])
			fru = int(row_data[75])
			# afrl = int(row_data[71])
			# afru = int(row_data[72])
			neci= row_data[76]
			mbr= int(row_data[77])
			esi= row_data[78]
			aut= row_data[79]
			alt= row_data[80]
			aml= row_data[81]
			tgt= row_data[82]
			ebena= row_data[83]
			pi= row_data[85]
			reo= int(row_data[87])
			teo= int(row_data[88])
			qsri= int(row_data[90])
			qsrp= int(row_data[91])
			qsrp= int(row_data[91])
			fdd= int(row_data[92])
			fdm= int(row_data[93])
			gperio= int(row_data[94])
			wprio= int(row_data[95])
			psthr= int(row_data[96])
			lpthr= int(row_data[97])
			timeh= int(row_data[99])
			uttr= int(row_data[100])
			uqrl= int(row_data[101])
			#zeqb:
			meas = row_data[109]
			#zeqe:
			hop = row_data[110]
			hsn1 = row_data[111]
			hsn2 = row_data[112]

			#zegvs:
			rac = int(row_data[130])

			#zegv:
			gena = row_data[121]
			egena = row_data[122]
			cded = int(row_data[123])
			cdef = int(row_data[124])
			bfg = int(row_data[131])
			mca = int(row_data[140])
			mcu = int(row_data[141])
			dlpc = row_data[147]
			#zeqy:
			arlt = int(row_data[152])
			ahrlt = int(row_data[153])

			#zeqf:
			dbc = row_data[28]
			dr = row_data[29]
			drm = int(row_data[34])

			dict_para = {}
			for x in range(6,nrows):
				#zeqg:
				dict_para['hys'] = int(hys)
				dict_para['rxp'] = int(rxp)
				dict_para['rlt'] = int(rlt)
				dict_para['prc'] = int(prc)
				#zeqj:
				dict_para['ag'] = int(ag)
				dict_para['mfr'] = int(mfr)
				dict_para['per'] = int(per)
				#zeqm:
				dict_para['dtx'] = int(dtx)
				dict_para['ret'] = int(ret)
				dict_para['ny1'] = int(ny1)
				dict_para['slo'] = int(slo)
				dict_para['frl'] = int(frl)
				dict_para['fru'] = int(fru)
				# dict_para['afrl'] = int(afrl)
				# dict_para['afru'] = int(afru)
				dict_para['neci'] = neci
				dict_para['mbr'] = int(mbr)
				dict_para['esi'] = esi
				dict_para['aut'] = aut
				dict_para['alt'] = alt
				dict_para['aml'] = aml
				dict_para['tgt'] = tgt
				dict_para['ebena'] = ebena
				dict_para['pi'] = pi
				dict_para['reo'] = int(reo)
				dict_para['teo'] = int(teo)
				dict_para['qsri'] = int(qsri)
				dict_para['qsrp'] = int(qsrp)
				dict_para['qsrp'] = int(qsrp)
				dict_para['fdd'] = int(fdd)
				dict_para['fdm'] = int(fdm)
				dict_para['gperio'] = int(gperio)
				dict_para['wprio'] = int(wprio)
				dict_para['psthr'] = int(psthr)
				dict_para['lpthr'] = int(lpthr)
				dict_para['timeh'] = int(timeh)
				dict_para['uttr'] = int(uttr)
				dict_para['uqrl'] = int(uqrl)
				#zeqb:
				dict_para['meas'] = meas
				#zeqe:
				dict_para['hop'] = hop
				dict_para['hsn1'] = hsn1
				dict_para['hsn2'] = hsn2

				#zegvs:
				dict_para['rac'] = int(rac)
				#zeqv:
				dict_para['gena'] = gena
				dict_para['egena'] = egena
				dict_para['cded'] = cded
				dict_para['cdef'] = cdef
				dict_para['bfg'] = bfg
				dict_para['mca'] = mca
				dict_para['mcu'] = mcu
				dict_para['dlpc'] = dlpc
				#zeqy:
				dict_para['arlt'] = arlt
				dict_para['ahrlt'] = ahrlt

				#zeqf:
				dict_para['dbc'] = dbc
				dict_para['dr'] = dr
				dict_para['drm'] = int(drm)



				dict_ci[ci] = dict_para
	#print ("---",dict_ci)
	return dict_ci

def dict_ci_zehg(list_ci):
	# fname = (r"E:\Task_python\06tool\Nokia2.xlsx")
	bk = xlrd.open_workbook(fname)
	shxrange = range(bk.nsheets)
	try:
		sh = bk.sheet_by_name("切换参数")
	except:
		print ("没有这个sheet")
	nrows = sh.nrows
	ncols = sh.ncols
	dict_ci = {}
	dict_para = {}
	for i in range(6,nrows):
		row_data = sh.row_values(i)
		ci = int(row_data[6])
		#print(ci)
		if ci in list_ci:
			#zehg:
			eic = row_data[20]
			eih = row_data[21]
			esd = row_data[24]
			efa = row_data[26]
			efp = row_data[27]
			efh = row_data[28]
			mih = int(row_data[30])
			#zeha:
			ldw = int(row_data[39])
			luw = int(row_data[41])
			qdw = int(row_data[43])
			quw = int(row_data[45])
			#zehs:
			ldr = int(row_data[47])
			ldp = int(row_data[48])
			ldn = int(row_data[49])
			lur = int(row_data[50])
			lup = int(row_data[51])
			lun = int(row_data[52])
			#zehq:
			qdp = int(row_data[68])
			qdn = int(row_data[69])
			qup = int(row_data[71])
			qun = int(row_data[72])
			#zehi:
			idr = int(row_data[73])
			iur = int(row_data[76])
			#zehn:
			aws = int(row_data[79])


			dict_para = {}
			for x in range(6,nrows):
				#zehg:
				dict_para['eic'] = eic
				dict_para['eih'] = eih
				dict_para['esd'] = esd
				dict_para['efa'] = efa
				dict_para['efp'] = efp
				dict_para['efh'] = efh
				dict_para['mih'] = int(mih)
				#zeha:
				dict_para['ldw'] = int(ldw)
				dict_para['luw'] = int(luw)
				dict_para['qdw'] = int(qdw)
				dict_para['quw'] = int(quw)
				#zehS:
				dict_para['ldr'] = int(ldr)
				dict_para['ldp'] = int(ldp)
				dict_para['ldn'] = int(ldn)
				dict_para['lur'] = int(lur)
				dict_para['lup'] = int(lup)
				dict_para['lun'] = int(lun)
				#zehq:
				dict_para['qdp'] = int(qdp)
				dict_para['qdn'] = int(qdn)
				dict_para['qup'] = int(qup)
				dict_para['qun'] = int(qun)
				#zehi:
				dict_para['idr'] = int(idr)
				dict_para['iur'] = int(iur)
				#zehn:
				dict_para['aws'] = int(aws)

				dict_ci[ci] = dict_para

	#print ("---",dict_ci)
	return dict_ci

def dict_ci_zeu(list_ci):
	# fname = (r"E:\Task_python\06tool\Nokia2.xlsx")
	bk = xlrd.open_workbook(fname)
	shxrange = range(bk.nsheets)
	try:
		sh = bk.sheet_by_name("功控参数")
	except:
		print ("没有这个sheet")
	nrows = sh.nrows
	ncols = sh.ncols
	dict_ci = {}
	dict_para = {}
	for i in range(6,nrows):
		row_data = sh.row_values(i)
		ci = int(row_data[6])
		# print(ci)
		if ci in list_ci:
			#zeug:
			inc =int(row_data[24])
			# print("---",inc)
			#参数int与类型int冲突，因此将参数int改为int1
			int1 = int(row_data[26])
			pd0 = int(row_data[27])
			pd1 = int(row_data[28])
			pd2 = int(row_data[29])
			#zeua:
			ldw = int(row_data[40])
			luw = int(row_data[42])
			qdw = int(row_data[44])
			quw = int(row_data[46])
			#zeum:
			gamma = int(row_data[50])
			pcws = int(row_data[52])
			#zeus:
			udp = int(row_data[55])
			udn = int(row_data[56])
			uur1 = int(row_data[57])   #这个地方需要修改uur是第BA列
			uup = int(row_data[58])
			uun = int(row_data[59])
			ldr = int(row_data[60])
			lur = int(row_data[63])
			#zeuq
			udr = int(row_data[66])
			udp = int(row_data[67])
			udn = int(row_data[68])
			uur2 = int(row_data[69])
			uup = int(row_data[70])
			uun = int(row_data[71])
			udr = int(row_data[66])
			ldp = int(row_data[73])
			ldn = int(row_data[74])
			lup = int(row_data[76])
			lun = int(row_data[77])
			lqp = int(row_data[79])
			lqn = int(row_data[80])
			#zeuq
			udp = int(row_data[67])
			udn = int(row_data[68])
			uup = int(row_data[70])
			uun = int(row_data[71])
			udr = int(row_data[66])
			ldp = int(row_data[73])
			ldn = int(row_data[74])
			lup = int(row_data[76])
			lun = int(row_data[77])
			lqp = int(row_data[79])
			lqn = int(row_data[80])


			dict_para = {}
			for x in range(6,nrows):
				#zeug:
				dict_para['inc']= int(inc)
				#参数int与类型int冲突，因此将参数int改为int1
				dict_para['int1']= int(int1)
				dict_para['pd0']= int(pd0)
				dict_para['pd1']= int(pd1)
				dict_para['pd2']= int(pd2)
				#zeua:
				dict_para['ldw']= int(ldw)
				dict_para['luw']= int(luw)
				dict_para['qdw']= int(qdw)
				dict_para['quw']= int(quw)
				#zeum:
				dict_para['gamma']= int(gamma)
				dict_para['pcws']= int(pcws)
				#zeus:
				dict_para['udp']= int(udp)
				dict_para['udn']= int(udn)
				dict_para['uur1']= int(uur1)
				dict_para['uup']= int(uup)
				dict_para['uun']= int(uun)
				dict_para['ldr']= int(ldr)
				dict_para['lur']= int(lur)
				#zeuq
				dict_para['udr']= int(udr)
				dict_para['udp']= int(udp)
				dict_para['udn']= int(udn)
				dict_para['uur2']= int(uur2)
				dict_para['uup']= int(uup)
				dict_para['uun']= int(uun)
				dict_para['udr']= int(udr)
				dict_para['ldp']= int(ldp)
				dict_para['ldn']= int(ldn)
				dict_para['lup']= int(lup)
				dict_para['lun']= int(lun)
				dict_para['lqp']= int(lqp)
				dict_para['lqn']= int(lqn)

				#zeuq
				dict_para['udp']= int(udp)
				dict_para['udn']= int(udn)
				dict_para['uup']= int(uup)
				dict_para['uun']= int(uun)
				dict_para['udr']= int(udr)
				dict_para['ldp']= int(ldp)
				dict_para['ldn']= int(ldn)
				dict_para['lup']= int(lup)
				dict_para['lun']= int(lun)
				dict_para['lqp']= int(lqp)
				dict_para['lqn']= int(lqn)

				dict_ci[ci] = dict_para

	# print ("---",dict_ci)
	return dict_ci

def dict_ci_zers(list_ci):
	# fname = (r"E:\Task_python\06tool\Nokia2.xlsx")
	bk = xlrd.open_workbook(fname)
	shxrange = range(bk.nsheets)
	try:
		sh = bk.sheet_by_name("规划")
	except:
		print ("没有这个sheet")
	nrows = sh.nrows
	ncols = sh.ncols
	dict_ci = {}
	dict_trx = {}
	for i in range(1,nrows):
		row_data = sh.row_values(i)
		ci = int(row_data[6])
		if ci in list_ci:
			trx  = int(row_data[36])
			dict_trx = {}
			for x in range(1,nrows):
				dict_trx['trx'] = int(trx)
		dict_ci[ci] = dict_trx
	# print (dict_ci)
	return dict_ci

