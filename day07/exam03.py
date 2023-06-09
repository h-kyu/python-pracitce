#비만도를 측정하는 프로그램을 작성하시오

# def obesity(h,kg):
#     kg1 = (h-100)*0.9
#     obesity = (kg/kg1)*100
#     if obesity < 80:
#         return "저체중입니다"
#     elif 80 <= obesity < 90:
#         return "경한저체중입니다"
#     elif 90 <= obesity < 110:
#         return "정상체중입니다"
#     elif 110 <= obesity < 120:
#         return "과체중입니다"
#     elif 120 <= obesity < 130:
#         return "경도비만입니다"
#     elif 130 <= obesity < 150:
#         return "중증도비만입니다"
#     elif 150 <= obesity < 200:
#         return "고도비만입니다"
#     else:
#         return "위험한 비만입니다"

# height = int(input("현재 신장을 입력하세요: "))
# weight = int(input("현재 체중을 입력하요: "))
# print(obesity(height,weight))


# def 표준체중(h):
#     s_kg = (h-100)*0.9
#     return s_kg

# def 비만도(kg,s_kg):
#     obesity = (kg/s_kg)*100
#     if obesity < 80:
#         return "저체중입니다"
#     elif 80 <= obesity < 90:
#         return "경한저체중입니다"
#     elif 90 <= obesity < 110:
#         return "정상체중입니다"
#     elif 110 <= obesity < 120:
#         return "과체중입니다"
#     elif 120 <= obesity < 130:
#         return "경도비만입니다"
#     elif 130 <= obesity < 150:
#         return "중증도비만입니다"
#     elif 150 <= obesity < 200:
#         return "고도비만입니다"
#     else:
#         return "위험한 비만입니다"

# height = float(input("현재 신장을 입력하세요: "))
# weight = float(input("현재 체중을 입력하요: "))
# print("표준체중: {}".format(표준체중(height)), "비만도: {}".format(비만도(weight,표준체중(height))))

def 표준체중(x):
    return round((x - 100) * 0.9, 2)
    
def 비만도(y):
    y = round((weight / 표준체중(height)) * 100, 2)
    
    if y < 80:
        return f"{y}, 저체중"
    elif y < 90:
        return f"{y}, 경한 저체중"
    elif y < 110:
        return f"{y}, 정상체중"
    elif y < 120:
        return f"{y}, 과체중"
    elif y < 130:
        return f"{y}, 경도비만"
    elif y < 150:
        return f"{y}, 중증도비만"
    elif y < 200:
        return f"{y}, 고도비만"
    else:
        return f"{y}, 위험한 비만"

height = float(input("현재 신장 입력(cm): "))
weight = float(input("현재 체중 입력(kg): "))

print(f"표준체중: {표준체중(height)}")
print(f"비만도는 {비만도(weight)}")

