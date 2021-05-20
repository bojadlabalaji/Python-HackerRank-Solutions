n,m=map(int,input().split())
i=list(map(int,input().split()))
A=set(map(int,input().split()))
B=set(map(int,input().split()))
h=0
for x in i:
    if x in A:
        h+=1
for x in i:
    if x in B:
        h-=1
print(h)
