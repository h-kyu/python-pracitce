# List, Dictionary, Tulpe, Set 등을 활용하여 다음을 구현하세요
# 로또 1~100회 추첨 번호 통계 구하기
# 출력 모양은 자유, dictionary 활용
# K = 회차, V = 당첨 번호 목록
from random import randint

V = []
a=1
while a < 101:
    lottonum = []
    for i in range(7):
        lotto = randint(1,45)
        while lotto in lottonum:
            lotto = randint(1,45)
        lottonum.append(lotto)
    V.append(lottonum)
    a+=1
for i in range(len(V)):
    for j in range(7):
        if V[i][j] < 10:
            V[i][j] = ('0'+str(V[i][j]))


b = 1
counts_V=[]
while b < 46:
    count=0
    for i in range(len(V)):
        for j in range(7):
            if b == int(V[i][j]):
                count+=1
    counts_V.append(count)
    b+=1
counts_K=[]
for i in range(1,46):
    if i < 10:
        a = ('0'+str(i))
        number = "[{}]번:".format(a)
        counts_K.append(number)
    else:
        number = "[{}]번:".format(i)
        counts_K.append(number)


counts = {}
for i in range(45):
    counts[counts_K[i]]=str(counts_V[i])+"회"

counts_keys = counts.keys()
space = 1
for i in counts_keys:
    print(i+counts[i]+'\t',end='')
    if space%5==0:
        print()
    space+=1


for i in range(len(V)):
    V[i][6] = 'Bonus['+str(V[i][6])+']'

K = []
for i in range(101):
    round = '■{}회차■'.format(i+1)
    K.append(round)
LOTTO = {}
for i in range(len(V)):
    LOTTO[K[i]]=V[i]
LOTTO_keys = LOTTO.keys()
for i in LOTTO_keys:
    print(i,*LOTTO[i])

