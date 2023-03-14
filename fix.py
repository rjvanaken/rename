import os
import glob

# Path to the directory where
# the files reside
path = r"C:\Users\rjvan\fix\screenshots"

# Getting the list of files/directories
# in the specified path Filtering the
# list to exclude the directory names
files = list(filter(os.path.isfile, glob.glob(path + "\*")))

# Sorting file list based on the
# creation time of the files
files.sort(key=os.path.getctime)


# Displaying the sorted list
# print(files)

# Python program to rename all file
# names in your directory
import os

os.chdir(r'C:\Users\rjvan\fix\screenshots')
print(os.getcwd())

for count, f in enumerate(os.listdir()):
	f_name, f_ext = os.path.splitext(f)
	f_name = "screenshot(" + str(count) +")"

	new_name = f'{f_name}{f_ext}'
	os.rename(f, new_name)
