#Question: Create a script that generates a text file with all letters of English alphabet inside it, one letter per line.




import string
f=open("41.txt","w+")
a=string.ascii_uppercase
b=(string.ascii_lowercase)
for values in a:
    f.write(values)
    f.write("\n")
for values in b:
    f.write(values)
    f.write("\n")
f.close()



"""Answer: 

import string

with open("letters.txt", "w") as file:
    for letter in string.ascii_lowercase:
        file.write(letter + "\n")"""
