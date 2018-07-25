# -*- coding: utf-8 -*-

#用到规划表里的数据  指令条数是TRX相加之和
#输入小区代号,BCXU
def get_zoyx(str_cell_id,bcxu,N1):

	#cell_id 如果输入的是两位数前面加0

	str1 = "ZOYX:OM%s:IUA:S:BCXU,%s:AFAST:4:;"%(str_cell_id,bcxu)

	str2 = ''
	str_zoyx = str1 + '\n'

	dict_16 = {0:'1',1:'2',2:'3',3:'4',4:'5',5:'6',6:'7',7:'8',8:'9',9:'A',10:'B',11:'C',12:'D',13:'E',14:'F',15:'G',16:'H',
	17:'I',18:'J',19:'K',20:'L',21:'M',22:'N',23:'O',24:'P',25:'Q',26:'R',27:'S',28:'T',29:'U'}
	for j in range(N1):
		# print (j)
		str2 = 'ZOYX:T%s%s:IUA:S:BCXU,%s:AFAST:64:;'%(str_cell_id,dict_16[j],bcxu)
		str_zoyx += str2 + '\n'
	
	return str_zoyx
