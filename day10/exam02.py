# 주민등록번호 검증하기
# reg_num = []
# for i in range(13):
#     num = int(input("주민등록번호 {}번째 자리를 입력하세요: ".format(i+1)))
#     reg_num.append(num)

# reg_num = input("주민등록번호 13자리를 입력하세요: ")

# sum=0
# for i in range(12):
#     if i > 7:
#         a = int(reg_num[i])*(i-6)
#     else:
#         a = int(reg_num[i])*(i+2)
#     sum+=a

# result = 11 - sum%11
# if result >= 10:
#     result -= 10

# if result == int(reg_num[12]):
#     print("인증되었습니다")
# else:
#     print("잘못 입력하셨습니다")

# 주민등록번호 생성
from random import randint

while True:
    year = randint(0,99)
    if year < 10:
        year = '0'+str(year)
    month = randint(1,12)
    if month < 10:
     month = '0'+str(month)
    date = randint(1,31)
    if date < 10:
        date = '0'+str(date)
    gen = randint(1,4)
    remain=''
    for i in range(6):
        a = randint(0,9)
        remain += str(a)

    reg_num = str(year)+str(month)+str(date)+str(gen)+remain
    # print(reg_num)
    sum=0
    for i in range(12):
        if i > 7:
            a = int(int(reg_num[i]))*(i-6)
        else:
            a = int(int(reg_num[i]))*(i+2)
        sum+=a
    # print(sum)
    result = (11 - sum%11)%10
    if result == int(reg_num[12]):
        print("랜덤으로 생성된 주민등록번호:",reg_num)
        break
    


# year = randint(0,100)
# if year < 10:
#     year = '0'+str(year)
# month = randint(1,12)
# if month < 10:
#  month = '0'+str(month)
# date = randint(1,31)
# if date < 10:
#     date = '0'+str(date)
# gen = randint(1,4)
# remain=''
# for i in range(6):
#     a = randint(0,9)
#     remain += str(a)

# reg_num = str(year)+str(month)+str(date)+str(gen)+remain
# print(reg_num)
# sum=0
# for i in range(12):
#     if i > 7:
#         a = int(int(reg_num[i]))*(i-6)
#     else:
#         a = int(int(reg_num[i]))*(i+2)
#     sum+=a
# print(sum)
# result = (11 - sum%11)%10    