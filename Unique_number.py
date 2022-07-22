n=int(input())
l=list(str(n))
a=[]
for i in l:
    if l.count(i)==1:
        a.append(i)
if len(a)==len(l):
    print('Unique Number')
else:
    print('Not Unique Number')