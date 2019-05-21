'''Question: Create a program that once executed the programs prints Hello  instantly first, then it prints it after 1 second, then after 2, 3, and then the program prints out the message "End of the Loop" and stops.

Expected output:

Hello
Hello
Hello
Hello
End of Loop
'''
###########################################################################

import time
i = 0
while(i<3):

    print("Hello")
    time.sleep(i)
    i = i+1
    if i>3:
        break
print("End of the loop")
