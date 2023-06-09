# import copy

# # a = []*3
# # a.append(1)
# # a.append(2,3)
# # # a.append(3)
# # print(a)

# a = {'1반':[[4,2,3],2,3],'2반':[[1,4,3],3,2],'3반':[[1,2,3],8,6]}
# b = list(a.values())
# print(type(b))
# print(id(b))
# c = copy.deepcopy(b)
# c[0][0].append(250)
# d=c[:]
# print(id(c))
# print(id(d))
# d.append([3,4])
# del d[0]
# d[0].append(50)
# c[0].append(100)
# print(id(d[0]))
# print(id(c[0]))
# print(d)
# print(b)
# print(c)
# print(a)

# a = [1,2,3,4]
# b = []+a
# b.append(5)
# print(a)

""" 과목과 점수를 저장하는 클래스 """
class Subject:
    def __init__(self, subname='', score=-1):
        self.__subname = subname
        self.__score = score

    def set_subname(self, subname):
        self.__subname = subname

    def set_score(self, score):
        self.__score = score

    def get_subname(self):
        return self.__subname

    def get_score(self):
        return self.__score

    def __str__(self):
        return f'Subject[과목명:{self.__subname}, 점수:{self.__score}]'

# s0 = Subject('파이썬', 99)
# s1 = Subject()
# s1.set_subname('국어')
# s1.set_score(90)
# print(s0)
# print(s1)

""" 학생 한명의 정보를 저장하는 클래스. 
name은 학생이름 sublist는 과목객체의 리스트를 저장 """
class Student:
    def __init__(self, name=''):
        self.__name = name
        self.__sublist = []
    
    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_score(self, sc):
        self.__sublist.append(sc)
    
    def get_score(self, subname):
        for sc in self.__sublist:
            if sc.get_subname() == subname:
                return sc.get_score()

    def get_score_all(self):
        return self.__sublist.copy()

    def get_subsize(self):
        return len(self.__sublist)

    def get_total_score(self):
        total_score = 0
        for subinfo in self.__sublist:
            total_score += subinfo.get_score()
        return total_score

    def get_average(self):
        return self.get_total_score() / len(self.__sublist)


def print_sub_list(sub_list):
    for sub in sub_list:
        print(f'{sub.get_subname()}점수:{sub.get_score()}')

st1 = Student('이순신')
st1.set_score(Subject('국어', 95))
st1.set_score(Subject('영어', 80))
st1.set_score(Subject('수학', 56))
print(st1.get_total_score())
print(st1.get_average())
print(st1.get_score('영어'))
print(st1.get_subsize())
print_sub_list(st1.get_score_all())
print()

st2 = Student('임꺽정')
st2.set_score(Subject('국어', 78))
st2.set_score(Subject('영어', 69))
st2.set_score(Subject('수학', 34))
print(st2.get_total_score())
print(st2.get_average())
print(st2.get_score('영어'))
print(st2.get_subsize())
print_sub_list(st2.get_score_all())
print()

st3 = Student('장보고')
st3.set_score(Subject('국어', 76))
st3.set_score(Subject('영어', 91))
st3.set_score(Subject('수학', 99))

st4 = Student('김유신')
st4.set_score(Subject('국어', 56))
st4.set_score(Subject('영어', 99))
st4.set_score(Subject('수학', 89))

st5 = Student('장영실')
st5.set_score(Subject('국어', 100))
st5.set_score(Subject('영어', 99))
st5.set_score(Subject('수학', 100))

""" 한 반을 나타내는 클래스. 학생객체를 리스트로 저장. 학생의 성적 순위 리스트 저장."""
class Group:
    def __init__(self):
        self.__st_list = []
    
    def add(self, st):
        self.__st_list.append(st)
        self.__st_list.sort(key=lambda x:x.get_average(), reverse=True)
        self.__st_rank = []
        for i in range(1, len(self.__st_list)+1):
            self.__st_rank.append(i)

    def get_st_list(self):
        return self.__st_list

    def get_st_rank(self):
        return self.__st_rank

""" 한 반의 학생 정보를 출력하는 외부함수 """
def print_info(g):
    idx = 0
    for st in g.get_st_list():
        print(f'{st.get_name()}학생 성적 정보')
        print(f'반석차: {g.get_st_rank()[idx]}등')
        for sub in st.get_score_all():
            print(f'{sub.get_subname()}과목:{sub.get_score()}점')
        print(f'총점:{st.get_total_score()}')
        print(f'평균:{st.get_average():.2f}')
        idx += 1
        print()        

grp1 = Group() # 1반
grp1.add(st3) # 장보고
grp1.add(st2) # 임꺽정
grp1.add(st1) # 이순신
print_info(grp1)

grp2 = Group() # 2반
grp2.add(st4)
grp2.add(st5)
print_info(grp2)


# 전교 석차 정보
print('★전교에서★')

# 전교 학생 정보와 빈 석차 리스트를 받아 전교 석차를 구하는 함수
def total_rank(st_list, t_rank):
    idx = 0
    while idx < len(st_list):
        t_rank[idx] = 1
        for j in range(0, len(st_list)):
            if st_list[idx].get_average() < st_list[j].get_average():
               t_rank[idx] += 1 
        idx += 1

# 한 명의 학생 정보를 출력하는 외부 함수
def print_std(std):
    print(f'이름:{std.get_name()}')
    print_sub_list(std.get_score_all())
    print(f'총점:{std.get_total_score()}')
    print(f'평균:{std.get_average()}')

# 전교생 목록 만들기    
st_list = grp1.get_st_list() + grp2.get_st_list()
# 전교생의 석차를 저장하기 위한 리스트
t_rank = [1 for st in range(len(st_list))]

total_rank(st_list, t_rank)

# 전교생 정보 및 전체 석차 출력
idx = 0
while idx < len(st_list):
    print_std(st_list[idx])
    print(f'전교석차:{t_rank[idx]}')
    print()
    idx += 1