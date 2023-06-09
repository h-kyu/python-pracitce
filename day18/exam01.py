# 다중 상속 개념
class 동물:
    def 먹는다(self):
        pass
    def 움직인다(self):
        pass
    def 호흡한다(self):
        pass
    def 소리낸다(self):
        pass

#공통 특성 정의
class 물에서생활하는동물:
    def 물에서생활(self):
        print('물에서 헤엄친다.')

class 포유류(동물):
    def 호흡한다(self):
        print('폐 호흡')

class 어류(동물):
    def 호흡한다(self):
        print('아가미 호흡')

class 개(포유류):
    def 먹는다(self):
        print('개같이 먹는다.')
    def 움직인다(self):
        print('개같이 움직인다.')
    def 소리낸다(self):
        print('개같이 소리낸다.')
    def 개특징(self):
        print('개만 가지는 특징')

class 고양이(포유류):
    def 먹는다(self):
        print('고양이같이 먹는다.')
    def 움직인다(self):
        print('고양이같이 움직인다.')
    def 소리낸다(self):
        print('고양이같이 소리낸다.')
    def 고양이특징(self):
        print('고양이만 가지는 특징')

class 고래(포유류, 물에서생활하는동물): # 다중상속
    def __init__(self, n):
        self.n = n
    def 먹는다(self):
        print(id(self.n), '고래같이 먹는다.')
    def 움직인다(self):
        print(id(self.n), '고래같이 움직인다.')
    def 소리낸다(self):
        print(id(self.n), '고래같이 소리낸다.')
    def 고래특징(self):
        print(id(self.n), '고래만 가지는 특징')
    def 물에서생활(self):
        super().물에서생활()
        print(id(self.n), '호흡하러 수면위로 다닌다.')

class 상어(어류, 물에서생활하는동물): # 다중상속
    def 먹는다(self):
        print('상어같이 먹는다.')
    def 움직인다(self):
        print('상어같이 움직인다.')
    def 소리낸다(self):
        print('상어같이 소리낸다.')
    def 상어특징(self):
        print('상어만 가지는 특징')

animals = [고래(111), 상어(), 고래(222)]


for a in animals:
    a.먹는다()
    a.소리낸다()
    a.먹는다()
    a.호흡한다()
    a.물에서생활()
    print()