#비만도를 측정하는 프로그램을 작성하시오

height = int(input("현재 신장을 입력하세요: "))
weight = int(input("현재 체중을 입력하요: "))
s_weight = (height-100)*0.9
obesity = (weight/s_weight)*100

if obesity < 80:
    print("저체중입니다")
elif 80 <= obesity < 90:
    print("경한저체중입니다")
elif 90 <= obesity < 110:
    print("정상체중입니다")
elif 110 <= obesity < 120:
    print("과체중입니다")
elif 120 <= obesity < 130:
    print("경도비만입니다")
elif 130 <= obesity < 150:
    print("중증도비만입니다")
elif 150 <= obesity < 200:
    print("고도비만입니다")
else:
    print("위험한 비만입니다")