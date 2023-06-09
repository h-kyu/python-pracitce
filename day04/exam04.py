# 몸무게를 kg단위로 입력하면 파운드(lb)단위로 변경하고 다음 체급표에 맞게 체급을 출력하는 프로그램 작성

# kg = int(input("몸무게를 입력하세요: "))
# lb = kg*2.204623
# if lb < 125:
#     weight="fly"
# elif lb < 135:
#     weight="bantam"
# elif lb < 145:
#     weight="feather"
# elif lb<155:
#     weight="light"
# elif lb<170:
#     weight="welter"
# elif lb<185:
#     weight="middle"
# elif lb<205:
#     weight="light heavy"
# else:
#     weight="heavy"

# print("당신은 {}급이며 체중은 {:.4f}파운드입니다.".format(weight,lb))

# 주민번호 7자리를 입력 받아 나이와 성별을 구하시오

reg_num = int(input("주민번호 7자리를 입력하세요: "))
gender = reg_num%10
age = reg_num//100000

if gender == 2 or gender == 4:
    gender = "여성"
elif gender == 1 or gender == 3:
    gender = "남성"
else:
    print("주민번호를 잘못 입력하셨습니다")

if age > 23:
    age = 123 - age + 1
else:
    age = 23 - age + 1


if age < 20:
    old = "미성년"
else:
    old = "성년"

print("당신은 {} {}이며 {}입니다.".format(age,gender,old))