""" 숫자 카드 게임 (96p) """

M, N = map(int, input().split())
# print(f'{M} {N}')
min_value = 0

for i in range(M):
    data = list(map(int, input().split()))
    if min_value < min(data):
        min_value = min(data)
print(min_value)