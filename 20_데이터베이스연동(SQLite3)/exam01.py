import sqlite3

# 데이터베이스 연결
conn = sqlite3.connect('example.db')

# 커서 생성
cursor = conn.cursor()

# users 테이블 생성
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
""")

# 커밋
conn.commit()

# 커서와 연결 닫기
cursor.close()
conn.close()
