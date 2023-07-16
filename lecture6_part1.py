'''
Problem:
	Climbing Stairs (k steps, space optimized, skip red steps)

	You are climbing a stair case. It takes n steps to reach to the top.
	Each time you can climb 1..k steps. You are not allowed to step on red stairs.
	In how many distinct ways can you climb to the top?
'''
def climbingStaors(n, k, stairs):
    dp = [0] * (k)
    dp[0] = 1
    dp[1] = 1
    stairs = [1, 0, 1, 0, 0, 1]
    for i in range(1, n + 1):
        for j in range(k):
            if i - j < 0:
                continue
            if stairs[i - 1]:
                dp[i % k] = 0
            else:   
                dp[i % k]  += dp[(i - j) % k]
    return dp[n % k]
print(climbingStaors(5, 3))