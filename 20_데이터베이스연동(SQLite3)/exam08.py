import sqlite3

# 하나의 ROW를 표현하기 위한 클래스
# VO(Value Object): 값을 표현하는 클래스
# DTO(Data Transfer Object): 레이어 간 데이터 전송을 위해 정의하는 클래스
class InfoVO:
    def __init__(self, no=None, name=None, age=None, btype=None, birth=None):
        self.no = no
        self.name = name
        self.age = age
        self.btype = btype
        self.birth = birth

    def __str__(self):
        return f"InfoVO(no={self.no}, name={self.name}, age={self.age}, btype={self.btype}, birth={self.birth})"

# DAO(Data Access Object): 데이터베이스에 접근하여 조작하는 기능을 정의한 클래스
class InfoDAO:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()

    def create(self, vo):
        self.cursor.execute("INSERT INTO INFO (NAME, AGE, BTYPE, BIRTH) VALUES (?, ?, ?, ?)", (vo.name, vo.age, vo.btype, vo.birth))
        self.conn.commit()
        print("New row added.")

    def read_all(self):
        self.cursor.execute("SELECT * FROM INFO")
        rows = self.cursor.fetchall()
        result = []
        for row in rows:
            vo = InfoVO(*row)
            result.append(vo)
        return result

    def read_by_no(self, no):
        self.cursor.execute("SELECT * FROM INFO WHERE NO=?", (no,))
        row = self.cursor.fetchone()
        if row:
            vo = InfoVO(*row)
            return vo
        else:
            return None

    def read_by_name(self, name):
        self.cursor.execute("SELECT * FROM INFO WHERE NAME=?", (name,))
        rows = self.cursor.fetchall()
        result = []
        for row in rows:
            vo = InfoVO(*row)
            result.append(vo)
        return result

    def update(self, vo):
        self.cursor.execute("UPDATE INFO SET NAME=?, AGE=?, BTYPE=?, BIRTH=? WHERE NO=?", (vo.name, vo.age, vo.btype, vo.birth, vo.no))
        self.conn.commit()
        print(f"Row with NO={vo.no} updated.")

    def delete(self, no):
        self.cursor.execute("DELETE FROM INFO WHERE NO=?", (no,))
        self.conn.commit()
        print(f"Row with NO={no} deleted.")


# 데이터베이스 연결
conn = sqlite3.connect('example.db')

# cursor 생성
cursor = conn.cursor()

# 테이블 생성
cursor.execute("""DROP TABLE IF EXISTS info""")

cursor.execute("""
    CREATE TABLE INFO (
    NO INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME TEXT(20) NOT NULL,
    AGE INTEGER CHECK (1 < AGE AND AGE < 120),
    BTYPE TEXT(2),
    BIRTH TEXT
);
""")

dao = InfoDAO(conn)

# 데이터 추가
dao.create(InfoVO(-1, 'John', 30, 'A', '1993-01-01'))

# 데이터 조회
rows = dao.read_all()
for row in rows:
        print(row)

# 데이터 수정
dao.update(InfoVO(1, 'Jane', 25, 'B', '1998-02-01'))

# 수정된 데이터 조회
rows = dao.read_by_name('Jane')
for row in rows:
    print(row)

# 데이터 삭제
dao.delete(1)

# 삭제된 데이터 조회
print(dao.read_by_no(1))

# cursor 닫기
cursor.close()

# 데이터베이스 연결 닫기
conn.close()
