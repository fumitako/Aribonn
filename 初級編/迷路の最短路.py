import queue
n,m = map(int,input().split())
#マップの入力
f = [list(map(str, input())) for _ in range(n)]

#キューの宣言
p = queue.Queue()

#探索の関数定義
#pには現在の位置(ci,cj)と、スタートからの距離(cnt)を格納したリストを入れる
def search(f,p):
	ci,cj,cnt = p.get()

	#今いる場所がゴールなら、cntを返す
	if f[ci][cj] == "G":
		return cnt

	#そうでなければ、そこは壁にしてすでに探索し終わったことにする
	else:
		f[ci][cj] = "#"

	#上下左右一つずつ動く
	for dd in [[-1,0],[0,-1],[1,0],[0,1]]:
		di,dj = dd
		ni = ci + di
		nj = cj + dj

		#次に動く場所がフィールド内であり、かつ"."か"G"である必要がある
		if (0 <= ni <= n-1 and 0 <= nj <= m-1) and (f[ni][nj] in [".", "G"]):

			#次に動ける場所だから、キューに入れる。現在の場所から一つ先なので、cnt+=1
			p.put([ni,nj,cnt+1])

	#次へ
	return search(f,p)


#スタート位置の抽出
for i in range(n):
	for j in range(m):
		if f[i][j] == "S":
			s = [i,j,0]
			p.put(s)


cnt = s[2]	#最初cntは0
cnt = search(f,p)
print(cnt)
