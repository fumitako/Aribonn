c = list(map(int, input().split()))[::-1] #入力を逆順にして、高額なものから入力を渡す
A = int(input())
tama = [500,100,50,10,5,1]				  #リストに合わせて高額なものから
ans = []
for i in range(6):
	a = A // tama[i]			#最大何枚使えるか
	b = min([a,c[i]])			#実際に何枚使えるか
	ans.append(b)
	A -= tama[i] * b			#使った分だけ合計金額から引きます
	if A == 0:					#達成したら抜ける
		break

print(sum(ans))
