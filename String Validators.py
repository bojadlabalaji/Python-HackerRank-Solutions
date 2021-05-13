s = input()
    print(any(ele.isalnum() for ele in s))
    print(any(ele.isalpha() for ele in s))
    print(any(ele.isdigit() for ele in s))
    print(any(ele.islower() for ele in s))
    print(any(ele.isupper() for ele in s))
    
