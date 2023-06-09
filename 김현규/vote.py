# 설문조사 애플리케이션 만들어 보기
# 설문 주제 자유
# 데이터베이스 연동 필수

import sqlite3

class VoteVO:
    def __init__(self, genre=None):
        self.genre = genre
    def __str__(self):
        return f"{self.genre}"
    
class VoteDAO:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()

    def create(self, vo):
        self.cursor.execute("INSERT INTO VOTE (GENRE, VOTES) VALUES (?,?)", (vo.genre,0))
        self.conn.commit()
        print("새로운 장르가 추가되었습니다.")
    def show_vote_list(self):
        self.cursor.execute("SELECT VOTE.ID, VOTE.GENRE FROM VOTE")
        rows = self.cursor.fetchall()
        return rows
    def show_vote_result(self):
        self.cursor.execute("SELECT * FROM VOTE")
        rows = self.cursor.fetchall()
        return rows
    def vote_count_id(self, id):
        self.cursor.execute("SELECT ID FROM VOTE")
        rows = self.cursor.fetchall()
        result=[]
        for row in rows:
            vo = row[0]
            result.append(vo)
        if id in result:
            self.cursor.execute("SELECT VOTES FROM VOTE WHERE ID=?",(id,))
            num = self.cursor.fetchone()
            num = num[0] + 1
            self.cursor.execute("UPDATE VOTE SET VOTES=? WHERE ID=?",(num,id))
            print("설문 완료")
            conn.commit()
        else:
            print('잘못 입력하셨습니다')
    def vote_count_genre(self, genre):
        self.cursor.execute("SELECT VOTES FROM VOTE WHERE GENRE=?",(genre,))
        num = self.cursor.fetchone()
        num = num[0] + 1
        self.cursor.execute("UPDATE VOTE SET VOTES=? WHERE GENRE=?",(num,genre))
        conn.commit()    

        
        
conn = sqlite3.connect('vote.db')
cursor = conn.cursor()

cursor.execute("""DROP TABLE IF EXISTS vote""")

cursor.execute("""
    CREATE TABLE VOTE (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    GENRE TEXT NOT NULL,
    VOTES INTEGER 
);
""")

dao = VoteDAO(conn)

# 기본 세팅
def setting(genre):
    cursor.execute("INSERT INTO VOTE (GENRE, VOTES) VALUES (?,?)", (genre,0)) 
setting("판타지")
setting("멜로")
setting("액션")
setting("느와르")   


while True:
    print("┌"+"─"*35+"┐")
    print("\n 좋아하는 영화 장르 종류 설문조사\n\n 1.설문 참여하기\n 2.설문 현황보기\n\n (이 외에 다른 숫자 입력 시 종료)\n")
    print("└"+"─"*35+"┘")
    try:
        choice = int(input("선택: "))
        if choice == 1 :
            rows = dao.show_vote_list()
            print("┌"+"─"*20+"┐")
            for row in rows:
                print(f'  {row[0]}. {row[1]}\n')
            print('  0. 기타(직접입력)')
            print("└"+"─"*20+"┘")
            try:
                setup = int(input("선택: "))
                if 0 < setup:
                    dao.vote_count_id(setup)
                elif setup == 0:
                    new_genre=input("영화 장르 입력: ")
                    dao.create(VoteVO(new_genre))
                    dao.vote_count_genre(new_genre)
                    print("설문 완료")
            except:
                print("숫자를 입력해주세요")
        elif choice == 2 :
            rows = dao.show_vote_result()
            print("┌"+"─"*20+"┐")
            for row in rows:
                print(f'  {row[0]}. {row[1]} ==> {row[2]}\n')
            print("└"+"─"*20+"┘")
        else:
            print("설문을 종료합니다")
            break
    except:
        print("숫자를 입력해주세요")

cursor.close()
conn.close()