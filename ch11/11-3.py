""" 문자열 뒤집기 """

s = input()

zero_set = 0
one_set = 0

comp = s[0]
for n in range(1, len(s)):
    if comp == s[n] and n != len(s) - 1:
        continue
    else:
        if comp == '0':
            zero_set+=1
            comp = '1'
        else:
            one_set+=1
            comp = '0'
result = zero_set if zero_set < one_set else one_set

print(f'{result}')
# print(f'{zero_set} {one_set}')\

""" 
정답
data = input()
count0 = 0
count1 = 0
if data[0] == '1':
    count0 += 1
else:
    count1 += 1
for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1]=='1':
            count0+=1
        else:
            count1+=1
print(min(count0, count1))
"""