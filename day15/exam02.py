class Goal:
    def __init__(self,count):
        self.__count=count
    @property
    def count(self):
        return self.__count
    @count.setter
    def count(self,count):
        self.__count=count

count1 = 0
count2 = 0
count3 = 0
countAll = 0
scores=0
while True:
    goal = int(input("골 입력(0:종료): "))
    if goal == 1 :
        count1+=1
    elif goal == 2:
        count2+=1
    elif goal == 3:
        count3+=1
    elif goal == 0:
        break
    if goal !=0 : 
        countAll+=1
        scores+=goal
a = Goal(count1)
b = Goal(count2)
c = Goal(count3)
d = Goal(countAll)
print("\t골\t점수")
print(f"1\t{a.count}\t{a.count}")
print(f"2\t{b.count}\t{2*b.count}")
print(f"3\t{c.count}\t{3*c.count}")
print(f"total\t{d.count}\t{scores}")

# class basketball:
#     def __init__(self,count):
#         self.count = count

        
#     def goal(self):
#         n=0
#         lis = []
#         def display(a,n,count):
#             print("    ","골    점수")
#             print(f"{n}    {a}      {count}")
#         while True:
#             a= int(input("골 입력(0:종료) :"))
#             if a == 0:
#                 print("       ","골    점수")
#                 print(f"total    {n}    {self.count}")
#                 break
#             elif a >= 4:
#                 print("3점 이하로 입력바랍니다")
#             else:
#                 n+=1
#                 self.count+=a
#                 lis.append(self.count)
#                 display(a,n,self.count)
        
    
# b = basketball(0)
# b.goal()
