# class Counter:
#     def __init__(self, count = 0, interval = 1):
#         self.__count = count
#         self.__interval = interval
#     def increment(self):
#         self.count += self.interval
#     @property
#     def count(self):
#         return self.__count
#     @property
#     def interval(self):
#         return self.__interval
#     @count.setter
#     def count(self, count):
#         self.__count = count
#     @interval.setter
#     def interval(self, interval):
#         self.__interval = interval
#     def init(self):
#         self.count = 0
#         self.interval = 1
#     def __str__(self):
#         return f'count={self.__count},interval={self.__interval}'

# # 카운트 객체 테스트
# # cnt1 = Counter()
# # cnt1.increment()
# # cnt1.increment()
# # print(cnt1.count)    
# # cnt1.init()
# # cnt1.increment()
# # cnt1.increment()
# # print(cnt1.count)    
# # cnt1.count = 10
# # print(cnt1.count)    
# # cnt1.interval = 2
# # cnt1.increment()
# # print(cnt1.count)    

# class BasketCounter:
#     def __init__(self):
#         self.__goal = [
#             Counter(),
#             Counter(),
#             Counter(),
#             Counter()
#         ]
#         self.__score = [
#             Counter(),
#             Counter(count=0, interval=2),
#             Counter(count=0, interval=3),
#             Counter()
#         ]
    
#     def goalin(self, goal):
#         goal -= 1
#         if 0 <= goal <= 3:
#             self.__goal[goal].increment()
#             self.__goal[3].increment()
#             self.__score[goal].increment()
#             self.__score[3].interval = goal+1
#             self.__score[3].increment()

#     @property
#     def goal(self):
#         return self.__goal

#     @property
#     def score(self):
#         return self.__score


# # 게임 시작
# team1 = BasketCounter()

# # 골인
# team1.goalin(1)
# team1.goalin(1)
# team1.goalin(2)
# team1.goalin(3)
# team1.goalin(2)
# team1.goalin(3)
# team1.goalin(2)

# goal = team1.goal
# score = team1.score

# # for g,s in zip(goal, score):
# #     print(f'{s.interval}점슛 골:{g.count}개, 점수:{s.count}')

# for i in range(3):
#     print(f'{score[i].interval}점슛 골:{goal[i].count}개, 점수:{score[i].count}')
# print(f'합계 골:{goal[3].count}개, 점수:{score[3].count}')


#농구 점수 계산기 만들기(클래스를 이용)
#캡슐화, 은닉화, 생성자, self 이용하기
#생성자를 이용해서 count값 초기화하기(0 또는 임의 값으로 초기화)
#Getter, Seteer 사용하여 사용자 임의로 초기화가 가능하도록 작성
#<기능> 1,2,3점 메뉴 입력 시 해당 골 과 득점 입력
#각각 골의 수와 총 골의 수 개별 누적
#프로그램 종료 시(경기종료) 총점과 총 골 수 출력
#출력 모양은 자유!

class BasketballScoreCalculator:
    def __init__(self, count=0):
        self._count = count
        self._score = 0
        self._one_point_goals = 0
        self._two_point_goals = 0
        self._three_point_goals = 0
    
    def add_goal(self, goal, points):
        if goal == 1:
            self._one_point_goals = points
        elif goal == 2:
            self._two_point_goals = points
        elif goal == 3:
            self._three_point_goals = points
        else:
            print("1~3점 슛까지만 넣을수있습니다!")
            return
        
        self._score += points
        self._count += 1
    
    def get_total_score(self):
        return self._score
    
    def get_total_goals(self):
        return (self._one_point_goals + (self._two_point_goals * 2) + (self._three_point_goals * 3))
    
    def set_count(self, count):
        self._count = count
    
    def get_count(self):
        return self._count
    
    def set_score(self, score):
        self._score = score
    
    def get_score(self):
        return self._score
    
    def set_one_point_goals(self, goals):
        self._one_point_goals = goals
    
    def get_one_point_goals(self):
        return self._one_point_goals
    
    def set_two_point_goals(self, goals):
        self._two_point_goals = goals
    
    def get_two_point_goals(self):
        return self._two_point_goals
    
    def set_three_point_goals(self, goals):
        self._three_point_goals = goals
    
    def get_three_point_goals(self):
        return self._three_point_goals

if __name__ == '__main__':
    calc = BasketballScoreCalculator()
    
    while True:
        print("┌─────┐─────┐─────┐")
        print("│     │  골 │ 점수│")
        print("└─────┘─────┘─────┘")
        print(f"│  1  │   {calc.get_one_point_goals()} │   {calc.get_one_point_goals()} │")
        print(f"│  2  │   {calc.get_two_point_goals()} │   {calc.get_two_point_goals() * 2} │")
        print(f"│  3  │   {calc.get_three_point_goals()} │   {calc.get_three_point_goals() * 3} │")
        print("┌─────┐─────┐─────┐")
        print(f"│total│   {calc.get_total_score()} │   {calc.get_total_goals()} │")
        print("└─────┘─────┘─────┘")

        goal = int(input("1~3중 골 입력(0: 종료): "))
        if goal == 0:
            break
        
        points = int(input("골 입력: "))
        calc.add_goal(int(goal), points)
        
print("Game over!")
print("총 골수: {}".format(calc.get_total_score()))
print("총 점수: {}".format(calc.get_total_goals()))
