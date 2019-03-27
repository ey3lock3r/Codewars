def tribonacci(signature, n):
    #for _ in range(n-3):
    #    signature.append(sum(signature[len(signature)-3:]))
    #return signature[:n]

    [signature.append(sum(signature[i-3:i])) for i in range(3,n)]
    return signature[0:n]

print(tribonacci([1, 1, 1], 10))