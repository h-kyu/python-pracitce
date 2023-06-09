# from random import *
# # year = input("주민번호 입력(앞자리 뒷자리는 띄어주세요):") 
# # ↑ 주민번호 검증기
# #431024 1452315
# #01 2 345678901
# # ↓ 주민번호 생성기
# year = ""
# for i in range(11):
#     if i ==2:
#         a = randint(1,12)
#         if len(str(a)) == 1:
#             year = year+"0"+str(a)
#             continue
#         year = year+str(a)
#         continue
#     if i == 3:
#         a = randint(1,31)
#         if len(str(a)) == 1:
#             year = year+"0"+str(a)
#             continue
#         year = year+str(a)
#         continue
#     if i == 4:
#         year = year+" "
#         continue
#     if i == 5:
#         a = randint(1,4)
#         year  =year+str(a)
#     a = randint(0,9)
#     year= year+str(a)
# print(year)
# a = 2
# result = 0
# for i in range(13):
#     if i == 6:
#         continue
#     result= result+ int(year[i])*a
#     a+=1
#     if a == 10:
#         a = 2

# s = 11 - (result%11)
# if len(str(s)) == 2:
#     s = str(s)
#     s = s[1]

# if int(s) == int(year[13]):
#     print(f"검증번호:{s}")
# else:
#     print(f"틀린 주번입니다. {year[13]}나와야됨")
#     print(s)

reg_num = []

reg_num = input("주민등록번호 13자리를 입력하세요: ")

sum=0
for i in range(12):
    if i > 7:
        a = int(reg_num[i])*(i-6)
    else:
        a = int(reg_num[i])*(i+2)
    sum+=a

result = 11 - sum%11
if result >= 10:
    result -= 10

if result == int(reg_num[12]):
    print("인증되었습니다")
else:
    print("잘못 입력하셨습니다")