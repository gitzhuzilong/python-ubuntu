
#new_bts
def new_bts(cell_id):
	#室外站
	if cell_id <= 200:
		str_cell_id = str(cell_id)+'1'
	elif cell_id<=400 and cell_id>200:
		str_cell_id = str(cell_id%200)+'4'
	elif cell_id>400 and cell_id<=500:
		str_cell_id = str(cell_id%400)+'7'
	#室内站
	elif cell_id>500 and cell_id<=600:
		str_cell_id = str(cell_id-300)+'1'
	elif cell_id>600 and cell_id<=700:
		str_cell_id = str(cell_id-400)+'4'
	elif cell_id>700 and cell_id<=800:
		str_cell_id = str(cell_id-500)+'7'		

if __name__ == '__main__':
	print (new_bts(638))