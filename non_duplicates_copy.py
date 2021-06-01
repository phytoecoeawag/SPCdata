# -*- coding: utf-8 -*-
"""
Spyder Editor

this script copies files from home to dest, IF they are not in dest already
Useful to merge training_sets

look at 3folder_copy.py to copy files only if they are NOT in 2 other folders

"""

import os
import shutil

#%% directories

home = input('home directory?')
dest = input('destination?')

#%% multiple folders with same names

#"""
#tested with hometest2 and desttest2

homedirs = os.listdir(home)
destdirs = os.listdir(dest)

for  i in homedirs: #i is a class, like asterionella
    #if the path points to a folder (avoid hidden) and this directory name..
    #..appears in the destination (i.e. count not 0) -> merge the sets
    if os.path.isdir(os.path.join(home,i)) and (not destdirs.count(i)==0):
        print(i)
        # list the files in the subfolder:
        homedirfiles = os.listdir(os.path.join(home,i)) #list of asterionella
        destdirfiles = os.listdir(os.path.join(dest,i))
        duplicates = [] #make a list of files that were in both directories already
        #to check if numbers match
        print("there are "+str(len(homedirfiles))+" files in "+i+ " in home")
        print("there are "+str(len(destdirfiles))+" files in "+i+ " in destination")
        
        for file in homedirfiles: #if the file in home 
            if destdirfiles.count(file)==0: #is not in dest
                shutil.copy2(os.path.join(home,i,file),os.path.join(dest,i)) #copy it to dest
            else: #if file already exists in dest, save it in duplicates[]
                duplicates.append(file)

        ###check to see if numbers match..
        #print(duplicates)
        print("there are already "+str(len(duplicates))+" "+i+" files from home in destination")
        
        destdirfiles_new = os.listdir(os.path.join(dest,i))
        print("there are now "+str(len(destdirfiles_new))+" "+i+" files in destination")
                
#"""   
  

"""
#%%This is for files directly in home or dest. NO subfolders

homefiles = os.listdir(home)
destfiles = os.listdir(dest)
duplicates = [] #make a list of files that were in both directories already

#to check if numbers match
print("there are "+str(len(homefiles))+" files in home")
print("there are "+str(len(destfiles))+" files in destination")

for file in homefiles: #if the file in home 
    if destfiles.count(file)==0: #is not in dest
        shutil.copy2(os.path.join(home,file),dest) #copy it to dest
    else: #if file already exists in dest, save it in duplicates[]
        duplicates.append(file)

###check to see if numbers match..
#print(duplicates)
print("there are already "+str(len(duplicates))+" files from home in destination")

destfiles_new = os.listdir(dest)
print("there are now "+str(len(destfiles_new))+" files in dest")
"""

