def jump(nums: list[int]) -> int:
    if (len(nums)) == 1:
        return 0
    jumps = nums[0]
    totalJumps = 0
    i = len(nums) - 2
    while i > 0:
        if i + nums[i] >= len(nums) - 1:
            
        i -= 1
    return totalJumps

print(jump([4,2,0,5,0,0,0]))
# [3,5,6,0,0,0,0,0,0]
# [2,4,1,0,2,4,0]
# [2,3,4,0,1,2,0,2,2,3]
