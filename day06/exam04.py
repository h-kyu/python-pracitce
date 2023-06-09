# 수를 입력 받아 1부터 입력 받은 값 까지의 합(1)을 구하고
# 수를 입력 받아 1부터 입력받은값 까지의 합(2)를 구하여
# (1)과 (2)의 합(3)을 구하고 1부터 (3)까지의 합을 구하시오


sum1=0
sum2=0
a=1
while True:
    sum=0
    num = int(input("수를 입력하세요: "))
    for i in range(num+1):
        sum += i
    print("결과{}: {} ".format(a,sum))
    sum1 += sum
    if a == 2:
        for i in range(sum1+1):
            sum2 += i
        print("결과3: {}".format(sum2))
        break
    a+=1