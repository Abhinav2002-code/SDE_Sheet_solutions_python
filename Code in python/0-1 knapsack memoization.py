
def f(values, weights, n, w, ind, dp):
    if ind == 0:
        if weights[0] <= w:
            return values[0]
        else:
            return 0

    if dp[ind][w] != -1:
        return dp[ind][w]
    
    notTake = 0 + f(values, weights, n, w, ind-1, dp)
    take = -1e9
    if weights[ind] <= w:
        take = values[ind] + f(values, weights, n, w - weights[ind], ind-1, dp)
    
    dp[ind][w] = max(take, notTake)
    
    return dp[ind][w]

def maxProfit(values, weights, n, w):
    dp = [[-1 for _ in range(w + 1)] for _ in range(n + 1)]
    
    return f(values, weights, n, w, n-1, dp)

    # Write your code here
    pass
