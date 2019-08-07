i,j=map(int,input().split())
  
for n in range(i+1,j):  
   sum = 0  
   temp = n  
   while temp > 0:  
       digit = temp % 10  
       sum = sum + digit ** 3  
       temp = temp // 10  
  
   if n == sum:  
       print(n,end=" ")    
