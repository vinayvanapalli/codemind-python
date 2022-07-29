def prime(x):
    if x==1:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    else:
        return True
n=int(input())
c=0
m=[]
for i in range(1,n+1):
    if n%i==0:
        m.append(i)
for i in m:
    if prime(i)==False:
        c=c+1
print(c)        
        