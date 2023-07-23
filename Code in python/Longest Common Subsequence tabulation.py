
from sys import stdin

# def f(s, t, ind1, ind2, dp):
# 	if ind1 < 0 or ind2 < 0 :
# 		return 0
	
# 	if dp[ind1][ind2] != -1:
# 		return dp[ind1][ind2]

# 	if s[ind1] == t[ind2]:
# 		dp[ind1][ind2] = 1 + f(s, t, ind1 - 1, ind2 - 1, dp)
# 		return dp[ind1][ind2]

# 	dp[ind1][ind2] = max(f(s, t, ind1 - 1, ind2, dp), f(s, t, ind1, ind2 - 1, dp))
# 	return dp[ind1][ind2]



def lcs(s, t) :
	dp = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]

	for i in range(len(s) + 1):
		dp[i][0] = 0
	for j in range(len(t) + 1):
		dp[0][j] = 0
	for i in range(1, len(s) + 1):
		for j in range(1, len(t) + 1):
			if s[i-1] == t[j-1]:
				dp[i][j] = 1 + dp[i-1][j-1]
			else:
				dp[i][j] = max(dp[i-1][j], dp[i][j-1])

	return dp[len(s)][len(t)]
	#Your code goes here






























    


#main
s = str(stdin.readline().rstrip())
t = str(stdin.readline().rstrip())

print(lcs(s, t))