# -*- coding: utf-8 -*-
import xlrd

fname = (r"/home/ubuntu/python_code/generatecmd/Nokia2.xlsx")
def dict_ci_zoyx():
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
		trx  = int(row_data[36])
		gtrx = int(row_data[37])
		dict_trx = {}
		# dict_trx['trx'] = trx
		for x in range(1,nrows):
			dict_trx['trx'] = trx
			dict_trx['gtrx'] = gtrx
			# gtrx给zerm使用的   
		dict_ci[ci] = dict_trx
	# print (dict_ci)
	return dict_ci



def dict_ci():
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
	for i in range(1,nrows):
		row_data = sh.row_values(i)
		ci = int(row_data[6])
		trx  = int(row_data[36])
		dict_ci[ci] = trx
	# print (dict_ci)

# list_ci = [61505,61506,61507]

def get_dict1_zeqc(list_ci):    #规划表里的
	# fname = (r"E:\Task_python\06tool\Nokia2.xlsx")
	bk = xlrd.open_workbook(fname)
	shxrange = range(bk.nsheets)
	try:
		sh = bk.sheet_by_name("规划")
	except:
		print ("没有这个sheet")
	nrows = sh.nrows
	ncols = sh.ncols
	dicts = {}
	dict_inside = {}

	for i in range(1,nrows):
		row_data = sh.row_values(i)
		ci = int(row_data[6])
		# trx  = int(row_data[22])
		if ci in list_ci:
			gd = row_data[9]
			new_ci = row_data[42]
			ncc = row_data[45]
			bcc = row_data[46]
			tsc = row_data[43]
			sdcch = row_data[38]
			ccche = row_data[39]
			tchd = row_data[40]
			dict_inside = {}
			# dict_trx['trx'] = trx
			for x in range(1,nrows):
				dict_inside['gd'] = gd
				dict_inside['new_ci'] = int(new_ci)
				dict_inside['ncc'] = int(ncc)
				dict_inside['bcc'] = int(bcc)
				dict_inside['tsc'] = int(tsc)
				dict_inside['sdcch'] = int(sdcch)
				dict_inside['ccche'] = ccche
				dict_inside['tchd'] = int(tchd)
			dicts[ci] = dict_inside
		else:
			continue
	# print (dicts)
	return dicts

def get_dict2_zeqc(list_ci):   #BTS参数表里面的
	# fname = (r"E:\Task_python\06tool\Nokia2.xlsx")
	bk = xlrd.open_workbook(fname)
	shxrange = range(bk.nsheets)
	try:
		sh = bk.sheet_by_name("BTS参数")
	except:
		print ("没有这个sheet")
	nrows = sh.nrows
	ncols = sh.ncols
	dicts_bts = {}
	dict_inside = {}

	# print (type(list_ci[0]))
	for i in range(6,nrows):
		row_data = sh.row_values(i)
		lac_ci = row_data[1]
		ci = int(row_data[6])
		if ci in list_ci:
			mcc = row_data[127]
			mnc = row_data[128]
			lac = row_data[129]
			hop = row_data[110]
			hsn1 = row_data[111]
			hsn2 = row_data[112]
			dict_inside = {}
			for x in range(6,nrows):
				dict_inside['mcc'] = int(mcc)
				dict_inside['mnc'] = int(mnc)
				dict_inside['lac'] = int(lac)
				dict_inside['hop'] = hop
				dict_inside['hsn1'] = hsn1
				dict_inside['hsn2'] = hsn2
			dicts_bts[ci] = dict_inside
	# print(dicts_bts)
	return dicts_bts

def dict_freq(list_ci):
	# fname = (r"E:\Task_python\06tool\Nokia2.xlsx")
	bk = xlrd.open_workbook(fname)
	shxrange = range(bk.nsheets)
	try:
		sh = bk.sheet_by_name("规划")
	except:
		print ("没有这个sheet")
	nrows = sh.nrows
	ncols = sh.ncols
	dict_ch = {}
	for i in range(1,nrows):
		row_data = sh.row_values(i)
		ci = int(row_data[6])
		if ci in list_ci:
			dict_inside= {}
			for x in range(0,len(list_ci)):
				bcch = int(row_data[48])
				for j in range(1,15):
					key = 'tch%s'%(str(j))
					if row_data[48+j] != '':
						dict_inside[key] = int(row_data[48+j])
					else:
						continue
				dict_inside['bcch'] = bcch
			dict_ch[ci] = dict_inside
	# print (dict_ch)
	return dict_ch


# def dict_ci_ltecp(list_ci):
# 	# fname = (r"E:\Task_python\06tool\Nokia2.xlsx")
# 	bk = xlrd.open_workbook(fname)
# 	shxrange = range(bk.nsheets)
# 	try:
# 		sh = bk.sheet_by_name("2G-4G邻区")
# 	except:
# 		print ("没有这个sheet")
# 	nrows = sh.nrows
# 	ncols = sh.ncols
# 	dict_ch = {}
# 	for i in range(6,nrows):
# 		row_data = sh.row_values(i)
# 		ci = int(row_data[6])
# 		if ci in list_ci:
# 			dict_inside= {}
# 			for x in range(6,nrows):
# 				ltecp = row_data[22]
# 				freq = int(row_data[20])		
# 				dict_inside['ltecp'] = int(ltecp)
# 				dict_inside['freq'] = freq
# 			key = str(ci)+str(int(row_data[22]))
# 			dict_ch[key] = dict_inside
# 	# print (dict_ch)
# 	return dict_ch

