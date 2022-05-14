import pymysql

con = pymysql.connect(host='localhost',
                      user='python',
                      password='python',
                      database='pythondb',
                      charset='utf8mb4',
                      cursorclass=pymysql.cursors.DictCursor)
try:
    with con.cursor() as cur:
        cur.execute('SELECT VERSION()')
        version = cur.fetchone()
        print(f'Database version: {version["VERSION()"]}')
finally:
    con.close()
