# MySQL Database Testing Project 🧪

Automated test suite for a **Library Management System** database, built to practice real-world database testing: schema validation, data integrity checks, and constraint enforcement — using **MySQL + Python + pytest**.

## 📌 What This Project Covers

- Designing a relational schema with primary keys, foreign keys, unique constraints, and defaults
- Seeding realistic sample data
- Writing manual SQL test queries to understand what "passing" and "failing" mean at the data layer
- Automating those checks into a repeatable **pytest** suite
- Generating an HTML test report

## 🗂️ Schema

4 related tables: `Authors` → `Books` → `Loans` ← `Members`

- **Authors**: `author_id (PK)`, `name`, `country`
- **Books**: `book_id (PK)`, `title`, `author_id (FK)`, `isbn (UNIQUE)`, `published_year`, `available_copies`
- **Members**: `member_id (PK)`, `name`, `email (UNIQUE, NOT NULL)`, `join_date`
- **Loans**: `loan_id (PK)`, `book_id (FK)`, `member_id (FK)`, `loan_date`, `return_date`

## 🧪 Test Categories

| Category | Examples |
|---|---|
| Schema Tests | Correct tables/columns exist |
| Data Validation | No NULLs, no duplicate emails, no orphan records |
| Constraint Enforcement | Duplicate emails, invalid foreign keys, and missing required fields are correctly **rejected** |

Full test case list and explanations are in [`Database_Testing_Project_Documentation.docx`](./Database_Testing_Project_Documentation.docx).

## ⚙️ Setup

```bash
# 1. Create the database
mysql -u root -p
SOURCE schema.sql;
SOURCE seed_data.sql;

# 2. Install Python dependencies
pip install pytest mysql-connector-python pytest-html

# 3. Set your MySQL password in conftest.py

# 4. Run the tests
python -m pytest -v
python -m pytest --html=report.html --self-contained-html
```

## 📁 Project Structure

```
db-testing-project/
├── schema.sql
├── seed_data.sql
├── conftest.py
├── test_schema.py
├── test_data_validation.py
├── test_constraints.py
└── README.md
```

## 🔧 Tech Stack

MySQL 8.0 · Python 3 · pytest · mysql-connector-python

## 🚀 Planned Enhancements

- GitHub Actions CI pipeline (MySQL service container + automated test runs on every push)
- Performance testing on larger datasets
- Stored procedure / trigger testing

---
*Built as a hands-on learning project to practice database QA fundamentals.*
