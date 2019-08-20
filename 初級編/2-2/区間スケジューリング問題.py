#n=10^5では間に合わない気がする

n = int(input())
s = list(map(int,input().split()))
f = list(map(int,input().split()))

inf = float("inf")

ans = 0

while s.count(-inf) < n:
	c = min(f)
	s = [s[i] if s[i] > c else -inf for i in range(len(s))]
	f = [f[i] if s[i] > c else inf for i in range(len(s))]
	ans += 1

print(ans)
