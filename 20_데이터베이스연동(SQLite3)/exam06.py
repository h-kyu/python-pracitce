import sqlite3

conn = sqlite3.connect('example.db') # 데이터베이스 연결
cursor = conn.cursor() # 커서 생성

try:
    # users 테이블에서 모든 데이터 가져오기
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    # 결과 출력
    for row in rows:
        print(row)
except Exception as e:
    print(e)
finally:
    # 커서와 연결 닫기
    cursor.close()
    conn.close()

