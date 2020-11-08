a=eval(input("Introduceti a="))
b=eval(input("Introduceti b="))
if a%2==0: 
    for i in range(a+1,b+1,2):
         print(i, end=' ')
if a%2==1: 
    for i in range(a,b+1,2): 
        print(i, end=' ')