import zipfile
import os
import glob2
import re
if not os.path.exists("46"):
    os.makedirs("46")
zip_ref = zipfile.ZipFile("46 letters.zip", "r")
zip_ref.extractall("46/")
zip_ref.close()
python_files = glob2.glob("C:/Users/KUMAR GAURAV/Desktop/100 question exercise/46/letters/**/*.txt")
for values in list(python_files):
    a=open("letter2.txt","a+")
    b=open(values,"r")
    c=b.read()
    a.write(c)
    a.close()
big_file = open("letter2.txt","r")
content = big_file.read()
ncontent = re.sub('\W+','',content)
list_content = list(ncontent)
print(list_content)
