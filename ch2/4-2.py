""" 시각 """

"""
if A in B      : B 안에 A가 있으면 참
if A not in B  : B 안에 A가 없으면 참
"""

n = int(input())
total = 0

for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
                total += 1
print(total)    
