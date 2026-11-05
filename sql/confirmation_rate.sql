-- LeetCode 1934: Confirmation Rate
-- Runs in SQLite, MySQL, or PostgreSQL.

-- 1. Set up the tables
DROP TABLE IF EXISTS Confirmations;
DROP TABLE IF EXISTS Signups;

CREATE TABLE Signups (
    user_id    INT PRIMARY KEY,
    time_stamp DATETIME
);

CREATE TABLE Confirmations (
    user_id    INT,
    time_stamp DATETIME,
    action     VARCHAR(10),   -- 'confirmed' or 'timeout'
    PRIMARY KEY (user_id, time_stamp)
);

-- 2. Sample data (Example 1)
INSERT INTO Signups (user_id, time_stamp) VALUES
    (3, '2020-03-21 10:16:13'),
    (7, '2020-01-04 13:57:59'),
    (2, '2020-07-29 23:09:44'),
    (6, '2020-12-09 10:39:37');

INSERT INTO Confirmations (user_id, time_stamp, action) VALUES
    (3, '2021-01-06 03:30:46', 'timeout'),
    (3, '2021-07-14 14:00:00', 'timeout'),
    (7, '2021-06-12 11:57:29', 'confirmed'),
    (7, '2021-06-13 12:58:28', 'confirmed'),
    (7, '2021-06-14 13:59:27', 'confirmed'),
    (2, '2021-01-22 00:00:00', 'confirmed'),
    (2, '2021-02-28 23:59:59', 'timeout');

-- 3. Solution
SELECT s.user_id,
       ROUND(AVG(CASE WHEN c.action = 'confirmed' THEN 1 ELSE 0 END), 2)
           AS confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c
       ON s.user_id = c.user_id
GROUP BY s.user_id
ORDER BY s.user_id;

-- Expected output:
-- user_id | confirmation_rate
-- 2       | 0.5
-- 3       | 0.0
-- 6       | 0.0
-- 7       | 1.0