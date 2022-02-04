#!/usr/bin/env python
# coding: utf-8

# # Table 1: SalesPeople
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| anupama            |
| information_schema |
| mysql              |
| performance_schema |
| sales              |
| sys                |
+--------------------+
6 rows in set (0.17 sec)

mysql> CREATE DATABASE ASSIGMENT;


mysql> USE ASSIGMENT;

mysql> CREATE TABLE SALESPEOPLE(Snum INT PRIMARY KEY,
Sname VARCHAR(50) UNIQUE KEY,
City VARCHAR(50),
Comm INT
);

SHOW TABLES;

INSERT INTO SALESPEOPLE VALUES
(1001,'Peel','London',12),
(1002,'Serres','Sanjose',13),
(1004,'Motika','London',11),
(1007,'Rifkin','Barcelona',15),
(1003,'Axelrod','Newyork',10);

SELECT * FROM SALESPEOPLE;
+------+---------+-----------+------+
| Snum | Sname   | City      | Comm |
+------+---------+-----------+------+
| 1001 | Peel    | London    |   12 |
| 1002 | Serres  | Sanjose   |   13 |
| 1003 | Axelrod | Newyork   |   10 |
| 1004 | Motika  | London    |   11 |
| 1007 | Rifkin  | Barcelona |   15 |
+------+---------+-----------+------+
DESC SALESPEOPLE;

+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| Snum  | int         | NO   | PRI | NULL    |       |
| Sname | varchar(55) | YES  | UNI | NULL    |       |
| City  | varchar(35) | YES  |     | NULL    |       |
| Comm  | int         | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
# # Table 2: Customers
mysql> CREATE TABLE Customers(
    -> Cnum INT PRIMARY KEY,
    -> Cname VARCHAR(30),
    -> City VARCHAR(30) NOT NULL,
    -> Snum INT,
    -> FOREIGN KEY (Snum) REFERENCES Salespeople(Snum));


mysql> INSERT INTO Customers VALUES
    -> (2001,"Hoffman","London",1001),
    -> (2002,"Giovanni","Rome",1003),
    -> (2003,"Liu","Sanjose",1002),
    -> (2004,"Grass","Berlin",1002),
    -> (2006,"Clemens","London",1001),
    -> (2008,"Cisneros","Sanjose",1007),
    -> (2007,"Pereira","Rome",1004);


mysql> SELECT * FROM CUSTOMERS;
+------+----------+---------+------+
| Cnum | Cname    | City    | Snum |
+------+----------+---------+------+
| 2001 | Hoffman  | London  | 1001 |
| 2002 | Giovanni | Rome    | 1003 |
| 2003 | Liu      | Sanjose | 1002 |
| 2004 | Grass    | Berlin  | 1002 |
| 2006 | Clemens  | London  | 1001 |
| 2007 | Pereira  | Rome    | 1004 |
| 2008 | Cisneros | Sanjose | 1007 |
+------+----------+---------+------+

# # Table 3: Orders
CREATE TABLE ORDERS(
Onum INT PRIMARY KEY,
Amt FLOAT,
Odate DATE,
Cnum INT,
Snum INT,
FOREIGN KEY (Cnum) REFERENCES customers(Cnum),
FOREIGN KEY (Snum) REFERENCES salespeople(Snum));

INSERT INTO orders VALUES
(3001,18.69,"1990-10-3",2008,1007),
(3003,767.19,"1990-10-3",2001,1001),
(3002,1900.10,"1990-10-3",2007,1004),
(3005,5160.45,"1990-10-3",2003,1002),
(3006,1098.16,"1990-10-3",2008,1007),
(3009,1713.23,"1990-10-4",2002,1003),
(3007,75.75,"1990-10-4",2004,1002),
(3008,4273.00,"1990-10-5",2006,1001),
(3010,1309.95,"1990-10-6",2004,1002),
(3011,9891.88,"1990-10-6",2006,1001);

SELECT * FROM ORDERS;
+------+---------+------------+------+------+
| Onum | Amt     | Odate      | Cnum | Snum |
+------+---------+------------+------+------+
| 3001 |   18.69 | 1990-10-03 | 2008 | 1007 |
| 3002 |  1900.1 | 1990-10-03 | 2007 | 1004 |
| 3003 |  767.19 | 1990-10-03 | 2001 | 1001 |
| 3005 | 5160.45 | 1990-10-03 | 2003 | 1002 |
| 3006 | 1098.16 | 1990-10-03 | 2008 | 1007 |
| 3007 |   75.75 | 1990-10-04 | 2004 | 1002 |
| 3008 |    4273 | 1990-10-05 | 2006 | 1001 |
| 3009 | 1713.23 | 1990-10-04 | 2002 | 1003 |
| 3010 | 1309.95 | 1990-10-06 | 2004 | 1002 |
| 3011 | 9891.88 | 1990-10-06 | 2006 | 1001 |
+------+---------+------------+------+------+
10 rows in set (0.00 sec)

DESC ORDERS;
+-------+-------+------+-----+---------+-------+
| Field | Type  | Null | Key | Default | Extra |
+-------+-------+------+-----+---------+-------+
| Onum  | int   | NO   | PRI | NULL    |       |
| Amt   | float | YES  |     | NULL    |       |
| Odate | date  | YES  |     | NULL    |       |
| Cnum  | int   | YES  | MUL | NULL    |       |
| Snum  | int   | YES  | MUL | NULL    |       |
+-------+-------+------+-----+---------+-------+
5 rows in set (0.00 sec)
# ### 1.  Count the number of Salesperson whose name begin with ‘a’/’A’.

SELECT * FROM SALESPEOPLE WHERE BINARY Sname LIKE "A%";
+------+---------+---------+------+
| Snum | Sname   | City    | Comm |
+------+---------+---------+------+
| 1003 | Axelrod | Newyork |   10 |
+------+---------+---------+------+
1 row in set, 1 warning (0.01 sec)



SELECT * FROM SALESPEOPLE WHERE BINARY Sname LIKE "a";
Empty set, 1 warning (0.00 sec)



SELECT COUNT(Sname) FROM SALESPEOPLE WHERE Sname LIKE "A%";
+--------------+
| COUNT(Sname) |
+--------------+
|            1 |
+--------------+
1 row in set (0.01 sec)



SELECT COUNT(Sname) FROM SALESPEOPLE WHERE BINARY Sname LIKE "a%";
+--------------+
| COUNT(Sname) |
+--------------+
|            0 |
+--------------+
1 row in set, 1 warning (0.00 sec)
# ### 2.Display all the Salesperson whose all orders worth is more than Rs. 2000.
SELECT salespeople.Sname,orders.Amt FROM salespeople 
INNER JOIN orders ON salespeople.Snum = orders.Snum 
WHERE Amt>2000;

+--------+---------+
| Sname  | Amt     |
+--------+---------+
| Serres | 5160.45 |
| Peel   |    4273 |
| Peel   | 9891.88 |
+--------+---------+
# ### 3.Count the number of Salesperson belonging to Newyork.
SELECT * FROM salespeople WHERE City = "Newyork"; 

+------+---------+---------+------+
| Snum | Sname   | City    | Comm |
+------+---------+---------+------+
| 1003 | Axelrod | Newyork |   10 |
+------+---------+---------+------+


SELECT COUNT(City) AS City_Name FROM salespeople WHERE City = "Newyork"; 

+-----------+
| City_Name |
+-----------+
|         1 |
+-----------+
# ### 4. Display the number of Salespeople belonging to London and belonging to Paris.
SELECT * FROM salespeople WHERE City IN ("London","Paris"); 

+------+--------+--------+------+
| Snum | Sname  | City   | Comm |
+------+--------+--------+------+
| 1001 | Peel   | London |   12 |
| 1004 | Motika | London |   11 |
+------+--------+--------+------+
# ### 5. Display the number of orders taken by each Salesperson and their date of orders.
SELECT salespeople.Sname,COUNT(orders.Onum) AS "Numbers of Orders",orders.Odate FROM salespeople 
 	INNER JOIN orders ON salespeople.Snum = orders.Snum GROUP BY salespeople.Sname;
    
    +---------+-------------------+------------+
| Sname   | Numbers of Orders | Odate      |
+---------+-------------------+------------+
| Axelrod |                 1 | 1990-10-04 |
| Motika  |                 1 | 1990-10-03 |
| Peel    |                 3 | 1990-10-03 |
| Rifkin  |                 2 | 1990-10-03 |
| Serres  |                 3 | 1990-10-03 |
+---------+-------------------+------------+


SELECT salespeople.Sname,orders.Onum,orders.Odate FROM salespeople INNER JOIN orders ON salespeople.Snum = orders.Snum;

+---------+------+------------+
| Sname   | Onum | Odate      |
+---------+------+------------+
| Axelrod | 3009 | 1990-10-04 |
| Motika  | 3002 | 1990-10-03 |
| Peel    | 3003 | 1990-10-03 |
| Peel    | 3008 | 1990-10-05 |
| Peel    | 3011 | 1990-10-06 |
| Rifkin  | 3001 | 1990-10-03 |
| Rifkin  | 3006 | 1990-10-03 |
| Serres  | 3005 | 1990-10-03 |
| Serres  | 3007 | 1990-10-04 |
| Serres  | 3010 | 1990-10-06 |
+---------+------+------------+
