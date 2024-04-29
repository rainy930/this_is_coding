""" 모험가 길드 """

N = int(input())
lst = list(map(int, input().split()))
lst.sort()

scare = 0
cnt = 0
group_cnt = 0
for n in lst:
    cnt+=1
    scare = n # 정답지를 보고 여길 줄일 수 있음
    if scare == cnt:
        group_cnt+=1
        cnt = 0
print(group_cnt)


"""
정답

n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
count = 0

for i in data:
    count+=1
    if count >= i:
        result+=1
        count=0
print(result)
"""
