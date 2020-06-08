def fillBackpack(items,capacity):
    n = len(items)
    t = [[0 for m in range (capacity+1)] for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(capacity + 1):
            if items[i-1][1] <= j and items[i-1][0] + t[i-1][j-items[i-1][1]]> t[i-1][j]:
                t[i][j] = items[i-1][0] + t[i-1][j-items[i-1][1]]
            else:
                t[i][j] = t[i-1][j]
    print(t)
    return t[n][capacity]




elementos = [(28,2),(33,5),(5,3),(12,6),(20,1)]
print(fillBackpack(elementos,15))