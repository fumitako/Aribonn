n = int(input())
r = int(input())
x = list(map(int, input().split()))


ind_left = 0
ind_center = float("inf")
cond_mae = True
cond_ato = False
cnt = 0
for i in range(len(x)):
	if cond_mae:
		if x[i] - x[ind_left] > 10:
			ind_center = i-1
			cnt += 1
			cond_mae = False
			cond_ato = True

	if cond_ato:
		if x[i] - x[ind_center] > 10:
			ind_left = i
			cond_mae = True
			cond_ato = False
	
#もし前半を見ている間に探索が終わってしまったら、一つ足す
if cond_mae == True:
	cnt += 1

print(cnt)
