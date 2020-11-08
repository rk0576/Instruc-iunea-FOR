n=eval(input("Introduceti n="))
n2=eval(input("Introduceti n2="))
n3=eval(input("Introduceti n3="))
n4=eval(input("Introduceti n4="))
n5=eval(input("Introduceti n5="))
n6=eval(input("Introduceti n6="))
s1=0
s2=0
s3=0
s4=0
s5=0
s6=0
a=1
for i in range(1,n+1):
    s1+=i 
for i in range(1,n2+1):
    s2+=(i-1)*i 
    a*=i
for i in range(1,n3+1): 
    s3+=a 
for i in range(1,n4+1):
    s4+=i**2 
for i in range(1,n5+1):
    s5+=i/(i+1) 
for i in range(1,n6+1):
    s6+=i*2
print(s1,s2,s3-1,s4,s5,s6)