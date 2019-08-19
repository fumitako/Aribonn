n,m = map(int, input().split())
f = [list(map(str,input())) for _ in range(n)] #入力後enter必要なの直したい…

def search(f,i,j):
	jouge = [-1,0,1]
	sayuu = [-1,0,1]
	if i == 0:
		jouge = [0,1]
	elif i == n-1:
		jouge = [-1,0]
	if j == 0:
		sayuu = [0,1]	
	elif j == m-1:
		sayuu = [-1,0]
	for ii in jouge:
		for jj in sayuu:
			if ii == 0 and jj == 0:
				continue
			elif f[i+ii][j+jj] == "w":
				f[i+ii][j+jj] = "."
				search(f,i+ii,j+jj)
	return f

cnt = 0
for i in range(n):
	for j in range(m):
		if f[i][j] == "w":
			f[i][j] = "."
			cnt += 1
			f = search(f,i,j)


print(cnt)
