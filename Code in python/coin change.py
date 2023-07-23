from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def f(denominations, value, ind, target , dp):
    if ind == 0:
        return (target % denominations[0] == 0)

    if dp[ind][target] != -1:
        return dp[ind][target]
    
    notTake = 0 + f(denominations, value, ind-1, target, dp)
    take = 0
    if denominations[ind] <= target:
        take = f(denominations, value, ind, target - denominations[ind], dp)
    
    dp[ind][target] = take + notTake
    
    return dp[ind][target]

def countWaysToMakeChange(denominations, value) :
    dp = [[-1 for _ in range(value + 1)] for _ in range(len(denominations ) + 1)]
    
	
    return f(denominations, value, len(denominations) - 1 , value, dp)































#taking inpit using fast I/O
def takeInput() :
    numDenominations = int(input())

    denominations = list(map(int, stdin.readline().strip().split(" ")))

    value = int(input())
    return denominations, numDenominations, value


#main
denominations, numDenomination, value = takeInput()
print((countWaysToMakeChange(denominations, value)))