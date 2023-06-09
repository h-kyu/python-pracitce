# # 사용자로부터 화폐금액을 입력 받아 화폐종류의 각 개수를 출력하세요.(변수만 사용)
money = int(input("돈을 입력하세요: "))
m5 = 0
m1 = 0
m_5 = 0
m_1 = 0
m__5 = 0
m__1 = 0
m50 = 0
m10 = 0
while money != 0:
    if money >= 50000:
        m5 = money // 50000
        money %= 50000
    elif money >= 10000:
        m1 = money // 10000
        money %= 10000
    elif money >= 5000:
        m_5 = money // 5000
        money %= 5000
    elif money >= 1000:
        m_1 = money // 1000
        money %= 1000
    elif money >= 500:
        m__5 = money // 500
        money %= 500
    elif money >= 100:
        m__1 = money // 100
        money %= 100
    elif money >= 50:
        m50 = money // 50
        money %= 50
    else:
        m10 = money // 10
        break
print("5만원: {}, 1만원: {}, 5천원: {}, 1천원: {}, 500원: {}, 100원: {}, 50원: {}, 10원: {}".format(m5,m1,m_5,m_1,m__5,m__1,m50,m10))

# 십진수를 이진수로 변환하는 프로그램을 작성하세요

num = int(input("숫자를 입력하세요: "))
a=1
while num > 0:
    if num < 2**a:
        while a != 0:
            if num // 2**(a-1) == 1:
                print(1,end='')                
            else:
                print(0,end='')
            num -= 2**(a-1)
            a-=1
    a+=1