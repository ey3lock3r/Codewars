def likes3(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)

def likes2(names):
    d = {
        0: "no one likes this",
        1: "{} likes this",
        2: "{} and {} like this",
        3: "{}, {} and {} like this",
        4: "{}, {} and {others} others like this"
        }
    length = len(names)
    return d[min(4, length)].format(*names, others = length - 2)

def likes(names):
    l = len(names)
    if l >= 4:
        return ''.join((names[0], ', ', names[1], ' and %s others like this'%(l-2)))
    elif l == 3:
        return ''.join((names[0], ', ', names[1], ' and ', names[2], ' like this'))
    elif l == 2:
        return ''.join(('%s and %s like this'%(names[0], names[1])))
    elif l == 1:
        return '%s likes this'%(names[0])
    else:
        return 'no one likes this'

print(likes3(['Dhinson', 'Peter']))