#Complete the script so that it removes duplicate items from list a .
#Expected output: ['1', 2, 1]


a = ["1", 1, "1", 2]

#Answer is:
#print(list(set(a)))
#Answer 2:

#from collections import OrderedDict
#a = ["1", 1, "1", 2]
#a = list(OrderedDict.fromkeys(a))
#print(a)

#Answer 3:

#a = ["1", 1, "1", 2]
#b = []
#for i in a:
#    if i not in b:
#        b.append(i)
