import sqlite3

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

# CREATE
def create_info(name, age, btype, birth):
    cursor.execute("INSERT INTO INFO (NAME, AGE, BTYPE, BIRTH) VALUES (?, ?, ?, ?)", (name, age, btype, birth))
    conn.commit()
    print("New row added.")

# READ
def read_info():
    cursor.execute("SELECT * FROM INFO")
    return cursor.fetchall()

# READ
def read_info_no(no):
    cursor.execute("SELECT * FROM INFO WHERE NO=?", (no,))
    return cursor.fetchall()

# READ
def read_info_name(name):
    cursor.execute("SELECT * FROM INFO WHERE NAME=?", (name,))
    return cursor.fetchall()


# UPDATE
def update_info(no, name, age, btype, birth):
    cursor.execute("UPDATE INFO SET NAME=?, AGE=?, BTYPE=?, BIRTH=? WHERE NO=?", (name, age, btype, birth, no))
    conn.commit()
    print(f"Row with NO={no} updated.")

# DELETE
def delete_info(no):
    cursor.execute("DELETE FROM INFO WHERE NO=?", (no,))
    conn.commit()
    print(f"Row with NO={no} deleted.")

# 데이터 추가
create_info('John', 30, 'A', '1993-01-01')

# 데이터 조회
rows = read_info()
for row in rows:
        print(row)

# 데이터 수정
update_info(1, 'Jane', 25, 'B', '1998-02-01')

# 수정된 데이터 조회
print(read_info_name('Jane'))

# 데이터 삭제
# delete_info(1)

# 삭제된 데이터 조회
print(read_info_no(1))

# cursor 닫기
cursor.close()

# 데이터베이스 연결 닫기
conn.close()
