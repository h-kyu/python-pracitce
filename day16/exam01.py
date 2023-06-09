# 말하는 인형과 건전지 구현(클래스와 객체의 이해)

class Doll():
    def __init__(self):
        self._voice = None
        self._battery = None
    def insert_battery(self,battery):
        self._battery = battery
    def get_battery(self):
        return self._battery
    def remove_battery(self):
        removed_battery = self._battery
        self._battery=None
        return removed_battery
    @property
    def get_voice(self):
        return self._voice
    def set_voice(self):
        if self._battery._volume >= 15:
            self._voice = input(f"저장할 음성을 입력하세요: ")    
            print("저장되었습니다!")
            self._battery._volume-=15        
        else:
            print(f"{self._battery._brand}에 전기가 읎다")
    def prt_voice(self):
        if self._battery == None:
            print("건전지 없음")
        elif self._battery._volume >= 10:
            if self._voice == None:
                print("녹음된 메시지가 없습니다.")
            else:
                print(f"{self._voice}") 
            self._battery._volume-=10      
        else:
            print(f"{self._battery._brand}에 전기가 읎다")
        


class Battery():
    def __init__(self, brand,size,volume,volt):
        self._brand=brand
        self._size=size
        self._volume=volume
        self._volt=volt
    def get_charge(self):
        return self._volume
    def set_charge(self,volume):
        self._volume = volume
    def show_info(self):
        return f'\n제조사: {self._brand}\n크기: {self._size}\n용량:{self._volume}\n전압:{self._volt}'


horse = Doll()
horse.insert_battery(Battery("Bexel",'AAA',100,10))

a=horse.get_battery()
print("배터리 정보", a.show_info())

horse.prt_voice()
horse.set_voice()
horse.prt_voice()
print("남은 배터리: ", a.get_charge())

horse.prt_voice()
horse.prt_voice()
print("남은 배터리: ", a.get_charge())

horse.prt_voice()
horse.prt_voice()
print("남은 배터리: ", a.get_charge())

horse.prt_voice()
horse.prt_voice()
horse.prt_voice()

removed_battery = horse.remove_battery()
print("꺼낸 전지 용량: ",removed_battery.get_charge())

horse.prt_voice()

batt = Battery("energy",'AA',10,10)
horse.insert_battery(batt)

b=horse.get_battery()
print("배터리 정보", b.show_info())
horse.set_voice()
horse.prt_voice()
horse.prt_voice()


