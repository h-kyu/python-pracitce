# 1) 10 이하의 정수를 입력하시오(10이상이면 다시 입력 받도록)
while True:
    num = int(input("10 이하의 정수를 입력하시오: "))
    print("입력하신 숫자는:",num)
    if num > 10:
        print("범위 밖의 숫자입니다.")
    else:
        break


# 2) 3의 배수를 판별하는 프로그램을 작성(단, Q가 입력되면 종료)
# - 입력 받자 마자 제일 먼저 q인지 판별. 아니면 정수로 반환해서 3의 배수를 판별
while True:
    num = input("숫자를 입력하세요(Q입력시 종료): ")
    if num == 'Q':
        print("종료합니다")
        break
    elif int(num)%3==0:
        print("3의 배수 입니다")
    else:
        print("3의 배수가 아닙니다")
        

# 3) 1자리 숫자를 계속 입력 받아 합과 입력된 개수를 구하시오
# (단, 2자리 이상의 숫자가 들어오면 입력된 2자리 이상의 수까지 계산하고 종료)
i=0
sum=0
while True:
    num = int(input("한자리 숫자를 입력하세요: "))
    i+=1
    sum+=num
    print("현재까지 입력한 횟수: {} 모든 수의 합: {}".format(i,sum))
    if num >= 10:
        print("두자리 숫자를 입력하여 종료합니다.")
        break

# 4) 수를 입력 받아 거꾸로 수를 출력하도록 프로그램을 작성
num = int(input("수를 입력하세요: "))
while num != 0:
    result = num%10
    num = num//10
    print(result, end='')