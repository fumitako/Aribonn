import collections as c
N = int(input())
inp = input()
s = c.deque(inp)
sr = c.deque(inp[::-1])
t = []

while len(s) > 0:
	if s <= sr:
		t.append(s.popleft())
		sr.pop()
	else:
		t.append(sr.popleft())
		s.pop()
		

print("".join(t))
