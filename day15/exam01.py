class Person:
    def __init__(self, name = None, age = 0):
        self.__name = name
        self.__age = age

    def printInfo(self):
        print(self.__name, self.__age)

def main():
    p1 = Person('홍길동', 20)
    print(p1.__dict__)
    p1.__dict__['age'] = 30 # age가 추가됨
    p1.__dict__['__age'] = 40 # __age가 추가됨
    print(p1.__age) # 객체의 __age가 아닌 추가된 멤버 __age에 접근
    #만약 __age를 추가하지 않았다면 AttributeError 발생
    p1.printInfo()
    print(p1.age) # 추가된 age
    print(p1.__dict__)

main()
# =======================================================================
# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#     def setX(self, x):
#         self.__x = x
#     def setY(self, y):
#         self.__y = y
#     def getX(self):
#         return self.__x
#     def getY(self):
#         return self.__y

# p1 = Point(10, 20)
# print(p1.getX(), p1.getY())
# p1.setX(100)
# p1.setY(200)
# print(p1.getX(), p1.getY())

#=================================================
# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y   
#     @property
#     def x(self):
#         #print('x getter 호출')
#         return self.__x
#     @property
#     def y(self):
#         #print('y getter 호출')
#         return self.__y
#     @x.setter
#     def x(self, x):
#         #print('x setter 호출')
#         self.__x = x
#     @y.setter
#     def y(self, y):
#         #print('y getter 호출')
#         self.__y = y

# p1 = Point(10, 20)
# print(p1.x, p1.y) # 직접 접근하듯 사용. 실제로 x()함수 호출
# p1.x = 100 # 속성에 직접 접근하듯 사용. 실제로 x(100)함수 호출
# p1.y = 200
# print(p1.x, p1.y)

# ====================================================
# class GetSetTest():
#     def __innit__(self):
#         self.__count=9

#     def count(self):
#         return self.__count
    
#     def count(self,value):
#         if value>0 and value<10:
#             self.__count=value
#         else:
#             print("0<count<10의 범위내에 있어야한대")

# if __name__=="__main__":
#     obj=GetSetTest()
#     print(obj.count)
#     obj.count=33
#     print(obj.count)
#     obj.count=7
#     print(obj.count)
#     print(obj.__GetSetTest__count)