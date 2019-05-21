import zipfile
import os
import glob2
letters=[]
if not os.path.exists ("47"):
    os.makedirs("47")
zip_ref=zipfile.ZipFile("46 letters.zip","r")
zip_ref.extractall("47/")
zip_ref.close()
python_files = glob2.glob("C:/Users/KUMAR GAURAV/Desktop/100 question exercise/46/letters/**/*.txt")
for file in list(python_files):
    f=open(file,"r")
    file_content=f.read()
    for value in list("python"):
        if file_content==value:
            letters.append[value]
print(letters)
