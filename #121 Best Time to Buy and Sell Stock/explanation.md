Use two pointers, a buy and sell pointer and a profit variable initialized to 0

The buy pointer will always be less then the sell pointer.
In the beginning, the two pointers will start the 0 and 1 indices. (While loop will account for size 1
arrays and still return 0 profit)
You will compare the two values and check if the buy stock is less/greater than the sell stock. 

If the buy stock is greater than the sell stock, this means we lose money and the sell stock should become our buy stock since its smaller than our current buy stock. Move the buy pointer to the sell pointer.

If the buy stock is less than the sell stock, this means you get profit! But, compare it against the profit variable to ensure that the difference is giving you more profit than you have already found. If the difference is less than profit, simply iterate your sell pointer and keep your buy pointer the same since its the smallest number you have found yet. 

Walk along the the array until you reach the end and return the profit