l = list(map(int,input().split()))
n = 0
for i in range(len(l)-1):
    if l[i] <= l[i+1]:
        n += 1
if n == 1 :
    print("True")
else:
    print("False")