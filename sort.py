def sort(l):
    k = []
    for i in l:
        for j in l:
            if j < i:
                k.append(j)
            else:
                k.append(i)
    return k


l = [3, 4, 6, 1, 2]
print(sort(l))

