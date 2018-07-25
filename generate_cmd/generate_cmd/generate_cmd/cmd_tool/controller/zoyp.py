
def get_zoyp(str_cell_id,N,ip_zoyp,port_zoyp,bs_start_ip):


	str1 = '''ZOYP:IUA:OM%s:"%s",,%s:"%s",26,,,%s:;'''%(str_cell_id,ip_zoyp,port_zoyp,bs_start_ip,port_zoyp)

	str2 = ''
	str_zoyp = str1 + '\n'

	dict_16 = {0:'1',1:'2',2:'3',3:'4',4:'5',5:'6',6:'7',7:'8',8:'9',9:'A',10:'B',11:'C',12:'D',13:'E',14:'F',15:'G',16:'H',
	17:'I',18:'J',19:'K',20:'L',21:'M',22:'N',23:'O',24:'P',25:'Q',26:'R',27:'S',28:'T',29:'U'}
	for j in range(N):
		port_zoyp += 1

		str2 = '''ZOYP:IUA:T%s%s:"%s",,%s:"%s",26,,,%s:;'''%(str_cell_id,str(dict_16[j]),ip_zoyp,port_zoyp,bs_start_ip,port_zoyp)
		str_zoyp += str2 + '\n'
	
	return str_zoyp