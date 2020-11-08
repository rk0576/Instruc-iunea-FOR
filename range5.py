n=eval(input("Introduceti n="))
s=0
for x in range(1,n+1): 
    if (x%3==0 and x%5==0):
         s+=x
print(s)