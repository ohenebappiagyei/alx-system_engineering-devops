-- This script converts the specified database, table, and field to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)

USE `hbtn_0c_0`

-- Convert the table to utf8mb4
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
