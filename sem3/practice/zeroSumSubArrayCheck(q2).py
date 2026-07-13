def zeroSumArraycheck(l):
    s=set()
    s.add(0)
    sub_array_sum=0
    for i in l:
        sub_array_sum+=i
        if sub_array_sum in s:
            return True
        s.add(sub_array_sum)
    return False
    

# l=[6, -2, -3, 1, 5, -4, 2]
l=[3, 4, -7, 3, 1, 3, 1, -4, -2, -2]

if (zeroSumArraycheck(l)):
    print("has zero sum sub array")
else:
    print("no")