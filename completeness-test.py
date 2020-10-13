import os
import fnmatch

def Check(list,ext):
	ListExt = []
	LenExt = len(ext)+1
	for x in list:
		if fnmatch.fnmatch(x,'*.'+ ext):
			y = x[:len(x)-LenExt]
			ListExt.append(y)
	return ListExt


print("Script to find missing files from FEA calculation.")

a = 0
while a == 0:
	Ext1 = input("Extension 1: ")
	Ext2 = input("Extension 2: ")
	if Ext1 == Ext2:
		print("You must give two different extensions!")
	else:
		a=1

FileList = os.listdir()
FileListExt1 = Check(FileList,Ext1)
FileListExt2 = Check(FileList,Ext2)


setext1=set(FileListExt1)
setext2=set(FileListExt2)

difference1=setext1.symmetric_difference(setext2)


with open("diff_report","w") as output:
	for item in difference1:
		output.write("%s\n" % item)
