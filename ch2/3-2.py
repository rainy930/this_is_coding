""" 큰 수의 법칙 (92p)"""

N, M, K = map(int, input().split())
# print(f'{N} {M} {K}')

sample = list(map(int, input().split()))
sample.sort()

first = sample[N-1]
second = sample[N-2]

result = 0

## Case 1
# max_cnt= K

# for i in range(M):
#     if max_cnt > 0:
#         result += first
#         max_cnt -= 1
#     else:
#         result += second
#         max_cnt = K

# print(result)
            
# Case 2 
a = M / (K + 1) 
b = M % (K + 1)

result += ((a * K) + b) * first
result += a * second

print(result)