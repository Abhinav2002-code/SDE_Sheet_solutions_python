
def f(values, weights, n, w, ind):
    if ind == 0:
        if weights[0] <= w:
            return values[0]
        else:
            return 0
    
    notTake = 0 + f(values, weights, n, w, ind-1)
    take = -1e9
    if weights[ind] <= w:
        take = values[ind] + f(values, weights, n, w - weights[ind], ind-1)
    
    return max(take, notTake)

def maxProfit(values, weights, n, w):

    return f(values, weights, n, w, n-1)

    # Write your code here
    pass
