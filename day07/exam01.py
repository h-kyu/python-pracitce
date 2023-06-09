# 1) 숫자를 입력 받아 음수를 판별하는 함수 정의
def minus(a):
    if a <0:
        return "음수입니다"
    else:
        return "음수가 아닙니다"
    
num = int(input("수를 입력하세요: "))
print(minus(num))

# 2) 태어난 년도를 2자리로 입력하여 나이를 구하는 함수 정의
def birth(a):
    if 100 > a > 23:
        return "당신의 나이는 {}세".format(123 - a + 1)
    elif 0 <= a <= 23:
        return "당신의 나이는 {}세".format(23 - a + 1)
    else:
        return "잘못 입력하셨습니다"
    
year = int(input("태어난 년도를 2자리로 입력하세요: "))
print(birth(year))

# 3) 태어난 년도를 2자리 혹은 4자리로 입력 받아 우리나라 나이를 반환하는 함수 정의
def birth(a):
    if 100 > a > 23:
        return "당신의 나이는 {}세".format(123 - a + 1)
    elif 0 <= a <= 23:
        return "당신의 나이는 {}세".format(23 - a + 1)
    elif 1000 <= a:
        return "당신의 나이는 {}세".format(2023 - a + 1)
    else:
        return "잘못 입력하셨습니다"
    
year = int(input("태어난 년도를 2자리 혹은 4자리로 입력하세요: "))
print(birth(year))
    

# 4) 숫자를 입력 받아 절대값을 반환하는 함수 정의
def value(a):
    if a < 0:
        return '절대값: {}'.format(-a)
    else:
        return '절대값: {}'.format(a)
num = int(input("숫자를 입력하세요: "))
print(value(num))

# 5) 1부터 입력한 수까지의 합을 반환하는 함수 정의
def add(a):
    sum=0
    for i in range(1,a+1):
        sum+=i
    return sum
    
num = int(input("수를 입력하세요: "))
print(add(num))


# 6) 수를 입력 받아 1부터 입력한 수 사이의 2의 배수들의 합을 반환하는 함수
def add(a):
    sum=0
    for i in range(1,a+1):
        if i%2==0:
            sum+=i
    return sum
    
num = int(input("수를 입력하세요: "))
print(add(num))