import os
def create_folder(direct):
	try:
		if not os.path.exists(direct):
			os.makedirs(direct)
		else:
			print("exist folder")
	except OSError:
		print("Error: creating direcotry "+ direct)

#pop="test"
#data=open('./'+pop+'/filename1',"w")
#dirc=os.getcwd()+'\\test'
#for f in os.listdir(dirc):
#	print(f)
#create_folder('./test')
