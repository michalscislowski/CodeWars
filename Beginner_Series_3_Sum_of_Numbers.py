def get_sum(a,b):
    sum = 0
    if a>b:
        for x in range(b, a+1):
            sum = sum+x
    elif a<b:
        for x in range(a, b+1):
            sum = sum+x
    elif a==b:
        sum = a
    return sum
    #good luck!
