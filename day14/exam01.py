# TV 클래스를 정의하시오
class TV:
    def __init__(self,brand):
        self.brand=brand
        self.power=False
        self.ch=0
        self.vol=0
    def powerOnOff(self):
        if self.power==True:
            self.power = False
        else:
            self.power = True
    def chUP(self):
        self.ch+=1
    def chDW(self):
        self.ch-=1
    def volUP(self):
        self.vol+=1
    def volDW(self):
        self.vol-=1
    def display(self):
        print(f"{self.brand} TV")
        if self.power == True:
            print(f"ch: {self.ch}")
            print(f"vol: {self.vol}")
            print("방송 중")
            print('--------------------')
        else:
            print("전원 꺼짐")
            print('--------------------')

# 위 클래스를 이용하여 두 대의 TV를 만들고 동작시키는 main작성
tv1 = TV('삼성')
tv1.power=True
tv1.ch=2
tv2 = TV('엘지')
tv1.display()
tv2.display()
tv2.powerOnOff()
tv1.chDW()
tv1.volUP()
tv1.volUP()
tv2.chUP()
tv2.chUP()
tv2.volUP()
tv1.display()
tv2.display()


















