def accum(s):
    return '-'.join([str(s[i]*(i+1)).capitalize() for i in range(len(s))])
    # your code
