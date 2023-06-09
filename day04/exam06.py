# 1) 10 이하의 정수를 5개 입력 받아 짝수이면 출력

num=''
for i in range(5):
    a = int(input("10 이하의 정수를 입력하세요: "))
    if a%2==0:
        num += (str(a)+' ')
print("짝수:", num)


# 2) 수를 입력 받아 1부터 입력한 수 사이의 2의 배수를 출력
num = int(input("숫자를 입력: "))
for i in range(1,num+1):
    if i%2==0:
        print(i, end=" ")

# 3) 수를 입력 받아 1부터 입력한 수 사이의 3의 배수를 출력
num = int(input("숫자를 입력: "))
for i in range(1,num+1):
    if i%3==0:
        print(i, end=" ")

# 4) 수를 입력 받아 1부터 입력한 수 사이의 2의 배수와 3의 배수를 출력
num_2 =''
num_3 =''
num = int(input("숫자를 입력: "))
for i in range(1,num+1):
    if i%2==0:
        num_2 += (str(i)+' ')
    if i%3==0:
        num_3 += (str(i)+' ')
print("2의 배수 :", num_2 , "3의 배수 :", num_3)

# 5) 수를 입력 받아 1부터 입력한 수 사이의 2와 4의 공배수를 출력

num = int(input("숫자를 입력: "))
for i in range(1,num+1):
    if i%4==0:
        print(i, end=" ")

# 6) 5개의 점수를 입력 받아 최대값을 출력
num_max = 0
for i in range(5):
    num = int(input("{}번째 100 이하의 점수를 입력하세요: ".format(i+1)))
    if num_max < num:
        num_max = num
print("입력하신 점수중 최대값: {}".format(num_max))

# 7) 100 이하의 점수 5개를 입력 받아 최소값을 구하시오
num_min = 100
for i in range(5):
    num = int(input("{}번째 100 이하의 점수를 입력하세요: ".format(i+1)))
    if num_min > num:
        num_min = num
print("입력하신 점수중 최소값: {}".format(num_min))


# 8) 5개의 점수를 입력 받아 최대값과 최소값을 제외한 나머지 점수의 합계와 평균을 구하시오
sum=0
avg=0
num_max = 0
num_min = 100
for i in range(5):
    num = int(input("{}번째 100 이하의 점수를 입력하세요: ".format(i+1)))
    sum += num
    if num_max < num:
        num_max = num
    if num_min > num:
        num_min = num
sum1 = sum-num_max-num_min
avg1=sum1/3
print("합: {} 평균: {}".format(sum1,avg1))
