# import datetime

# year = input("년도 입력")
# y = datetime.datetime.now().year
# if year.isdigit():
#     year = int(year)
#     print("나이는 {}".format(y-year))
# else:
#     print("잘못 입력")

def func(name,age=0):
    print(name,age)
func("홍길동",25)
func("ef")