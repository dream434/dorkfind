from googlesearch import search
import sys

import pyfiglet as pyg  

res= pyg.figlet_format("Ys jhonson le wana !!!!!" , font="banner3")
print(res)

try :
	a = sys.argv[1]
	query = a
	for dork in search(query, tld="co.in", num=100, stop=100, pause=2):
		  		class couleur:
		  			OK = '\033[92m' #GREEN
		  		print(couleur.OK+dork)

except :
	
	print('python dorker.py target')
