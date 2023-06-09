# 올해 년도와 태어난 년도를 입력 받아 현재 나이를 계산하도록 작성

this_y = int(input("올 해 연도: "))
born_y = int(input("태어난 연도: "))
print("당신의 나이는 : {}입니다.".format(this_y-born_y))

# 600kg 제한의 화물용 엘리베이터가 있다
# 2개의 물건에 대한 무게를 실수로 입력 받아 현재 엘리베이터에 더 적재할 수 있는 무게를 구하도록 작성

object1 = float(input("첫번째 물건의 무게 : ")) 
object2 = float(input("두번째 물건의 무게 : "))
print("남은 무게 : {}/600.0kg".format(600-object1-object2))

# 다음과 같이 동작하도록 작성
# 당신의 이름은 무엇입니까? 이규철
# 이규철님의 나이는 몇 살입니까?
# 이규철님의 나이는 20살 입니다

name = input("당신의 이름은 무엇입니까?")
age = int(input("{}님의 나이는 몇 살 입니까?".format(name)))
print("{}님의 나이는 {}살 입니다.".format(name,age))







