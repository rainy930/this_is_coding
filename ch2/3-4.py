""" 1이 될 때 까지 """

N, K = map(int, input().split())

calculated_cnt = 0

# # Case 1
# while True:
#     if N == 1:
#         break
#     if N % K == 0:
#         N/=K
#     else:
#         N-=1
#     calculated_cnt += 1
# print(calculated_cnt)

# Case 2
while True:
    target = (N // K) * K
    calculated_cnt += (N - target)
    N = target
    if N < K:
        break
    N //= K
    calculated_cnt+=1

calculated_cnt -= 1
print(calculated_cnt)
