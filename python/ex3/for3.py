x=int(input("Enter x:\n"))
counter=0
umnj=1
for i in range(1,x) :
    counter=counter+1
    umnj=umnj*i
    break
print (counter)
print (x*umnj)
