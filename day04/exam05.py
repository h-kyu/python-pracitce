text = input("문자 입력: ")
for i in range(1,6):
    print("{}.{}".format(i,text))

num1 = int(input("문자(숫자) 입력: "))
sum=0
for i in range(1,num1+1):
    sum += i
print("1 ~ {} 합: {}".format(num1,sum))

num2 = int(input("문자(숫자) 입력: "))
for i in range(num2+1):
    print(num2)
    num2 -= 1