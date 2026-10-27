/*
197. Rising Temperature
Easy

Table: Weather
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| recordDate    | date    |
| temperature   | int     |
+---------------+---------+
id is the column with unique values for this table.
There are no different rows with the same recordDate.
This table contains information about the temperature on a certain day.

Write a solution to find all dates' id with higher temperatures compared to
its previous dates (yesterday).

Return the result table in any order.

Example 1:
Input:
Weather table:
+----+------------+-------------+
| id | recordDate | temperature |
+----+------------+-------------+
| 1  | 2015-01-01 | 10          |
| 2  | 2015-01-02 | 25          |
| 3  | 2015-01-03 | 20          |
| 4  | 2015-01-04 | 30          |
+----+------------+-------------+

Output:
+----+
| id |
+----+
| 2  |
| 4  |
+----+

Explanation:
In 2015-01-02, the temperature was higher than the previous day (10 -> 25).
In 2015-01-04, the temperature was higher than the previous day (20 -> 30).
*/

-- Pretty output settings (SQLite-only commands, they start with a dot)
.headers on
.mode column
.nullvalue null

-- ---------- Setup: build the table (LeetCode does this for you) ----------
DROP TABLE IF EXISTS Weather;

CREATE TABLE Weather (
    id          INT PRIMARY KEY,
    recordDate  DATE,
    temperature INT
);

INSERT INTO Weather (id, recordDate, temperature) VALUES
    (1, '2015-01-01', 10),
    (2, '2015-01-02', 25),
    (3, '2015-01-03', 20),
    (4, '2015-01-04', 30);

-- ---------- Your solution ----------
-- Self-join: compare each day ("today") with the row exactly one day earlier ("yesterday").
--
-- SQLite has no DATEDIFF, so this local version uses julianday() instead.
-- On LeetCode (MySQL), submit this version:
--
--   SELECT today.id
--   FROM Weather today
--   JOIN Weather yesterday
--       ON DATEDIFF(today.recordDate, yesterday.recordDate) = 1
--   WHERE today.temperature > yesterday.temperature;

SELECT today.id
FROM Weather today
JOIN Weather yesterday
    ON julianday(today.recordDate) - julianday(yesterday.recordDate) = 1
WHERE today.temperature > yesterday.temperature;