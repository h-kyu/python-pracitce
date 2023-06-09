for i in range(3):
    for j in range(5):
        print(i+j+3, end=" ")
    print("")

# 두 수를 입력 받아 큰 수에서부터 작은 수까지 출력되도록 프로그램 작성
num1 = int(input("수를 입력하세요: "))
num2 = int(input("수를 입력하세요: "))

if num1<num2:
    for i in range(num2-num1+1):
        print(num2 - i, end=" ")
else:
    for i in range(num1-num2+1):
        print(num1 - i, end=" ")

print()
# 수를 입력 받아 0부터 입력 받은 수까지 3의 배수를 출력되도록 프로그램을 작성.(0은 제외)

num = int(input("수를 입력하세요: "))
for i in range(1, num+1):
    if i%3 != 0:
        continue
    print(i, end=" ")