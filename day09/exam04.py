# from random import*
# from random import randint, random, uniform, randrange

# i = randint(1,100)  # 1~100 임의의 정수
# print(i)

# f = random()   # 0~1 사이 임의의 float
# print(f)

# f = uniform(1.0, 36.6)   # 1~36.5 사이 임의의 float
# print(f)

# i = randrange(1, 101, 2)   # 1~100 사이 임의의 정수(마지막 숫자 2는 처음숫자로부터의 간격)
# print(i)

# i = randrange(10)   # 0~9 사이 임의의 정수
# print(i)

lotto = 23
from random import randint
while lotto == 23:
        lotto = randint(1,45)
        print(lotto)