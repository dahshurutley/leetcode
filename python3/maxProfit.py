def maxProfit(prices): 
# Initialize:
#     max_so_far = INT_MIN
#     max_ending_here = 0

# Loop for each element of the array

#   (a) max_ending_here = max_ending_here + a[i]
#   (b) if(max_so_far < max_ending_here)
#             max_so_far = max_ending_here
#   (c) if(max_ending_here < 0)
#             max_ending_here = 0
# return max_so_far

    # Buy == first index of the list 
    buy = prices[0]

    # init profit as 0
    profit = 0


    for i in range(1, len(prices)):

        # if prices[i] < prices[0], set buy == to the current index 
        if prices[i] < buy:
            buy = prices[i]
        
        # if the current index value - buy > profit, set profit
        elif prices[i] - buy > profit:
            profit = prices[i] - buy
    return profit

print(maxProfit([7, 1, 5, 3, 6, 4]))
# [7,1,5,3,6,4]
