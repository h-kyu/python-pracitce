# 다음과 같이 표준 체중을 구하도록 작성
# 표준체중 = (현재 키 - 100) * 0.9

# height = float(input("키 입력 : "))
# print("{}cm에 대한 표준 체중은 {}입니다.".format(height,(height-100)*0.9))

# 다음과 같이 비만도 비율을 구하도록 작성
# 비만도(%) = (현재체중 / 표준체중) * 100

weight1 = float(input("현재 체중 입력 : "))
weight2 = float(input("표준 체중 입력 : "))
percentage = int((weight1/weight2)*100)
print("비만도 : {}%입니다".format(percentage))

# 위 동작을 합하여 키와 몸무게를 입력 받아 비만도를 구하도록 작성

# m_height = float(input("키 입력 : "))
# m_weight = (m_height-100)*0.9
# p_weight = float(input("현재 체중 입력 : "))
# m_percentage = (p_weight/m_weight)*100
# print("비만도 : {:.0f}%입니다".format(m_percentage))
