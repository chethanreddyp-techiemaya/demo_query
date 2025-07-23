import pyodbc


def get_db_connection():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=34.123.45.67;'
        'DATABASE=master;'
        'UID=sqlserver;'
        'PWD=sqlserver12345;'
    )
    return conn
