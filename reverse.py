def test(a, b):
    assert a == b, 'Test case failed'

def reverse_words2(str):
    return ' '.join(s[::-1] for s in str.split())

#def reverse_words(text):
#    #test(text)

#    arr = list(text)
#    temp = []
#    result = []#

#    while len(arr)>0:
#        temp.append(arr.pop(0))
#        if temp[-1] == ' ':
#            result = result + temp[-2::-1] + [' ']
#            temp.clear()
#        
#        if len(arr) == 0:
#            result = result + temp[::-1]
#            break
#        
#    return ''.join((result))

test(reverse_words2(''), '')
test(reverse_words2('This is an example!'), 'sihT si na !elpmaxe')
test(reverse_words2('double  spaces'), 'elbuod  secaps')
print(reverse_words2('double  spaces'))