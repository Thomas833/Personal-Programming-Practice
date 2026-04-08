def mySolution(prices: list[int]) -> int:
    profit = 0
    i = 0
    j = i + 1
    while j < len(prices):
        if prices[i] < prices[j]:
            profit = prices[j] - prices[i] if prices[j] - prices[i] > profit else profit
        else:
            i=j
        j+=1 
    return profit

print(mySolution([1,2,4,2,5,7,2,4,9,0,9]))
# [1,7,2,9,6]
# [3,10,1,7,2]
# [8,7,6,5,1]