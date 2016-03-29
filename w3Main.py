temp = input("user input temperature:")
sel = input("F or C:")
print (temp, sel)
if(sel=='F'):
    print (int((temp)-32)*5/9,'C')
elif(sel=='C'):
    print (int(temp)*9/5+32,'F')
else:
    print ("Input Error")