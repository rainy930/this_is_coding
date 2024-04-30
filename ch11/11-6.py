""" 무지의 먹방 라이브 """

def solution(f_t, a_f):
    time = 0    
    while True:
        current = time % len(f_t)
            
        if f_t[current] > 0:
            f_t[current]-=1
            time+=1
            # print(f'{time} / {f_t}')
        else:
            time+=1
        if a_f == time:
            return current

food_times = list(map(int, input().split()))

if len(food_times) < 1 or len(food_times) > 2000:
    print("food_times 값을 잘못 입력하셨습니다.")
    print(food_times)
    exit()
for num in food_times:
    if num < 1 or num > 1000:
        print("food_times 값을 잘못 입력하셨습니다.")
        exit()
        
k = int(input())


result = solution(food_times, k)
print(f'{k}초에서 네트워크 장애가 발생했습니다. {result}번 음식을 섭취해야 할 때 중된되었으므로, 장애 복수 후에 {result}번 음식부터 다시 먹기 시작하면 됩니다.')

"""
정답 / https://school.programmers.co.kr/learn/courses/30/lessons/42891?language=python3 (동작 검증)

import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))
    
    sum_value=0
    previous=0
    length = len(food_times)
    
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value+= (now-previous) * length
        length -= 1
        previous = now
        
    result = sorted(q, key =lambda x: x[1])
    return result[(k - sum_value) % lenth[1]]

"""