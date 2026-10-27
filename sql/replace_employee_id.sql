/*
Replace Employee ID With The Unique Identifier
Easy

Table: Employees
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+
id is the primary key. Each row contains the id and the name of an employee.

Table: EmployeeUNI
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| unique_id     | int     |
+---------------+---------+
(id, unique_id) is the primary key. Each row contains the id and the
corresponding unique id of an employee.

Write a solution to show the unique ID of each employee. If an employee
does not have a unique ID, show null instead.

Return the result table in any order.

Example 1:
Input:
Employees:              EmployeeUNI:
+----+----------+       +----+-----------+
| id | name     |       | id | unique_id |
+----+----------+       +----+-----------+
| 1  | Alice    |       | 3  | 1         |
| 7  | Bob      |       | 11 | 2         |
| 11 | Meir     |       | 90 | 3         |
| 90 | Winston  |       +----+-----------+
| 3  | Jonathan |
+----+----------+

Output:
+-----------+----------+
| unique_id | name     |
+-----------+----------+
| null      | Alice    |
| null      | Bob      |
| 2         | Meir     |
| 3         | Winston  |
| 1         | Jonathan |
+-----------+----------+
*/

-- Pretty output settings (SQLite-only commands, they start with a dot)
.headers on
.mode column
.nullvalue null

-- ---------- Setup: build the tables (LeetCode does this for you) ----------
DROP TABLE IF EXISTS Employees;
DROP TABLE IF EXISTS EmployeeUNI;

CREATE TABLE Employees (
    id   INT PRIMARY KEY,
    name VARCHAR(20)
);

CREATE TABLE EmployeeUNI (
    id        INT,
    unique_id INT,
    PRIMARY KEY (id, unique_id)
);

INSERT INTO Employees (id, name) VALUES
    (1, 'Alice'),
    (7, 'Bob'),
    (11, 'Meir'),
    (90, 'Winston'),
    (3, 'Jonathan');

INSERT INTO EmployeeUNI (id, unique_id) VALUES
    (3, 1),
    (11, 2),
    (90, 3);

-- ---------- Your solution (this is the part you submit on LeetCode) ----------
SELECT eu.unique_id, e.name
FROM Employees e
LEFT JOIN EmployeeUNI eu
    ON e.id = eu.id;