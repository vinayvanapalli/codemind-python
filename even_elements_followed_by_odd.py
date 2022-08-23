n=int(input())
l=list(map(int,input().split()))
s=[]
a=[]
for i in l:
    if i%2==0:
        s.append(i)
    
    else:
        a.append(i)
s.extend(a)
for i in s:
    print(i,end=' ')