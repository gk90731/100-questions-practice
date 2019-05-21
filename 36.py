#Question: Please download the words1.txt file from the attachment and then create a Python function that takes a text file as input and returns the number of words contained in the text file.

#Expected output:10
def counter(file):
    #content = file.read()
    strng_list = content.split()
    return len(strng_list)



file = open("words1.txt","r")
content = file.read()
print(counter(file))
