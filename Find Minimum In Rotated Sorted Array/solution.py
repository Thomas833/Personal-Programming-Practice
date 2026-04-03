# modify binary search algorithm to search for minimum, not specific value
def modifiedBinarySearch(nums) -> int:
    low = 0
    high = len(nums) - 1
    
    # use < because we want to exit loop when low == high, meaning one left, which is minimum
    # condition to look for is if mid element is greater than last element in array
    while low < high:
        mid = (low + high) // 2
        
        if nums[mid] > nums[high]:
            low = mid + 1 # exclude mid since mid has been determined to not be valid
        else: # if nums[mid] <= nums[high]
            high = mid # include mid (not mid - 1) because midpoint could be minimum value
    
    # at this point, low == high and have found minimum element
    return nums[low]


     

print(modifiedBinarySearch([4,5,6,7,8,1,2]))