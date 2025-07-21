def expose_superman(trust, n):
    if n == 1: #only one person must be Superman
        return 1
    
    trust_counts = [0] * (n + 1)
    trusted_by_counts = [0] * (n + 1)
    

    for chunk in trust:
        for i in range(len(chunk)):
            
    return -1

n = 2
trust = [[1, 2]]
print(expose_superman(trust, n))

n = 3
trust = [[1, 3], [2, 3]]
print(expose_superman(trust, n))

n = 3
trust = [[1, 3], [2, 3], [3, 1]]
print(expose_superman(trust, n))
