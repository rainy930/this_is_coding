""" 곱하기 혹은 더하기 """

s = input()
if len(s) < 0 or len(s) > 20:
    print('일정 범위 외로 입력하셨습니다.')

result = 0 # 초기값에 아에 s[0]을 넣고
for i in range(0, len(s)): # for 문에 시작을 1로 하면 되네
    if i == 0: # 그러면 이 if 문은 없어도 됨
        result = int(s[i])
        continue
    if result <= 1 or int(s[i]) <= 1:
        result+=(int(s[i]))
    else:
        result*=(int(s[i]))
print(result)

"""
정답
data = input()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)
"""