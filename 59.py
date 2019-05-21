'''Question: Please complete the code so that it prints out the expected output.

a = [1, 2, 3]

Expected output:

Item 1 has index 0
Item 2 has index 1
Item 3 has index 2'''
##############################################################################

a = [1, 2, 3]
for item in a:
    print("Item",item,"has index",item-1)

###############################################################################
#alternate:
'''a = [1, 2, 3]
for index, item in enumerate(a):
    print("Item %s has index %s" % (item, index))'''

#enumerate(a)  creates an enumerate object which yields pairs of indexes and items. 
