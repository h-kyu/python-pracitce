# 하나의 수를 입력 받아 12의 약수이면 true를 거짓이면 false를 출력

a = int(input("수를 입력: "))
print(12%a==0)

# 두 수를 입력 받아 첫번째 수가 두번째 수의 제곱근이면 true를 아니면 false를 출력

num1 = int(input("첫번째 수 입력: "))
num2 = int(input("두번째 수 입력: "))

print(num1**2==num2)