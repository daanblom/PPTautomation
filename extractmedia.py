import os
import shutil

ppt = input("Pick PPTX file: ")

os.system("mkdir _TMP_")

zipped = ppt + ".zip"

os.system("cp " + ppt + " " + zipped)
os.system("mv " + zipped + " " + "_TMP_")
os.chdir("_TMP_")
os.system("unzip " + zipped)
os.system("rm -f " + zipped)
os.chdir("ppt")
os.system("mv media ../..")
os.chdir("..")
os.chdir("..")
os.system("pwd")



userpath = "media/"
path = userpath
names = os.listdir(path)
folder_name = ['image', 'vector', 'video', 'audio', 'bin']

for x in range(0,5):
	if not os.path.exists(path+folder_name[x]):
		os.makedirs(path+folder_name[x])

for files in names:

	# I M A G E S

	if ".png" in files and not os.path.exists(path+'image/'+files):
		shutil.move(path+files, path+'image/'+files)
	if ".jpg" in files and not os.path.exists(path+'image/'+files):
		shutil.move(path+files, path+'image/'+files)
	if ".JPG" in files and not os.path.exists(path+'image/'+files):
		shutil.move(path+files, path+'image/'+files)
	if ".jpeg" in files and not os.path.exists(path+'image/'+files):
		shutil.move(path+files, path+'image/'+files)
	if ".tiff" in files and not os.path.exists(path+'image/'+files):
		shutil.move(path+files, path+'image/'+files)



	# V E C T O R 

	if ".svg" in files and not os.path.exists(path+'vector/'+files):
			shutil.move(path+files, path+'vector/'+files)
	if ".emf" in files and not os.path.exists(path+'vector/'+files):
			shutil.move(path+files, path+'vector/'+files)

	# V I D E O 

	if ".mp4" in files and not os.path.exists(path+'video/'+files):
			shutil.move(path+files, path+'video/'+files)
	if ".mov" in files and not os.path.exists(path+'vieo/'+files):
			shutil.move(path+files, path+'video/'+files)

	# A U D I O  

	if ".mp3" in files and not os.path.exists(path+'audio/'+files):
			shutil.move(path+files, path+'audio/'+files)
	if ".mov" in files and not os.path.exists(path+'audio/'+files):
			shutil.move(path+files, path+'audio/'+files)

	# R E M O V E

	if ".wdp" in files and not os.path.exists(path+'bin/'+files):
			shutil.move(path+files, path+'bin/'+files)
		


# END
os.system("rm -r -f media/bin")
os.system("rm -r -f _TMP_")

