#!/bin/env python3

from googlesearch import search
from colorama import Fore, Style
import argparse
import requests
import time
import threading

def arparse():
    banner='''
    ____             __   _______           __
   / __ \____  _____/ /__/ ____(_)___  ____/ /
  / / / / __ \/ ___/ //_/ /_  / / __ \/ __  / 
 / /_/ / /_/ / /  / ,< / __/ / / / / / /_/ /  
/_____/\____/_/  /_/|_/_/   /_/_/ /_/\__,_/   
                                 v.0.1            
                                 Author :Jhonson
                                 
    '''

    print(Fore.GREEN + Style.BRIGHT +banner+ Style.RESET_ALL)

arparse()

def main(title,num,save): 
   
 try :  
   launch=input(str(Fore.RED +Style.BRIGHT +'Filter results YES OR NO : '+ Style.RESET_ALL)).upper()
   print('\n')

   if launch == 'YES':
        filter = search(title, num_results=int(num), lang="en")
        for i in filter:
            if args.title in i:
                print(Fore.BLUE +Style.BRIGHT +i+ Style.RESET_ALL)
                time.sleep(2) 
                if args.save:
                   with open(save, 'a') as file :
                     
                      file.write(i+'\n')
        objet=f'File save {args.save}'
        print(Fore.YELLOW +Style.BRIGHT +f'{objet}'+ Style.RESET_ALL)
                  
   else : 
        filter = search(title, num_results=int(args.num), lang="en")
        for i in filter:
           
            print(Fore.BLUE +Style.BRIGHT +i+ Style.RESET_ALL)
            time.sleep(2) 
            if args.save:
               with open(args.save, 'a') as file :
                   file.write(i+'\n') 
 
   
   if  launch != 'YES':
        objet=f'File save {args.save}'        
        print(Fore.YELLOW +Style.BRIGHT +f'{objet}'+ Style.RESET_ALL)

 except requests.exceptions.ReadTimeout:

   print(Fore.GREEN +Style.BRIGHT +'Resend Problem Connexion'+ Style.RESET_ALL)
 except requests.exceptions.ConnectionError:
   print(Fore.GREEN +Style.BRIGHT +'No data connexion'+ Style.RESET_ALL)
 
 
  
if __name__=='__main__':

       parser = argparse.ArgumentParser(description="DorkFind")
       parser.add_argument("-title", "--title", dest="title", help="title of your dork", required=True)
       parser.add_argument("-num", "--num", dest="num", help="nomber of results", required=True)     
       parser.add_argument("-save", "--save", dest="save", help="save", required=False)  
       args = parser.parse_args()

       thread = threading.Thread(target=main, args=(args.title,args.num, args.save)) 
       thread.start()
       thread.join(timeout=2)
