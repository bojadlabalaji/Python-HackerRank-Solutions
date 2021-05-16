# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
string,k=input().split()
for i in sorted(permutations(string,int(k))):
    print(''.join(i))
