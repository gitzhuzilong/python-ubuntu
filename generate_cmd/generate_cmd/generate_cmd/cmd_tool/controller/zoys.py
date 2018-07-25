
def get_zoys(str_cell_id,N):

	#n = 10
	str1 = "ZOYS:IUA:OM%s:ACT:;"%(str_cell_id)
	str_zoys = str1 + '\n'
	dict_16 = {0:'1',1:'2',2:'3',3:'4',4:'5',5:'6',6:'7',7:'8',8:'9',9:'A',10:'B',11:'C',12:'D',13:'E',14:'F',15:'G',16:'H',
	17:'I',18:'J',19:'K',20:'L',21:'M',22:'N',23:'O',24:'P',25:'Q',26:'R',27:'S',28:'T',29:'U'}
	for j in range(N):
		str2 = "ZOYS:IUA:T%s%s:ACT:;"%(str_cell_id,dict_16[j])
		str_zoys += str2 + '\n'

	return str_zoys