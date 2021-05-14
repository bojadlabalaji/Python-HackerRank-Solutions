N,M=map(int,input().split())
s1=".|."
s2="---"
for i in range(N//2) :
    print(s2*(N//2-i)+s1*(2*i+1)+s2*(N//2-i))
i=N//2
print(s2*(i-1)+"-WELCOME-"+s2*(i-1))
for i in range(N//2):
    print(s2*(i+1)+s1*(N-(2*i+2))+s2*(i+1))
