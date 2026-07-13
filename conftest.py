import pytest
import mysql.connector

@pytest.fixture
def db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="krishna",   # replace with your MySQL root password
        database="library_db"
    )
    yield conn
    conn.close()

@pytest.fixture
def db_cursor(db_connection):
    cursor = db_connection.cursor()
    yield cursor
    cursor.close()