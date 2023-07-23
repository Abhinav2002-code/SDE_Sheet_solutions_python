from sys import stdin
import sys
sys.setrecursionlimit(10**7) 

def f(i, j, str1, str2, dp):
    if i < 0:
        return j + 1
    if j < 0:
        return i + 1
    
    if dp[i][j] != -1:
        return dp[i][j]
    
    if str1[i] == str2[j]:
        dp[i][j] = 0 + f(i-1, j-1, str1, str2, dp)
        return dp[i][j]
    
    insert = 1 + f(i, j-1, str1, str2, dp)
    delete = 1 + f(i-1, j, str1, str2, dp)
    replace = 1 + f(i-1, j-1, str1, str2, dp)

    dp[i][j] = min(insert, delete, replace)

    return dp[i][j]


def editDistance(str1, str2) :
    n = len(str1)
    m = len(str2)

    dp = [[-1 for _ in range(m)] for _ in range(n)]
 
    # Your code goes here
    return f(n-1, m-1, str1, str2, dp)


























    
#taking inpit using fast I/O
def takeInput() :
    str1=input()
    str2=input()

    return str1, str2


#main
str1, str2  = takeInput()
print(editDistance(str1, str2))
