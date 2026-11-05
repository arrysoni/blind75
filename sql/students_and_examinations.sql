-- LeetCode 1280: Students and Examinations
-- Runs as-is in SQLite, MySQL, or PostgreSQL.
-- Terminal: sqlite3 -header -column :memory: < students_and_examinations.sql

-- 1. Set up the tables
DROP TABLE IF EXISTS Examinations;
DROP TABLE IF EXISTS Subjects;
DROP TABLE IF EXISTS Students;

CREATE TABLE Students (
    student_id   INT PRIMARY KEY,
    student_name VARCHAR(50)
);

CREATE TABLE Subjects (
    subject_name VARCHAR(50) PRIMARY KEY
);

CREATE TABLE Examinations (
    student_id   INT,
    subject_name VARCHAR(50)
    -- no primary key: duplicates allowed
);

-- 2. Sample data (Example 1)
INSERT INTO Students (student_id, student_name) VALUES
    (1,  'Alice'),
    (2,  'Bob'),
    (13, 'John'),
    (6,  'Alex');

INSERT INTO Subjects (subject_name) VALUES
    ('Math'),
    ('Physics'),
    ('Programming');

INSERT INTO Examinations (student_id, subject_name) VALUES
    (1,  'Math'),
    (1,  'Physics'),
    (1,  'Programming'),
    (2,  'Programming'),
    (1,  'Physics'),
    (1,  'Math'),
    (13, 'Math'),
    (13, 'Programming'),
    (13, 'Physics'),
    (2,  'Math'),
    (1,  'Math');

-- 3. Solution
SELECT s.student_id, s.student_name, sub.subject_name,
       COUNT(e.subject_name) AS attended_exams
FROM Students s
CROSS JOIN Subjects sub
LEFT JOIN Examinations e
       ON e.student_id = s.student_id
      AND e.subject_name = sub.subject_name
GROUP BY s.student_id, s.student_name, sub.subject_name
ORDER BY s.student_id, sub.subject_name;

-- Expected output:
-- student_id | student_name | subject_name | attended_exams
-- 1          | Alice        | Math         | 3
-- 1          | Alice        | Physics      | 2
-- 1          | Alice        | Programming  | 1
-- 2          | Bob          | Math         | 1
-- 2          | Bob          | Physics      | 0
-- 2          | Bob          | Programming  | 1
-- 6          | Alex         | Math         | 0
-- 6          | Alex         | Physics      | 0
-- 6          | Alex         | Programming  | 0
-- 13         | John         | Math         | 1
-- 13         | John         | Physics      | 1
-- 13         | John         | Programming  | 1