USE library_db;

-- Authors
INSERT INTO Authors (name, country) VALUES
('J.K. Rowling', 'UK'),
('George Orwell', 'UK'),
('Chinua Achebe', 'Nigeria'),
('Haruki Murakami', 'Japan');

-- Books
INSERT INTO Books (title, author_id, isbn, published_year, available_copies) VALUES
('Harry Potter and the Sorcerer''s Stone', 1, '9780439708180', 1997, 5),
('1984', 2, '9780451524935', 1949, 3),
('Animal Farm', 2, '9780451526342', 1945, 4),
('Things Fall Apart', 3, '9780385474542', 1958, 2),
('Norwegian Wood', 4, '9780375704024', 1987, 3);

-- Members
INSERT INTO Members (name, email) VALUES
('Alice Sharma', 'alice.sharma@example.com'),
('Rahul Verma', 'rahul.verma@example.com'),
('Priya Nair', 'priya.nair@example.com');

-- Loans
INSERT INTO Loans (book_id, member_id, loan_date, return_date) VALUES
(1, 1, '2025-01-10', '2025-01-24'),
(2, 2, '2025-02-05', NULL),
(3, 1, '2025-02-15', '2025-03-01'),
(4, 3, '2025-03-01', NULL);
