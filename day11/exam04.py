# from random import randint

# k = []
# dic={}

# for i in range(100):
#     k.append(i)
#     v=set()
#     while len(v) < 7:
#         a=randint(1,45)
#         v.add(a)
#         dic[k[i]+1]=v

# for i in range(1,101):
#     print(f'{i}회차:',end=" ")
#     for j in range(7):        
#         if j == 6:
#             print(f'bonus:[{list(dic[i])[j]}]')
#         else:
#             print(f'{list(dic[i])[j]}',end=" ")

# for i in range(1,46):
#     Sum = 0
#     print(f'{i}번:',end=" ")
#     for j in range(1,101):
#         for k in range(7):
#             if list(dic[j])[k] == i :
#                 Sum+=1
#     print(f'{Sum}회',end=" ")
#     if i%5 ==0:
#         print()
# 로또 1~100회 추첨 번호 통계 구하기
# 출력 모양 자유 / 딕셔너리 활용 (K = 회차, V = 당첨번호목록)

from random import randint

lotto_dict = {}
lottoNum = []

# 1~100회까지 임의 당첨번호 생성
print('----- 로또 당첨 번호 생성 -----')

for i in range(100) :
    while len(lottoNum) < 7 :
        number = randint(1, 45)
        if number not in lottoNum :
            lottoNum.append(number)
    lotto_dict[i+1] = lottoNum
    lottoNum = []
    # print(f'■{i+1}회차■ {list(lotto_dict.get(i+1))}')

for k, v in lotto_dict.items() :
    print(f'■{k}회차■', end=' ')
    for val in v :
        if val == v[-1] :
            print(f'Bonus[{val:02d}]', end=' ')
        else :
            print(f'{val:02d}', end=' ')
    
    print()

print()
# 1~100회동안 해당 로또번호가 몇 번 등장했는지 카운트 후 통계
print('---------- 당첨 번호 통계 ----------')

numCnt = [0 for i in range(45)]
for value in lotto_dict.values() :
    for cnt in value :
        numCnt[cnt-1] += 1

for i in range(len(numCnt)) :
    print(f'[{i+1:02d}]번:({numCnt[i]:02d})회', end='\t')
    if (i+1)%5 == 0 :
        print()