def Count(len):
    cnt = 0
    for x in Line:
        cnt += (x // len)
    return cnt

k, n = map(int, input().split())

Line = []

result = 0
largest = 0

for i in range(k):
    temp = int(input())
    Line.append(temp)
    largest = max(largest, temp)

lt = 1
rt = largest

while lt <= rt:
    mid = (lt+rt) // 2
    if Count(mid) >= n:
        result = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(result)