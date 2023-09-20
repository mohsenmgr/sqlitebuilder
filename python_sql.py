import sqlite3

conn = sqlite3.connect('sqlite_database.db')
cursor = conn.cursor()


cursor.execute('SELECT id, name FROM lines where name not in ("STAB_PRELIEVO","STAB_CESSIONE")')
lines_records = cursor.fetchall()


cursor.execute('SELECT id,mname FROM my_measures where id not in (1,2,60,61)')
my_measures_records = cursor.fetchall()

iid = 1

for line_id,line_name in lines_records:
    for my_measure_id, *_ in my_measures_records:
        cursor.execute('INSERT INTO line_measures VALUES (?,?,?)',(iid,line_id,my_measure_id))
        iid = iid + 1
        conn.commit()


conn.close()