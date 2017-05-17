import pymssql
with pymssql.connect(server='0.0.0.0', user='user', password='password', database='database') as conn:
    with conn.cursor(as_dict=True) as cursor:
        cursor.execute("""
        IF OBJECT_ID('tblPython', 'U') IS NOT NULL
        DROP TABLE tblPython
        CREATE TABLE tblPython (
        ID INT IDENTITY(1,1) CONSTRAINT pk_tblPython_id PRIMARY KEY,
        Name VARCHAR(100),
        SSO VARCHAR(100),
        )
        """)
        print('Table Created')
    with conn.cursor(as_dict=True) as cursor:
        cursor.executemany(
        "INSERT INTO tblPython VALUES (%s, %s)",
        [('Anitha', '121212'),
        ('Hari', '123134'),
        ('Surya','125454')])
        conn.commit()
        print('DATA INSERTED')
    with conn.cursor(as_dict=True) as cursor:
        cursor.execute('SELECT * FROM tblPython')
        print('Reading Table Data')
        for row in cursor:
            print("ID=%d, Name=%s, SSO=%s" % (row['ID'], row['Name'], row['SSO']))
    with conn.cursor(as_dict=True) as cursor:
        cursor.execute('DELETE FROM tblPython WHERE ID=%d','1')
        conn.commit()
        print('Deleted record of ID=1')
    with conn.cursor(as_dict=True) as cursor:
        cursor.execute('SELECT * FROM tblPython')
        print('Reading Table Data')
        for row in cursor:
            print("ID=%d, Name=%s, SSO=%s" % (row['ID'], row['Name'], row['SSO']))
    with conn.cursor(as_dict=True) as cursor:
        cursor.execute("UPDATE tblPython SET SSO='111111' WHERE ID=2")
        conn.commit()
        print('UPDATED SSO OF ID=2')
    with conn.cursor(as_dict=True) as cursor:
        cursor.execute('SELECT * FROM tblPython')
        print('Reading Table Data')
        for row in cursor:
            print("ID=%d, Name=%s, SSO=%s" % (row['ID'], row['Name'], row['SSO']))
