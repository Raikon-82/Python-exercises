x=int (input ("enter x\n"))
a=int (input ("enter a\n"))
y=x/100
z=x/10%10
p=x%10 
sum1=y+z+p
if a==y :
    print (y)
elif a==z :
    print (z)
elif a==p :
    print (p)
else : 
    print (sum1)

