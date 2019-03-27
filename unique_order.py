unique_in_order2 = lambda l: [z for i, z in enumerate(l) if i == 0 or l[i - 1] != z]

def unique_in_order(iterable):
    return [iterable[i-1] for i in range(1, len(iterable)+1) if i == len(iterable) or iterable[i-1]!=iterable[i]] 

print(unique_in_order2('AAAABBBCCDAABBB'))