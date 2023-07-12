from typing import *

# def f(day, last, points, dp):
#     if day == 0:
#         maxi = 0
#         for i in range(3):
#             if i != last:
#                 maxi = max(maxi, points[0][i])
#         return maxi
    
#     if dp[day][last] != -1:
#         return  dp[day][last]

#     maxi = 0
#     for i in range(3):
#         if i != last:
#             point = points[day][i] + f(day-1, i, points,dp)
#             maxi = max(maxi,point)
#     dp[day][last] = maxi    
#     return dp[day][last]


def ninjaTraining(n: int, points: List[List[int]]) -> int:
    dp = [[-1] * 4 for _ in range(n)]

    dp[0][0] = max(points[0][1],points[0][2])
    dp[0][1] = max(points[0][0],points[0][2])
    dp[0][2] = max(points[0][0],points[0][1])
    dp[0][3] = max(points[0][1],max(points[0][2], points[0][0]))

    for day in range(1,n):
        for last in range(4):
            dp[day][last] = 0
            for task in range(3):
                if task != last:
                    point = points[day][task] + dp[day-1][task]
                    dp[day][last] = max(dp[day][last],point)


    return dp[n-1][3]
    pass
