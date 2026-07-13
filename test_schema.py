def test_all_tables_exist(db_cursor):
    db_cursor.execute("SHOW TABLES;")
    tables = [row[0] for row in db_cursor.fetchall()]
    expected = {"Authors", "Books", "Members", "Loans"}
    assert expected.issubset(set(tables))

def test_all_tables_exist(db_cursor):
    db_cursor.execute("SHOW TABLES;")
    tables = [row[0].lower() for row in db_cursor.fetchall()]
    expected = {"authors", "books", "members", "loans"}
    assert expected.issubset(set(tables))