'''
Problem:
	Find the sum of the first N numbers.

Objective function:
	f(i) is the sum of the first i elements.

Recurrence relation:
	f(n) = f(n-1) + n

'''

def nSum(n):
    dp = [0] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + i
    return dp[n]

n = 5
print(nSum(n))