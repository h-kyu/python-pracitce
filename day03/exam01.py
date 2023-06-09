# 세 수를 입력 받아 합계와 평균을 구하시오
# 단, 소수점 2자리까지만 출력

# a,b,c = input('입력: ').split() -> split 함수를 사용하면 빈칸 3개로 입력 받아 a,b,c에 각각 대입 가능하다
a = int(input('첫번째 수 입력: '))
b = int(input('두번째 수 입력: '))
c = int(input('세번째 수 입력: '))
sum = a + b + c
avg = sum/3 
print('합: {}, 평균: {}'.format(sum,round(avg,2)))

# 삼각형의 두 각을 입력 받아 나머지 하나의 각을 구하는 프로그램을 작성

angle1 = int(input('첫번째 각도 입력: '))
angle2 = int(input('두번째 각도 입력: '))
angle3 = 180 - (angle1 + angle2)
print("나머지 각은 {}도이다.".format(angle3))