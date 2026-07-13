def test_no_null_member_names_or_emails(db_cursor):
    db_cursor.execute("SELECT * FROM Members WHERE name IS NULL OR email IS NULL;")
    assert db_cursor.fetchall() == []

def test_no_duplicate_emails(db_cursor):
    db_cursor.execute("""
        SELECT email, COUNT(*) FROM Members GROUP BY email HAVING COUNT(*) > 1;
    """)
    assert db_cursor.fetchall() == []

def test_no_orphan_loans_book(db_cursor):
    db_cursor.execute("SELECT * FROM Loans WHERE book_id NOT IN (SELECT book_id FROM Books);")
    assert db_cursor.fetchall() == []

def test_no_orphan_loans_member(db_cursor):
    db_cursor.execute("SELECT * FROM Loans WHERE member_id NOT IN (SELECT member_id FROM Members);")
    assert db_cursor.fetchall() == []