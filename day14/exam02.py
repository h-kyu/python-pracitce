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

tv1 = TV('삼성')
tv2 = TV('엘지')
# tv1.volUP()
# tv1.chUP()
# tv1.powerOnOff()
# tv1.display()





# #TV클래스 정의

# class TV :
#     # 객체변수 brand, onoff, chanel, volume

#     # def __init__(self, brand, onoff = False, chanel = 0, volume = 0) :
#     #     self.brand = brand
#     #     self.onoff = onoff
#     #     self.chanel = chanel
#     #     self.valume = volume

#     def __init__(self, brand, onoff = None, chanel = None, volume = None) :
#         self.brand = brand

#         if onoff == None :
#             self.onoff = False
#         elif onoff == 'on' :
#             self.onoff = True
#         elif onoff == 'off' :
#             self.onoff = False
        
#         if chanel == None :
#             self.chanel = 0
#         elif type(chanel) == int :
#             self.chanel = chanel
#         else :
#             self.chanel = 0

#         if volume == None :
#             self.volume = 0
#         elif type(volume) == int :
#             self.volume = volume
#         else :
#             self.volume = 0
    
#     def powerOnOff(self) :
#         if self.onoff == False :
#             self.onoff = True
#         else :
#             self.onoff = False
    
#     def chUp(self) :
#         self.chanel += 1
    
#     def chDown(self) :
#         self.chanel -= 1

#     def volUp(self) :
#         self.volume += 1
    
#     def volDown(self) :
#         self.volume -= 1

#     def display(self) :
#         print(self.brand, 'TV')
#         if self.onoff == False :
#             print('전원꺼짐')
#             print('===========')
#         else :
#             print(f'ch : {self.chanel}')
#             print(f'vol : {self.volume}')
#             print('방송 중')
#             print('===========')

# tv1 = TV('삼성')
# tv2 = TV('엘지', 'on')

# tv1.display()
# tv2.display()

# tv1.powerOnOff()
# tv1.display()
# tv2.display()

# tv1.chUp()
# tv1.volUp()

# tv2.chDown()
# tv2.volUp()

# tv1.display()
# tv2.display()