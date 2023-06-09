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
    def volUP(self):
        self.vol+=1
    def display(self):
        if self.power == True:
            print(f"{self.brand} TV")
            print(f"ch: {self.ch}")
            print(f"vol: {self.vol}")
            print("방송중")
            print("-------------------------")
        else:
            print("방송중이지 않습니다")
            print("-------------------------")

class Remote():   
    def __init__(self,tv):
        self.tv=tv
    def powerOnOff(self):
        if self.tv.power==True:
            self.tv.power = False
        else:
            self.tv.power = True

    def chUP(self):
        self.tv.chUP()
    def chDW(self):
        self.tv.chDW()
    def volUP(self):
        self.tv.volUP()
    def volDW(self):
        self.tv.DW()
    def display(self):
        self.tv.display()
tv1 = TV('삼성')
tv2 = TV('엘지')
samsung = Remote(tv1)
lg = Remote(tv2)
samsung.display()
lg.display()

samsung.powerOnOff()
samsung.chUP()
lg.powerOnOff()
lg.volUP()
samsung.display()
lg.display()


