#!/usr/bin/env python
# coding: utf-8

# ##### Write a SQL statement to create a table named countries including columns country_id, country_name and region_id and make sure that no countries except Italy, India and China will be entered in the table.
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| anupama            |
| assigment          |
| dimple             |
| information_schema |
| mysql              |
| performance_schema |
| sales              |
| sys                |
+--------------------+
8 rows in set (0.26 sec)

mysql> CREATE DATABASE COUTRIES;
Query OK, 1 row affected (0.04 sec)

mysql> USE COUTRIES
Database changed
mysql> CREATE TABLE IF NOT EXISTS countries (
    -> COUNTRY_ID varchar(2),
    -> COUNTRY_NAME varchar(40)
    -> CHECK(COUNTRY_NAME IN('Italy','India','China')) ,
    -> REGION_ID decimal(10,0)
    -> );
Query OK, 0 rows affected (0.10 sec)

mysql> DESC COUNTRIES;
+--------------+---------------+------+-----+---------+-------+
| Field        | Type          | Null | Key | Default | Extra |
+--------------+---------------+------+-----+---------+-------+
| COUNTRY_ID   | varchar(2)    | YES  |     | NULL    |       |
| COUNTRY_NAME | varchar(40)   | YES  |     | NULL    |       |
| REGION_ID    | decimal(10,0) | YES  |     | NULL    |       |
+--------------+---------------+------+-----+---------+-------+
3 rows in set (0.03 sec)
# In[ ]:




