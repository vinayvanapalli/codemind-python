n=int(input())
l=list(map(int,input().split()))
s=sum(l)
y= s//n
if y in l:
    print(True)
else:
    print(False)