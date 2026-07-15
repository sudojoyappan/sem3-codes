
def subArraySum(l,k):
    res=0
    currentSum=0
    prefixSums={0:1}
    for n in l:
        currentSum+=n
        diff=currentSum-k
        res+=prefixSums.get(diff,0)
        prefixSums[currentSum]=1+prefixSums.get(currentSum,0)