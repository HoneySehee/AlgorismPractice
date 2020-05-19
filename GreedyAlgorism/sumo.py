n = int(input("숫자 입력:"))

sumo = []

for i in range(n):
    s, e = map(int, input().split())
    sumo.append((s, e))
sumo.sort(reverse=True)

largetst = 0
cnt = 0

for x, y in sumo:
    if y > largetst:
        largetst = y
        cnt += 1
print(cnt)