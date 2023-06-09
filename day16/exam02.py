# # 5명의 이름과 나이를 저장하고 출력하는 프로그램 자성
# # 한 번에 다섯 명의 정보를 저장하고 출력한다

# class Person:
#     def __init__(self, name, age, person):
#         self.name = name
#         self.age = age
#         self.person = person

# people = []
# for i in range(5):
#     print(f'{i+1}번째 정보 입력')
#     name = input('이름: ')
#     age = int(input('나이: '))
#     person = (f"{i+1}정보\n이름: {name}, 나이: {age}")
#     people.append(Person(name, age, person))

# for person in sorted(people, key=lambda p: p.age):
#     print(f"{person.person}")

class Person:
    def __init__(self, name='', age=0):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        self.__age = age

    def __str__(self):
        return f'Person[name={self.name}, age={self.age}]'

#Person객체 사용하기
p1 = Person()
p1.name = '이순신'
p1.age = 32
p2 = Person('홍길동', 20)
print(p1)
print(p2)
print()

class PersonManager:
    def __init__(self, size = 5):
        self.size = size
        self.pl = {}
        self.no = 0
    
    def insert(self, ps):
        if len(self.pl) == self.size:
            return
        if isinstance(ps, Person):
            self.pl.__setitem__(self.no, ps)
            self.no += 1
    
    def select(self, no):
        return self.pl.get(no)

    def sorted(self):
        return sorted(self.pl.items(), key=lambda x:x[1].age, reverse=True)

#Person 타입의 객체를 관리하는 클래스 사용 예시
pm = PersonManager()

pm.insert(Person('이순신', 20))
pm.insert(Person('홍길동', 30))
pm.insert(Person('임꺽정', 15))
pm.insert(Person('김좌진', 33))
pm.insert(Person('장보고', 27))
pm.insert(Person('김구', 10))

for ps in range(0, 10):
    if ps != None:
        print(pm.select(ps))

print()

for ps in pm.sorted():
    print(ps[1])