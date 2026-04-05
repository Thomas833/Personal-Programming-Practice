def officialSolution(nums: list[int], val: int) -> int:
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    
    print(nums)
    return k

print(officialSolution([0,1,2,0,4,2], 2))



def mySolution(nums: list[int], val: int) -> int:
    j = len(nums) - 1
    i = 0

    while i <= j:
        if nums[i] != val and nums[j] != val:
            i += 1
        elif nums[i] != val and nums[j] == val:
            i += 1
            j -= 1
        elif nums[i] == val and nums[j] != val:
            temp = nums[j]
            nums[j] = nums[i]
            nums[i] = temp
            i += 1
            j -= 1
        else:
            j -= 1
    #print(nums)
    return i