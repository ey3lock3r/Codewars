def anagrams(word, words):
    return [w for w in words if ''.join(sorted(word)) == ''.join(sorted(w))]
    #for w in words:
    #    if ''.join(sorted(w)) == word:
    #        lst.append(w)

    #return lst

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))