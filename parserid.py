
import os 
import sys
import pyfiglet as pyg  

res= pyg.figlet_format("Ys jhonson le wana !!!!!" , font="banner3")
print(res)


try :
	os.chdir('/sdcard')
	so = sys.argv[1]
	a = open(so, 'r')
	for line in a.readlines():
		if 'id=' in line :
			print(line)
except :
	print('python paserid.py list.txt')		
