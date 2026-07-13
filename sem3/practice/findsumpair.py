def findPair(l,x):
    l.sort()
    min=0
    max=len(l)-1
    for i in range(len(l)):
        sum=l[min]+l[max]
        if sum>x:
            max-=1
        elif sum<x:
            min+=1
        else:
            return l[min],l[max]


l=[8, 7, 2, 5, 3, 1]
x=10
print(findPair(l,x))