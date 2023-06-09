from random import randint

lottonum = []
for i in range(6):
    lotto = randint(1,45)
    while lotto in lottonum:
        lotto = randint(1,45)
    lottonum.append(lotto)

    
print('로또 번호: ', end='')
print(lottonum)

# lottonum = list(range(6))
# for i in range(len(lottonum)):
#     lottonum[i] = randint(1,45)
#     while lottonum[i] in lottonum:
#         lottonum[i] = randint(1,45)
    
# print('로또 번호: ', end='')
# print(lottonum)

# lottonum = []

# while len(lottonum) < 6:
#     num = randint(1, 45)
#     if num not in lottonum:
#         lottonum.append(num)

# print('로또 번호:', lottonum)

# lottonum = list(range(6))

# for i in range(len(lottonum)):
#     lottonum[i] = randint(1,45)   
#     if lottonum[i-1]==lottonum[i]:
#         i-=1
#         lottonum.remove[i]

# print('로또 번호:', end="")
# print(lottonum)