import psycopg2

connection = psycopg2.connect('dbname=example')

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS table2')

cursor.execute('''
  create TABLE table2 (
    id INTEGER PRIMARY KEY,
    completed BOOLEAN NOT NULL DEFAULT False
  )
''')

cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s)', (1, True))

cursor.execute('INSERT INTO table2 (id, completed) VALUES (%(id)s, %(completed)s)', {
               'id': 2, 'completed': False})

cursor.execute('SELECT * from table2')

result = cursor.fetchone()
print(result[0]+1)

connection.commit()

connection.close()
cursor.close()
