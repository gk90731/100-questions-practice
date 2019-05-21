'''Question: Please create a script that generates 26 text files named a.txt, b.txt, and so on up to z.txt. Each file should contain a letter reflecting its filename. So, a.txt will contain letter a, b.txt will contain letter b and so on.'''



##############################################


import string
import os

if not os.path.exists("45"):
    os.makedirs("45")
a=string.ascii_lowercase
for value in a:

    f=open( "45/" +value+ ".txt","w+")
    f.write(value)
f.close()
