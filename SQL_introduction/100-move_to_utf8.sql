-- 100. Convert hbtn_0c_0 DB, first_table, and name field to utf8mb4 with utf8mb4_unicode_ci

-- Change the default charset and collation of the database
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Select the database
USE hbtn_0c_0;

-- Change the table to utf8mb4 (this will change all columns unless overridden)
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Fix the name column to use only collation (avoid explicit charset in output)
ALTER TABLE first_table CHANGE name name VARCHAR(256) COLLATE utf8mb4_unicode_ci DEFAULT NULL;
