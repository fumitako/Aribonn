n = int(input())
l = sorted(list(map(int,input().split())))
ans = 0
while len(l) > 1:
	mini = min(l)
	ind = l.index(mini)
	min1 = l.pop(ind)

	mini = min(l)
	ind = l.index(mini)
	min2 = l.pop(ind)

	ans += min1+min2
	l.append(min1+min2)

print(ans)
