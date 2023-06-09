# 숫자를 입력 받아 음수를 판별하시오

# a = int(input("숫자를 입력하세요: "))
# if a <0:
#     print("음수이며 {}을(를) 입력하였습니다.".format(a))
# else:
#     print(a,"을 입력하였습니다.")


# 태어난 년도를 2자리 혹은 4자리로 입력 받아 우리나라 나이를 구하는 프로그램을 작성하시오

year1 = int(input("태어난 년도를 2자리로 입력하시오: "))
if year1 <= 23:
    age = 23 - year1 + 1
else:
    age = 123 - year1 + 1
print(year1,"년에 태어난 당신은 {}살입니다.".format(age))

year2 = int(input("태어난 년도를 입력하시오: "))
age = 2023 - year2 + 1
print(year2,"년에 태어난 당신은 {}살입니다.".format(age))