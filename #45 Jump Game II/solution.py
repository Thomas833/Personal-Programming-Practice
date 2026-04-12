def jump(nums: list[int]) -> int:
    totalJumps = farthest = end = 0

    for i in range(len(nums)):
        farthest = max(nums[i] + i, farthest)
        if i == end:
            totalJumps += 1
            end = farthest
    return totalJumps

print(jump([20,9,10,0,0,0,0,0,0]))
# [3,9,10,0,0,0,0,0,0]
# [3,4,1,0,2,0,0]
# [2,3,4,0,1,2,0,2,2,3]
