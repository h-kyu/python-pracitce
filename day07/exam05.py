# 1) 임의의 개수로 실수를 입력 받아 최소값과 최대값을 제외한 나머지 점수들의 합계를 반환하는
#    함수를 정의(가변인자 활용)
# for i in range(int(input("임의의 개수를 입력하세요: "))):
#     num = float(input("실수를 입력하세요: "))
    
# def result(*args):
#     sum = 0
#     for num in args:
#         num = int(num)
#         sum += num
#     sum -= (max(args)+min(args))
#     return sum
# scores=[]
# score=0
# while True:
#     score = int(input("점수를 입력하세요(0입력시 종료): "))
#     if score == 0:
#         break
#     scores.append(score)
# print("입력하신 점수의 합계: {}".format(result(*scores)))


# 2) 합계에 해당하는 값과 개수를 입력 받아 평균을 반환하는 함수 정의
# def result(*args):
#     sum = 0
#     for num in args:
#         num = int(num)
#         sum += num
#     sum -= (max(args)+min(args))
#     return sum
# scores=[]
# score=0
# count=0
# while True:
#     score = int(input("점수를 입력하세요(0입력시 종료): "))
#     if score == 0:
#         break
#     scores.append(score)
#     count+=1
# print("입력하신 점수의 평균: {}".format(result(*scores)/count))

# 3) cm값을 inch 값으로 반환하는 함수(1 INch == 2.54 cm) 정의
# def change(a):
#     a /= 2.54
#     return a
# num = float(input("inch로 반환하고자하는 cm를 입력하세요: "))
# print("{:.2f}inch 입니다.".format(change(num)))

# 4) 파일의 용량(byte)을 매개변수로 입력 받아 bit단위로 반환하는 함수 정의
#   파일의 용량을 입력할 때 단위도 입력한다.(G, M, K)
#   ex) byteToBit(32,'G')
#       byteToBit(64,'M')

# def byteToBit(a,b):
#     if b == 'B':
#         return a*8
#     elif b == 'K':
#         return a*8*1024
#     elif b == 'M':
#         return a*8*(1024**2)
#     elif b == 'G':
#         return a*8*(1024**3)
#     elif b == 'T':
#         return a*8*(1024**4)
#     else:
#         return "지원하지 않는 기능입니다"
# storage=int(input("bit로 바꾸고자 하는 파일의 용량을 입력하세요: "))
# unit=input("파일 용량 단위를 입력하세요(B=byte,K=KB,M=MB,G=GB,T=TB): ")
# print("{} bit 입니다".format(byteToBit(storage,unit)))


# 5) 인자로 N을 전달하면 N에 대한 팩토리얼을 반환하는 함수 정의

# def factorial(a):
#     mul=1
#     while a != 0:
#         mul*=a
#         a-=1
#     return mul

# N = int(input("수를 입력하세요: "))
# print("{}에 대한 팩토리얼: {}".format(N, factorial(N)))

# 6) 인자로 N을 전달하면 거꾸로 만든 수를 반환하는 함수 정의

# def back(a):
#     result = ''
#     while a != 0:
#         result += str(a%10)+''
#         a //= 10
#     return result
# N = int(input("거꾸로 만들 수를 입력하세요: "))
# print(back(N))

#임의의 개수로 실수를 입력 받아 
# 최소값과 최대값을 제외한 나머지 점수들의 합계를 
# 반환하는 함수를 정의(가변인자 활용)
def middleSum(*args):
    max_val, min_val, total = 0,0,0
    size = len(args)
    if size != 0:
        min_val = args[0]
    else:
        return -1
    for i in range(size):
        if args[i] >= max_val:      max_val = args[i]
        elif args[i] <= min_val:    min_val = args[i]
        total += args[i]

    result = total - (min_val + max_val)
    return result

#그냥 호출 테스트
# print( middleSum() )
# print( middleSum(1,2,3,4,5,6) )
# print( middleSum(0,1,2,3,4,5,6,7,8,9,10,11) )

#리스트 전달(unpack)
data = []
print( middleSum(*data) )

#입력받은 문자열을 리스트로 만들어 전달(unpack)
data = input('숫자만 입력(빈칸으로 구분):').split()
i = 0
while i < len(data):
    data[i] = int(data[i])
    i += 1
print( middleSum(*data) )