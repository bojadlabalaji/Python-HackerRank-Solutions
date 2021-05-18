from collections import Counter
n=int(input())
size=[]
size=list(map(int,input().split()))
cn=int(input())
cl=[]
for x in range(cn):
    ele=list(map(int,input().split()))
    cl.append(ele)
sizedic=Counter(size)
earn=0
for x in range(cn):
    if cl[x][0] in sizedic and sizedic[cl[x][0]]>0:
        sizedic[cl[x][0]]-=1
        earn+=cl[x][1]
print(earn)
