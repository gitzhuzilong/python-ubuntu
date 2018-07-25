from django.shortcuts import render
from django.http import HttpResponse
import codecs
import os
from django.http import StreamingHttpResponse
# Create your views here.
from cmd_tool.controller import zqkc
from cmd_tool.controller import zqkc
from cmd_tool.controller import zoyx
from cmd_tool.controller import zoyp
from cmd_tool.controller import zoys
from cmd_tool.controller import zdwp
from cmd_tool.controller import zefc
from cmd_tool.controller import zeqc
from cmd_tool.controller import zeuczehc
from cmd_tool.controller import zerc
from cmd_tool.controller import zerm
from cmd_tool.controller import zeqv12
from cmd_tool.controller import zean
from cmd_tool.controller import prpara
from cmd_tool.controller import zeqf
from cmd_tool.controller import close_bts
from cmd_tool.controller import zers
from cmd_tool.controller import zeqs
from cmd_tool.controller import zeh
from cmd_tool.controller import dicts
from cmd_tool.controller import dicts2

def index(request):
	return render(request,'index.html')

# def upload_file(request):  

# 	return render(request,'index.html')

def get_para(request):
	if request.method == "POST":    # 请求方法为POST时，进行处理  
		myFile =request.FILES.get("myfile", None)    # 获取上传的文件，如果没有文件，则默认为None  
	if not myFile:  
		return HttpResponse("no files for upload!")  
	# destination = open(os.path.join("/home/ubuntu/python_code/django_project/ningbo_excel",myFile.name),'wb+')
	destination = open(os.path.join("/home/ubuntu/python_code/generatecmd",myFile.name),'wb+')
	for chunk in myFile.chunks():      # 分块写入文件  
		destination.write(chunk)  
	destination.close()

	ci1 = request.POST['ci_1']
	ci2 = request.POST['ci_2']
	ci3 = request.POST['ci_3']
	ci4 = request.POST['ci_4']
	ci5 = request.POST['ci_5']
	ci6 = request.POST['ci_6']
	list_ci1 = []

	list_ci1.append(int(ci1))
	list_ci1.append(int(ci2))
	list_ci1.append(int(ci3))
	list_ci1.append(int(ci4))
	list_ci1.append(int(ci5))
	list_ci1.append(int(ci6))

	list_ci = []
	for i in range(0,6):
		if list_ci1[i] == 0:
			list_ci=list_ci1[0:i]
			break
	# print ("list_ci_new:::",list_ci_new)

	bs_start_ip = request.POST['ip_start']
	subnet_ip = request.POST['subnet_ip']
	etme_ip = request.POST['etme_ip']
	port_zoyp1 = request.POST['port']
	etme_id = request.POST['etme_id']
	# vlanid = request.POST['vlanid']
	
	bcxu = request.POST['bcxu']
	cell_id = request.POST['bcf']
	ip_zoyp = request.POST['zoyp_ip']
	english_name = request.POST['englishname']


	if (len(str(cell_id)) == 2):
		str_cell_id = '0'+str(cell_id)
	else:
		str_cell_id = str(cell_id)
	#new_bts(cell_id)
	#室外站
	if int(cell_id) <= 200:
		str_cell_ids = str(cell_id)+'1'
	elif int(cell_id)<=400 and int(cell_id)>200:
		str_cell_ids = str(cell_id%200)+'4'
	elif int(cell_id)>400 and int(cell_id)<=500:
		str_cell_ids = str(cell_id%400)+'7'
	#室内站
	elif int(cell_id)>500 and int(cell_id)<=600:
		str_cell_ids = str(int(cell_id)-300)+'1'
	elif int(cell_id)>600 and int(cell_id)<=700:
		str_cell_ids = str(int(cell_id)-400)+'4'
	elif int(cell_id)>700 and int(cell_id)<=800:
		str_cell_ids = str(int(cell_id)-500)+'7'
	bts = int(str_cell_ids)

	dict_trx = dicts.dict_ci_zoyx()
	n = 0
	for i in range(len(list_ci)):
		print (dict_trx[list_ci[i]]['trx'])
		n = n + dict_trx[list_ci[i]]['trx']

	port_zoyp = int(port_zoyp1)
	str_zqkc = zqkc.get_zqkc(subnet_ip,etme_ip)
	str_zoyx = zoyx.get_zoyx(str_cell_id,bcxu,n)
	str_zoyp = zoyp.get_zoyp(str_cell_id,n,ip_zoyp,port_zoyp,bs_start_ip)
	str_zoys = zoys.get_zoys(str_cell_id,n)
	str_zdwp = zdwp.get_zdwp(str_cell_id,n,bcxu)
	str_zefc = zefc.get_zefc(cell_id,str_cell_id,etme_id,bs_start_ip)
	cell_count = len(list_ci)  #小区个数
	# english_name = 'CHUANSHAQIAO'  #后面有个N,是诺基亚的意思，可以不要，这里就不要了
	dict_programme = dicts.get_dict1_zeqc(list_ci)
	dict_bts = dicts.get_dict2_zeqc(list_ci)
	cell_id = int(cell_id)
	str_zeqc = zeqc.get_zeqc(cell_id,bts,cell_count,english_name,dict_programme,dict_bts,list_ci)
	
	str_zeuczehc = zeuczehc.get_zeuczehc(bts,cell_count)

	dict_freq = dicts.dict_freq(list_ci)
	dict_tsc = dicts.get_dict1_zeqc(list_ci)
	str_zerc = zerc.get_zerc(cell_id,bts,n,dict_trx,list_ci,dict_freq,dict_tsc)

	str_zerm = zerm.get_zerm(dict_trx,list_ci,cell_id,bts,n)

	dict_trx = dicts2.dict_ci_zers(list_ci)
	str_zers = zers.get_zers(bts,dict_trx,list_ci)

	dict_para = dicts2.dict_ci_zeqg(list_ci)
	str_zeqv1 = zeqv12.get_zeqv1(bts,dict_para,list_ci)
	str_zeqv2 = zeqv12.get_zeqv2(bts,dict_para,list_ci)

	str_zeqs = zeqs.get_zeqs(bts,list_ci)



	# dict_ltep = dicts.dict_ci_ltecp(list_ci)
	# str_zean = zean.get_zean(dict_ltep,list_ci,bts)
	
	#辅助作用
	trx = []
	for i in range(0,len(list_ci)):
		trx.append(dict_trx[list_ci[i]]['trx'])
	# print ("trx   ::::  ",trx)
	trx_use=[]
	trx_use.append(0)
	for x in range(0,len(list_ci)-1):
		trx_use.append(trx_use[x]+trx[x])
	# print ("trx_use  :::",trx_use)

		
	#功控参数
	# bts = int(str_cell_ids)
	dict_para = dicts2.dict_ci_zeu(list_ci)
	str_zeug = prpara.get_zeug(bts,dict_para,dict_trx,list_ci)
	str_zeua = prpara.get_zeua(bts,dict_para,dict_trx,list_ci)
	str_zeum = prpara.get_zeum(bts,dict_para,dict_trx,list_ci)
	str_zeus = prpara.get_zeus(bts,dict_para,dict_trx,list_ci)
	str_zeuq = prpara.get_zeuq(bts,dict_para,dict_trx,list_ci)
	#BTS参数
	dict_para = dicts2.dict_ci_zeqg(list_ci)
	str_zeqf = zeqf.get_zeqf(bts, dict_para,dict_trx, list_ci)
	#可能要关BTS参数
	str_zeqg = close_bts.get_zeqg(bts, dict_para, dict_trx,list_ci)
	str_zeqj = close_bts.get_zeqj(bts, dict_para, dict_trx,list_ci)
	str_zeqm = close_bts.get_zeqm(bts, dict_para, dict_trx,list_ci)
	str_zeqb = close_bts.get_zeqb(bts, dict_para, dict_trx,list_ci)
	str_zeqe = close_bts.get_zeqe(bts, dict_para, dict_trx,list_ci)
	str_zeqv = close_bts.get_zeqv(bts, dict_para, dict_trx,list_ci)
	str_zeqy = close_bts.get_zeqy(bts, dict_para, dict_trx,list_ci)

	#切换参数
	dict_para = dicts2.dict_ci_zehg(list_ci)
	str_zehg = zeh.get_zehg(bts, dict_para,dict_trx, list_ci)
	str_zeha = zeh.get_zeha(bts, dict_para, dict_trx,list_ci)
	str_zehs = zeh.get_zehs(bts, dict_para, dict_trx,list_ci)
	str_zehq = zeh.get_zehq(bts, dict_para, dict_trx,list_ci)
	str_zehi = zeh.get_zehi(bts, dict_para, dict_trx,list_ci)
	str_zehn = zeh.get_zehn(bts, dict_para, dict_trx,list_ci)

	str_cmd = ''
	str_cmd += str_zqkc
	str_cmd += '\n'
	str_cmd += str_zoyx
	str_cmd += '\n'
	str_cmd += str_zoyp
	str_cmd += '\n'
	str_cmd += str_zoys
	str_cmd += '\n'
	str_cmd += str_zdwp
	str_cmd += '\n'
	str_cmd += str_zefc
	str_cmd += '\n'
	str_cmd += str_zeqc
	str_cmd += '\n'
	str_cmd += str_zeuczehc
	str_cmd += '\n'
	str_cmd += str_zerc
	str_cmd += '\n'
	str_cmd += str_zerm
	str_cmd += '\n'

	str_cmd += str_zers
	str_cmd += '\n'
	str_cmd += str_zeqv1
	str_cmd += '\n'
	str_cmd += str_zeqv2
	str_cmd += '\n'	
	# str_cmd += str_zeqs
	str_cmd += '\n'

	str_cmd += '#功控参数'
	str_cmd += '\n'
	str_cmd += str_zeug
	str_cmd += '\n'
	str_cmd += str_zeua
	str_cmd += '\n'
	str_cmd += str_zeum
	str_cmd += '\n'
	str_cmd += str_zeus
	str_cmd += '\n'
	str_cmd += str_zeuq
	str_cmd += '\n'
	str_cmd += '#BTS参数'
	str_cmd += '\n'
	str_cmd += str_zeqf
	str_cmd += '\n'
	str_cmd += '#可能要关BTS'
	str_cmd += '\n'
	str_cmd += str_zeqg
	str_cmd += '\n'
	str_cmd += str_zeqj
	str_cmd += '\n'
	str_cmd += str_zeqm
	str_cmd += '\n'
	str_cmd += str_zeqb
	str_cmd += '\n'
	str_cmd += str_zeqe
	str_cmd += '\n'
	str_cmd += str_zeqv
	str_cmd += '\n'
	str_cmd += str_zeqy
	str_cmd += '\n'
	str_cmd += '#切换参数'
	str_cmd += '\n'
	str_cmd += str_zehg
	str_cmd += '\n'
	str_cmd += str_zeha
	str_cmd += '\n'	
	str_cmd += str_zehs
	str_cmd += '\n'
	str_cmd += str_zehq
	str_cmd += '\n'
	str_cmd += str_zehi
	str_cmd += '\n'
	str_cmd += str_zehn
	str_cmd += '\n'

	str_cmd += str_zeqs
	str_cmd += '\n'


	f1 = codecs.open(r"cmd.txt",'w','utf-8')
	f1.write(str_cmd)
	f1.close()
	
	f = codecs.open("cmd.txt",'rb','utf-8')
	c = f.read()
	f.close()
	response = StreamingHttpResponse(c)
	response['Content-Type'] = 'application/octet-stream'
	response['Content-Disposition'] = 'attachment;filename="cmd.txt"'
	
	return response
	# return HttpResponse("上传成功")
