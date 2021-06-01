# SPCdata
#####
Instructions on how to Annotate and how to use SPCConvert 


#####
The python scripts to manage data from the SPC on the Macbook used for tagging are listed below with a comment on what they do.

3folder_copy.py: 
This script checks files in three directories: home1, home2, home3. If the files in home1 DO NOT 
exist in home2 AND home3, the files will be copied from home1 to home3.

check_duplicate.py:
This script checks if there are duplicate files in 2 directories.

copy_Jpegs.py:
Useful to create training or validation sets with just images:
This script takes the .jpegs out of the timestamp-folders and moves them to a chosen destination.
It still needs some tweaks, look at the file's comments.

copy_planki_results.py:
Reads the plankifier results and makes folders (by class) with the images that resulted from the
plankifier. This is efficient to check the results of the plankifier.

copying_fromQ.py:
This script is used to copy raw_data folders from Q. You can edit it to copy 
folders in a sistematic way, for example: Copy one folder from Q to the computer every 24 hours. This
would take a long time if done manually. Look at the code and its comments.
It also makes a .csv file with the dates of the folders you copied

counting_files.py:
the script counting_jpegs.py is clearer, more elegant and better. This was like a draft. 

counting_jpegs.py:
This script counts how many images are in each subfolder in a chosen directory. Great to make
counts of images organized for training, for example. A .csv file is also created with the counts.

datetimescsv.py:
This is a script to check from which dates are your .jpegs in a folder
Does not check for subfolders, yet. It saves the results as a .csv file
It also plots how many images come from which day.

deleting_raw_binary.py:
Deletes the raw_color and binary files created by the SPCConvert. This is useful to make a sample 
for the classifier of only "useful" .jpegs. It need some tweaking still. Look at the comments

non_duplicates_copy.py:
This script copies files from one directory to another, IF they are not in the destination already
Useful to merge training_sets. It is a little bit more simple than 3folder_copy.py

random_copy.py:
Copies a random sample from a dataset. Good for creating random validation sets.

read_planki.py:
Very similar to copy_planki_results.py
Reads the output of the classifier.
It then compares, looks for specific class and plot the amount of images of that class for each date.

tag_reading.py:
Reads Tags from the Macbook and organizes them to later copy to any other destination.
Useful to make validation or training sets from images in different folders but with same tag.

untaring.py:
untars all the folders from the SPC in a directory. Pre-step to SPCConvert.
