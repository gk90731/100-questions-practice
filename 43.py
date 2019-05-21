'''Question: Create a script that generates a file where all letters of English alphabet are listed two in each line. The inside of the text file would look like:

ab
cd
ef

and so on.'''


import string
f=open("43.txt","w+")
a=string.ascii_lowercase
b=list(a)
for values in b:
    f.write(values + values +"\n")
f.close()
