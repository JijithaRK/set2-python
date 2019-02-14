j1=int(input())
t1=j1
tr=0
while t1!=0:
    tr=tr*10+t1%10
    t1=t1//10
if j1==tr:
    print("yes")
else:
    print("no")
