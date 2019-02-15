n11 = int(input())  
s11 = 0  
t3 = n11 
  
while t3 > 0:  
   digi = t3 % 10  
   s11 =s11 + digi ** 3  
   t3 //= 10  
  
if n11 == s11:  
   print("yes")  
else:  
   print("no")
