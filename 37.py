#Question: Create a function that takes a text file as input and returns the number of words contained in the text file. Please take into consideration that some words can be separated by a comma with no space. For example "Hi,it's me." would need to be counted as three words. For your convenience, you can use the text file in the attachment.


def counter(file):
    file=open("words2.txt","r")
    content=file.read()
    newcontents=content.replace(',',' ')
    string_list=newcontents.split()
    return len(string_list)


print(counter("words2.txt"))
