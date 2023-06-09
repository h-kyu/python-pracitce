# 수를 입력 받아 0을 제외한 7의 배수를 입력 받은 수 만큼 출력하시오
num = int(input("수를 입력하세요: "))
for i in range(num):
    print((i+1)*7, end=" ")

print()

# 수를 입력 받아 1부터 입력 받은 수 사이의 2의 배수와 3의 배수를 출력
# 단 2와 ㄱ의 공배수는 출력 제외
num = int(input("수를 입력하세요: "))
num_2 = "2의 배수: "
num_3 = "3의 배수: "
for i in range(1, num+1):
    if i%2==1:
        continue
    elif i%3==0:
        continue
    num_2 += (str(i)+' ')
for i in range(1, num+1):
    if i%3==0:
        if i%2==0:
            continue
        num_3 += (str(i)+' ')
print(num_2)
print(num_3)

# 3.
for i in range(3):
    for j in range(4):
        print((i+1)*(j+1), end=' ')
    print()