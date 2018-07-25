# -*- coding: utf-8 -*-
# import pandas as pd 

def get():
	# df = pd.read_excel(r"E:\Task_python\06tool\Nokia.xlsx",sheetname='规划')
	# print (df.dtypes)
	# print (df['逻辑站名'])
	
	#这条语句可以将来用于前端传入逻辑站名
	# print (df[df['小区名'].str.contains('川沙桥')])
	# print(df[df["逻辑站名"]=="GA-川沙桥"])
	# name = '川沙'
	# txt_name = name+'.txt'
	# print (txt_name)
	# f1 = open(txt_name,'w')
	# str1 = "qweas"
	# f1.write(str1)
	ip = "123.3.4.97"
	ip_list = ip.split('.')
	print (ip_list)
	ip_list[3] = str(int(ip_list[3])+2)
	print (ip_list)
	ip_new = ".".join(ip_list)
	print (ip_new)


	str1 = "ZERC:BTS=28,TRX=1::FREQ=26,TSC=7,:DNAME=T0281:LEV=-80,CH0=MBCCH,CH1=SDCCH,CH2=CCCHE,CH3=TCHD,CH4=TCHD,CH5=TCHD,CH6=TCHD,CH7=TCHD,;"
	str1 = str1.replace("TCHD","*****",4)
	print (str1)




if __name__ == '__main__':
	get()