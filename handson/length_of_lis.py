
def length_of_lis(nums) :
    '''
    Given an unsorted array of integers, find the length of the longest increasing subsequence.

    '''
    res= 1
    f = min(nums)
    i = nums.index(f)
    li = [f]
    for e in nums :
        ind = nums.index(e)
        if ind > i  and e > f:
            f = e
            i = ind
            res+=1
            li.append(f)
    print(li)
    return res

nums = [10, 9, 2, 5, 3, 7, 101, 18]
result = length_of_lis(nums)
print(result)