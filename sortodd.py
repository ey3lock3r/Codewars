def sort_array2():
    odds = sorted((x for x in arr if x%2 != 0), reverse=True)
    return [x if x%2==0 else odds.pop() for x in arr]

def sort_array(source_array):
    # Return a sorted array.
    a = sorted([i for i in source_array if i%2!=0])
    func = lambda x: [(yield x) for x in a]
    smpl = func(a)
    return [i if i%2==0 else next(smpl) for i in source_array ]

print(sort_array([5, 3, 2, 8, 1, 4]))