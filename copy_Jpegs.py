#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 12:40:04 2020

@author: Tommy

To create training or validation sets with just images:
Take the images out of the timestamp folders and move them to dest


Still needs adjustments if we want to copy images from another folder
that's not 0000000000 and maybe 0000006000. First adjust the untaring 

"""

import os
import shutil

#%%
home = input('In which directory are the images?') #home directory
dest = input('To which directory do you want to move them?')


#%%For big sets divided into subfolders: 
#"""
subfolders = os.listdir(home)
for i in subfolders:
    subfolderpath = os.path.join(home,i)
    if os.path.isdir(subfolderpath): #if i is a folder = directory
        destpath = os.path.join(dest,i) #this path will be created below
        try: 
            os.mkdir(destpath) #subfolder in destination with same name as in home
        except: #if it already exists, continue with code
            pass

        #/Users/ecoadmin/Documents/temp/test3/1527681671/0000000000_static_html/images
        lastdir = os.path.join(subfolderpath,'0000000000_static_html/images')
        for a,b,c in os.walk(lastdir): #a is the path and c is a list of files inside
            for i in c:
                if i.endswith('.jpeg'):
                    dir_img = os.path.join(lastdir,a,i)
                    shutil.copy2(dir_img,destpath)
#"""



#%%For small sets directly to one folder
"""
for a,b,c in os.walk(home): #c is a list of files for each subfolder
    for i in c:
        if i.endswith('.jpeg'):
            dir_img = os.path.join(a,i) #a is the path to the last folder
            #shutil.copy2(dir_img,dest) #change "copy2" to "move" if you want to
"""

