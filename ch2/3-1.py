""" 거스름돈 (87p)"""

n = int(input('손님에게 거슬러 줘야할 금액: '))
count = 0

coin_types = [500, 100, 50, 10]
coin_cnt= int[0, 0, 0, 0]

for coin in coin_types:
    coin_cnt[count] = n / coin
    n %= coin
    count+=1

print(f'500 : {coin_cnt[0]}\n100 : {coin_cnt[1]}\n50 : {coin_cnt[2]}\n10 : {coin_cnt[3]}\n\n최소 동전 개수 : {sum(coin_cnt)}')