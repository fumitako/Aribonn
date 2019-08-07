import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

ans = 0

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):

            len = a[i] + a[j] + a[k]
            ma = max([a[i], a[j], a[k]])
            rest = len - ma

            if ma < rest:
                ans = max([ans, len])

print(ans)
