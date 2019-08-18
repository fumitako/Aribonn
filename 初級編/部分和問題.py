import sys
n = int(input())
a = list(map(int, input().split()))
k = int(input())

def Base_10_to_n(X, n):
    X_dumy = X
    out = ''
    while X_dumy>0:
        out = str(X_dumy%n)+out
        X_dumy = int(X_dumy/n)
    return out

for i in range(2**n):
	b = Base_10_to_n(i,2).rjust(n,"0")
	s = 0
	for j in range(len(b)):
		if b[j] == "1":
			s += a[j]
	if s == k:
		print("Yes")
		sys.exit()

print("No")
