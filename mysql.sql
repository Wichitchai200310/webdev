-- Active: 1727723728897@@127.0.0.1@3306@ecommerce
CREATE DATABASE bakery_db CHARACTER SET utf8;
CREATE USER 'root'@'localhost' IDENTIFIED BY '1234';
GRANT ALL PRIVILEGES ON bakery_db.* TO 'root'@'localhost';
SET GLOBAL transaction_isolation = 'READ-COMMITTED';
SET GLOBAL time zone 'Asia/Bangkok';
FLUSH PRIVILEGES;
