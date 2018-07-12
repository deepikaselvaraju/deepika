s=[]
sum=0
n=int(input())
m=int(input())
for i in range(0,n):
   s.append(input())
for i in range(0,m):
   sum=sum+int(s[i])
print (sum)
