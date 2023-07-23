from sys import stdin
import sys

def f(price, ind, n, dp):
    rod_length = ind + 1

    if ind == 0:
        return n * price[0]
    
    if dp[ind][n] != -1:
        return dp[ind][n]
    
    notTake = 0 + f(price, ind-1, n, dp)
    take = -1e9
    if rod_length <= n:
        take = price[ind] + f(price, ind, n - rod_length, dp)
    
    dp[ind][n] = max(take,notTake)

    return dp[ind][n]


def cutRod(price, n):
    dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]

    # Write your code here.
    return f(price, n-1, n, dp)
    pass
























# Taking input using fast I/O.
def takeInput():
    n = int(input())

    price = list(map(int, input().strip().split(" ")))

    return price, n


# Main.
t = int(input())
while t:
    price, n = takeInput()
    print(cutRod(price, n))
    t = t-1
