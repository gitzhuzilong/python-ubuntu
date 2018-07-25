
def get_zeuczehc(bts,cell_count):
	str_uh = ''
	for i in range(0,cell_count):
		str_u = "ZEHC:BTS=%s,;"%(bts+i)
		str_h = "ZEUC:BTS=%s,;"%(bts+i)
		str_uh += str_u+'\n'+str_h+'\n'
	return str_uh