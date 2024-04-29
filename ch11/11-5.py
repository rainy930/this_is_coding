""" 볼링공 고르기 """

N, M = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0

for i in range(0, len(lst)-1):
    for j in range(i, len(lst)):
        if lst[i] == lst[j]:
            continue
        else:
            cnt+=1
print(cnt)

"""
정답 / 풀이 한번 더 살펴보기..
n, m = map(int, input().split())
data = list(map(int, input().split()))

array = [0] * 11

for x in data:
    array[x] += 1

result = 0

for i in range(1, m+1):
    n -= array[i]
    result += array[i] * n

print(result)
"""
