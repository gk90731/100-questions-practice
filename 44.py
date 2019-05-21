'''Question: Create a script that generates a file where all letters of English alphabet are listed three in each line. The inside of the text file would look like:

abc
def
ghi

and so on.'''



import string
f=open("44.txt","w+")
a= string.ascii_lowercase + " "
for value1, value2, value3 in zip(a[0::3],a[1::3],a[2::3]):
    f.write(value1 + value2 + value3 +"\n")
f.close()
