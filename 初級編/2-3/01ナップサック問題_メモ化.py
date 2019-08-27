N = int(input())
wv = [list(map(int, input().split())) for _ in range(N)]
W = int(input())

#DP

dp = [[-1 for _ in range(W+1)] for _ in range(N+1)]

def rec(i, j):
	if dp[i][j] != -1:
		return dp[i][j]

	if i == N:
		dp[i][j] = 0
		return dp[i][j]
	elif j < wv[i][0]:
		dp[i][j] = rec(i+1, j)
		return dp[i][j]
	else:
		dp[i][j] = max(rec(i+1, j), rec(i+1, j-wv[i][0]) + wv[i][1])
		return dp[i][j]

rec(0,W)
print(dp[0][W])
