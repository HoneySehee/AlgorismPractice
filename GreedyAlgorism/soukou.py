l = int(input())
a = list(map(int, input().split()))
m = int(input())
a.sort()

print(a)

for _ in range(m):
    a[0]+=1
    a[l-1]-=1
    a.sort()

print(a[l-1]-a[0])