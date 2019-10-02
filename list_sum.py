l = list(map(int,input().split()))
k = int(input())
g = 0
s = 0
for i in range(len(l)):
    if g != len(l):
        p = []
        s = 0
        for j in l[g::]:
            s = s + j
            p.append(j)
            if s == k:
                print(p)
        g += 1