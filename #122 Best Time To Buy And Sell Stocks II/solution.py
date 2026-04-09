def mySolution(prices: list[int]) -> int:
    i = 0
    j = 1
    maxProfit = 0 
    while j < len(prices):
        if prices[j] - prices[i] >= 0:
            maxProfit += prices[j] - prices[i]
            i = j
        else:
            i += 1
        j += 1
    return maxProfit


print(mySolution([7,6,4,3,1])) 