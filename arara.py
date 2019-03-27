def count_arara(n):
    d = {
        0: ' '.join(['adak']*int(n/2)),
        1: ' '.join(['adak']*int(n/2) + ['anane'])
    }
    return d[n%2]

print(count_arara(9))