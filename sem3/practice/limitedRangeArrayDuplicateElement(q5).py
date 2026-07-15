#Given a limited range array of size n containing elements between 1 
# and n-1 with one element repeating, find the duplicate number in it without using any extra space.

l=[ 1, 2, 3, 4, 4 ]

def limitedRangeArrayDuplicateElement(l):
    for i in l:
        if l.count(i)>1:
            return i
        
print(limitedRangeArrayDuplicateElement(l))