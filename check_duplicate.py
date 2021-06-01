# -*- coding: utf-8 -*-
"""
Spyder Editor

This script just checks if there are duplicate file in the home and home2 directories
"""

import os



#%%

home = "/Users/ecoadmin/Documents/_centric_diatoms_centrales"
home2 = "/Users/ecoadmin/Documents/SPC_centrales/1583215271/0000000000_static_html/images/00000"


files1 = os.listdir(home)
files2 = os.listdir(home2)
n=0

for file in files2:
    #if 'file' from files2 is also in files1 (different than 0)
    if not files1.count(file)==0:
	#count it. n will have the amount of files duplicated
        n=n+1
	#print the name of the file
        print(file)
"""
#%% test 
fails1 = ['hello','world','pandas']
fails2 = ['hola','world','numpy','pandas']
m=0

for fail in fails2:
    if not fails1.count(fail)==0:
        m=m+1
        print(fail)   
""" 