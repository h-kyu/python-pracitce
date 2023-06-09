# 반과 전교학생의 성적처리 프로그램
# 학급 수와 인원, 과목 개수는 변경 가능

class School():
    def __init__(self,classes=2,subjects=2):
        self._classes = classes
        self._students = []
        self._subjects = subjects
        self._students_name = {}
        self._subjects_title = []
    def get_subjects(self):
        return self._subjects
    def set_students_name(self):
        self._students=[]
        for j in range(self._classes):
            members = int(input(f"{j+1}반 학생 수: "))
            self._students.append(members)
        for i in range(self._classes):
            group=[]
            print(f"{i+1}반")
            for j in range(self._students[i]):
                name = input(f"{j+1}번째 학생이름 입력: ")
                group.append(name)
            self._students_name[f'{i+1}반'] = group
    def get_students_name(self):
        return self._students_name
    def set_subjects_title(self):
        for i in range(self._subjects):
            title = input(f"{i+1}번째 과목이름 입력: ")
            self._subjects_title.append(title)
    def get_subjects_title(self):
        return self._subjects_title

class Grades():
    def __init__(self,school):
        self._school = school
        self._all_score = {}
        self._school_rank = []
    def set_score(self):
        for i in range(self._school._classes):
            print(f'{i+1}반')
            stu_lst = []
            for j in self._school._students_name[f'{i+1}반']:
                stu_score_lst = []
                stu_score_lst.append(j)
                print(f'{j}')
                for k in self._school._subjects_title:
                    score=int(input(f'{k} 점수: '))
                    stu_score_lst.append(score)
                stu_lst.append(stu_score_lst)
            self._all_score[f'{i+1}반']=stu_lst
    def get_score(self):
        return self._all_score
    def set_class_rank(self):
        stu_score = list(self._all_score.values())
        for i in range(len(stu_score)):
            for j in range(self._school._students[i]):
                sum = 0
                for k in range(self._school._subjects):
                    sum+= stu_score[i][j][k+1]
                avg = round(sum/self._school._subjects,2)
                stu_score[i][j].append(sum)
                stu_score[i][j].append(avg)
        for i in range(len(stu_score)):
            stu_score[i].sort(key=lambda x:x[self._school._subjects+1],reverse=True)
            for j in range(self._school._students[i]):
                stu_score[i][j].append(j+1)
    def get_class_rank(self):
        return self._all_score
    def set_school_rank(self):
        stu_score = list(self._all_score.values())
        school_rank=[]
        for i in range(len(stu_score)):
            for j in stu_score[i]:
                school_rank.append(j)
        school_rank.sort(key=lambda x:x[self._school._subjects+1],reverse=True)
        for i in range(len(school_rank)):
            school_rank[i].append(i+1)
        self._school_rank = school_rank
    def get_rank(self):
        return self._school_rank
    def overview(self):
        self._school_rank.sort()
        tool = self._school
        print("이름\t",end='')
        for i in range(tool._subjects):
            print("{}\t".format(tool._subjects_title[i]),end='')
        print("총점\t평균\t반석차\t전교석차")
        for i in range(len(self._school_rank)):
            for j in self._school_rank[i]:
                print(f"{j}\t",end='')
            print()
    
info = School()
info._classes=2
info._subjects=3
info.set_students_name()
info.set_subjects_title()
rank = Grades(info)
rank.set_score()
rank.set_class_rank()
rank.set_school_rank()
rank.overview()

