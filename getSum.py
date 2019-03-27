def get_sum(a,b):
    #return sum([i for i in range(min([a, b]), max([a, b])+1)])
    return sum(range(min([a, b]), max([a, b])+1))

a = get_sum(5, 1)
print (a)