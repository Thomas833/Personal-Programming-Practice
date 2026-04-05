def mySolution(nums: list[int]) -> int:
    i = j = 0
    hashmap = {}
    while j < len(nums):
        if nums[j] not in hashmap:
            hashmap[nums[j]] = j
            nums[i] = nums[j]
            i += 1
        j += 1
    print(nums)
    return i

print(mySolution([0,0,0,1,2,2,3,3,4]))

    