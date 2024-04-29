""" 만들 수 없는 금액 """

n = int(input())

lst = list(map(int, input().split()))

lst.sort()

target = 1
for n in lst:
    if target < n:
        break
    else:
        target+=n
print(target)

""" 
실패 문제

상세 풀이 
1) https://kk-programming.tistory.com/11
2) https://wooono.tistory.com/542
"""