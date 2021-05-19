if __name__ == '__main__':
    n = int(input().strip())
    b=bin(n)[2:]
    print(max(map(len,b.split('0'))))
