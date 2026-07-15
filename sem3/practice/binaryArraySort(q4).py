l=[ 1, 0, 1, 0, 1, 0, 0, 1 ]
def binaryArraySort(l):
    x=0
    for i in range(len(l)):
        if l[i] == 1:
            x=l.pop(i)
            l.append(x)

    return l

print(binaryArraySort(l))