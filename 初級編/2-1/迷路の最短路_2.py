#全部のたどり着くまでの距離を算出する

import queue


n, m = map(int, input().split())
f = [list(map(str,input())) for _ in range(n)]

s = []
g = []

for i in range(n):
	if f[i].count("S") == 1:
		s = [i, f[i].index("S")]
		break
for i in range(n):
	if f[i].count("G") == 1:
		g = [i, f[i].index("G")]
		break

f_dict = {"#":-1, ".":float("inf"), "G":float("inf"), "S":0}
ff = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
	for j in range(m):
		ff[i][j] = f_dict[f[i][j]]



q = queue.SimpleQueue()

def bfs(ff,q):
	p = q.get()
	ff[p[0]][p[1]] = p[2]
	for dp in [[-1,0,1], [0,-1,1], [1,0,1], [0,1,1]]:
		np = [p[i]+dp[i] for i in range(3)]
		if (0 <= np[0] <= n-1 and 0 <= np[1] <= m-1) and ff[np[0]][np[1]] == float("inf"):
			q.put(np)

	if q.empty():
		return ff

	return bfs(ff,q)

q.put(s+[0])
ans = bfs(ff,q)
print(ans[g[0]][g[1]])

#for i in ff:
#	i_for_print = [str(ii) if ii != -1 else "#" for ii in i ]
#	print("".join(i_for_print))
#	print("")
