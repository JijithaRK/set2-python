j=int(input())
c1=0
for i in range(1,j+1):
    if(j%i==0):
        c1=c1+1
if(c1==2):
    print("yes")
else:
    print("no")
