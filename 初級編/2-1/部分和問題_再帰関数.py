n = int(input())
a = list(map(int, input().split()))
k = int(input())


#if内に次の関数があるたびに、その関数を呼び出している。
#最終的に一つ目のifでSUM=kを確認してreturn True。実質的にそれまでのif分は再帰させるためだけにあるように見える
def dfs(list,k,i,SUM):
	if i == len(list):
		return SUM == k
	if dfs(list,k,i+1,SUM):
		return True
	if dfs(list,k,i+1,SUM+list[i]):
		return True

	return False

cond = dfs(a,k,0,0)

print("Yes") if cond else print("No")
