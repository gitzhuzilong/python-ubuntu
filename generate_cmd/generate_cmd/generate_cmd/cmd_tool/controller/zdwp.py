
def get_zdwp(str_cell_id,N,bcxu):
	str1 = "ZDWP:OM%s:BCXU,%s:62,1:OM%s,0:;"%(str_cell_id,bcxu,str_cell_id)
	str_zdwp = str1 + '\n'

	dict_16 = {0:'1',1:'2',2:'3',3:'4',4:'5',5:'6',6:'7',7:'8',8:'9',9:'A',10:'B',11:'C',12:'D',13:'E',14:'F',15:'G',16:'H',
	17:'I',18:'J',19:'K',20:'L',21:'M',22:'N',23:'O',24:'P',25:'Q',26:'R',27:'S',28:'T',29:'U'}
	for j in range(N):
		str2 = "ZDWP:T%s%s:BCXU,%s:0,%s:T%s%s,0:;"%(str_cell_id,dict_16[j],bcxu,str(j+1),str_cell_id,dict_16[j])
		str_zdwp += str2 + '\n'

	return str_zdwp
	