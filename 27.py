#Question:

#Create a function that calculates acceleration given initial velocity v1, final velocity v2, start time t1, and end time t2. The formula for acceleration is:


#To test your solution, call the function by inputting values 0, 10, 0, 20 for v1, v2, t1, and t2 respectively, and you should get the expected output.

#Expected output:0.5

def accn_cal(v1,v2,t1,t2):
    calculated_aacn=(v2-v1)/(t2-t1)
    return calculated_aacn

print(accn_cal(0,10,0,20)) 
