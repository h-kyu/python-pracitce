from random import randint

# 1
num_lst = []
flag_lst = []
for i in range(45):
    flag_lst.append(False)

for i in range(6):
    flag = True
    num = randint(1,45)
    if flag_lst[num-1] == False:
        flag = not flag
    if flag:
        while flag_lst[num-1] == False:
            num = randint(1,45)
        flag_lst[num-1] = True
    else:
        flag_lst[num-1] = True
    num_lst.append(num)
print(num_lst)
print(flag_lst)

# 2

num_lst = list(range(1,46))
a = 0
n = int(input("swap 횟수: "))
while a <= n :
    num1, num2 = randint(1,45), randint(1,45)
    num_lst[num1-1], num_lst[num2-1] = num_lst[num2-1], num_lst[num1-1]
    a+=1
for i in range(6):
    print(num_lst[i], end=' ')

