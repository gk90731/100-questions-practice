#Complete the script so it generates the expected output using my_range  as input data. Please note that the items of the expected list output are all strings.
#Expected output:

#['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']


my_range = range(1, 21)
print(list(map(str,my_range)))



#here we applied string inbuilt function to my_range parameter
#map function applies a built in function or userdefined function to a list
