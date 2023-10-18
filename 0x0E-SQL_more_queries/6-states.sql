-- Create database hbtn_0d_usa and table states (in the database hbtn_0d_usa) on your MySQL server
-- Create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use database
USE hbtn_0d_usa;
-- create table
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));
