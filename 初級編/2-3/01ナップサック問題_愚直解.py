N = int(input())
wv = [list(map(int, input().split())) for _ in range(N)]
W = int(input())

#愚直解

def dfs(i,j):
	if i == N:
		res = 0

	elif j < wv[i][0]:
		res = dfs(i+1,j)

	else:
		res = max(dfs(i+1, j), dfs(i+1, j-wv[i][0]) + wv[i][1])

	return res

print(dfs(0,W))
