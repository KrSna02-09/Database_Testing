import pytest
import mysql.connector
from mysql.connector import errors


def test_duplicate_email_rejected(db_connection, db_cursor):
    with pytest.raises(mysql.connector.errors.IntegrityError):
        db_cursor.execute(
            "INSERT INTO Members (name, email) VALUES (%s, %s);",
            ("Fake User", "alice.sharma@example.com")
        )
        db_connection.commit()

def test_invalid_book_fk_rejected(db_connection, db_cursor):
    with pytest.raises(mysql.connector.errors.IntegrityError):
        db_cursor.execute(
            "INSERT INTO Loans (book_id, member_id, loan_date) VALUES (%s, %s, %s);",
            (999, 1, "2025-04-01")
        )
        db_connection.commit()

def test_missing_email_rejected(db_connection, db_cursor):
    with pytest.raises(errors.Error):
        db_cursor.execute(
            "INSERT INTO Members (name) VALUES (%s);",
            ("No Email Guy",)
        )
        db_connection.commit()