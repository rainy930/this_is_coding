""" 왕실의 나이트 """ 

lo = input() 

y_cood = int(lo[1])
x_cood = int(ord(lo[0])) - int(ord('a')) + 1

possible_move = [(-2, -1), (-1, -2), (2, -1), (1, -2), (-1, 2), (2, 1), (1, 2)]

result = 0
for p in possible_move:
    x = x_cood + p[0]
    y = y_cood + p[1]

    if x >= 1 and x <= 8 and y >= 1 and y <= 8:
        result+=1
print(result)