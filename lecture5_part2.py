'''
Problem:
	Climbing Stairs
	You are climbing a stair case. It takes n steps to reach to the top.
	Each time you can either climb 1 or 2 steps.
	In how many distinct ways can you climb to the top?

Framework for Solving DP Problems:
	1. Define the objective function
		f(i) is the number of distinct ways to reach the i-th stair by making 1 to k stairs.
	2. Identify base cases
		f(0) = 1
		f(1) = 1
	3. Write down a recurrence relation for the optimized objective function
		f(n) = f(n-1) + f(n-2) + ... + f(n - k)
	4. What's the order of execution?
		bottom-up
	5. Where to look for the answer?
		f(n)
'''
def climbingStaors(n, k):
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
		# dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - k]  # k = 2
        for j in range(k):
            if i - j < 0:
                continue
            dp[i] += dp[i - j]
    return dp[n]
print(climbingStaors(2, 3))