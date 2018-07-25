import zqkc
import zoyx
import zoyp
import dicts
import zoys
import zdwp
import zefc
import zeqc
import zeuczehc
import zerc
import zerm
import zean
#以川沙桥为例
def test():
	#这里是要输入的参数，分别将输入传递给各个函数
	bs_start_ip = "172.147.255.96"    #基站ip起始地址
	etme_ip = "10.0.3.3"          #etme_ip
	cell_id = 28 #输入放入小区代号   相当于bcf
	bcxu = 5     #输入的BCXU

	#zefc用到的
	etme_id = 2
	vlanid = 48

	list_ci = [61505,61506,61507]
	dict_trx = dicts.dict_ci_zoyx()

	ip_zoyp = '172.147.192.8'
	port_zoyp = 49312



	#new_bts(cell_id)
	#室外站
	if cell_id <= 200:
		return str(cell_id)+'1'
	elif cell_id<=400 and cell_id>200:
		return str(cell_id%200)+'4'
	elif cell_id>400 and cell_id<=500:
		return str(cell_id%400)+'7'
	#室内站
	elif cell_id>500 and cell_id<=600:
		return str(cell_id-300)+'1'
	elif cell_id>600 and cell_id<=700:
		return str(cell_id-400)+'4'
	elif cell_id>700 and cell_id<=800:
		return str(cell_id-500)+'7'
	if (len(str(cell_id)) == 2):
		str_cell_id = '0'+str(cell_id)
	else:
		str_cell_id = str(cell_id)
	
	

	n = 0
	for i in range(len(list_ci)):
		print (dict_trx[list_ci[i]]['trx'])
		n = n + dict_trx[list_ci[i]]['trx']

#########################################################
	#生成指令
	# str_zqkc = zqkc.get_zqkc(bs_start_ip,etme_ip)
	# print (str_zqkc)

	str_zoyx = zoyx.get_zoyx(str_cell_id,bcxu,n)
	print (str_zoyx)

	# str_zoyp = zoyp.get_zoyp(str_cell_id,n,ip_zoyp,port_zoyp,bs_start_ip)
	# print (str_zoyp)

	# str_zoys = zoys.get_zoys(str_cell_id,n)
	# print (str_zoys)

	# str_zdwp = zdwp.get_zdwp(str_cell_id,n,bcxu)
	# print (str_zdwp)


	# str_zefc = zefc.get_zefc(cell_id,str_cell_id,etme_id,vlanid,bs_start_ip)
	# print (str_zefc)


	# cell_count = len(list_ci)  #小区个数
	# english_name = 'CHUANSHAQIAO'  #后面有个N,是诺基亚的意思，可以不要，这里就不要了
	# dict_programme = dicts.get_dict1_zeqc(list_ci)
	# dict_bts = dicts.get_dict2_zeqc(list_ci)
	# str_zeqc = zeqc.get_zeqc(cell_id,cell_count,english_name,dict_programme,dict_bts,list_ci)
	# print (str_zeqc)

	# str_zeuczehc = zeuczehc.get_zeuczehc(cell_id,cell_count)
	# print (str_zeuczehc)

	# dict_freq = dicts.dict_freq(list_ci)
	# dict_tsc = dicts.get_dict1_zeqc(list_ci)
	# str_zerc = zerc.get_zerc(cell_id,n,dict_trx,list_ci,dict_freq,dict_tsc,str_cell_id)
	# print (str_zerc)


	# str_zerm = zerm.get_zerm(dict_trx,list_ci,cell_id,n)
	# print (str_zerm)

	# dict_ltep = dicts.dict_ci_ltecp(list_ci)
	# str_zean = zean.get_zean(dict_ltep,list_ci,cell_id)
	# print (str_zean)

if __name__ == '__main__':
	test()