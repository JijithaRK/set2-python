n11,a11,d22=map(int,input().split())
i1=1
ap22=0
while i1<=n11:
    ap22=ap22+a11
    a11=a11+d22
    i1=i1+1
print(ap22)
