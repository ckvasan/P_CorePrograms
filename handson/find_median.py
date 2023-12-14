#  find the median of a list of numbers without using the sort() function
def merge(left, right):
    i= 0
    j= 0
    nums =[]
    while(i < len(left) and j < len(right)):
        if (left[i] <right[j]) :
            nums.append(left[i])
            i +=1
        else :
            nums.append(right[j])
            j += 1
    nums +=left[i:]
    nums+= right[j:]
    return nums
def divide(nums):
    if (len(nums) == 1):
        return nums
    else :
        l = len(nums)//2

    left = divide(nums[0:l])
    right = divide(nums[l:])
    return merge(left,right)


def find_median(nums):
     #nums =[]
     nums = divide(nums)
     print(f"The sorted nums is {nums}")

     size = len(nums)
     if size%2 == 0 :
         print(size)
         result = nums[int(size/2)] + nums[int(size/2) +1]
         return (result/2)
     else :
         result = nums[size//2]
         return result

numbers = [5, 2, 9, 1, 7, 6, 3, 8, 4,7]
result = find_median(numbers)
print(f"The median of the list {numbers} is and its length is {len(numbers)}: {result}")