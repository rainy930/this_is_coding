""" 상하좌우 """

N = int(input())

x = 1
y = 1
plans = input().split()
x_moves = [-1, 1, 0, 0]
y_moves = [0, 0, -1, 1]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + x_moves[i]
            ny = y + y_moves[i]
    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue
    x, y = nx, ny
print(x,y)