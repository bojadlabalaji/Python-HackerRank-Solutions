def print_formatted(number):
    # your code goes here
    l=len(bin(number)[1:])
    for i in range(1,number+1):
        print(f"%{l-1}d%{l}o%{l}X%{l}s"%(i,i,i,bin(i)[2:]))
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
