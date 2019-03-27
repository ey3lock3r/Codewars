def accum(s):
    return '-'.join([(s[i]*(i+1)).capitalize() for i in range(len(s))])

print(accum("RqaEzty"))