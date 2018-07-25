
def get_zefc(cell_id,str_cell_id,etme_id,bs_start_ip):

	str_zefc = '''ZEFC:%s,M,R,2:DNAME=OM%s,:::::ETMEID=%s,VLANID=48,BCUIP=%s,SMCUP=26,BMIP=%s,SMMP=26,:::;'''%(cell_id,str_cell_id,etme_id,bs_start_ip,bs_start_ip,)

	str_zefc += '\n'
	return str_zefc
