import textwrap

def wrap(string, max_width):
    return textwrap.fill(string,max_width)
    #The fill() method is similar to the wrap method, but it does not generate a list. It generates a string. It adds the new line character after exceeding the specified width.

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
