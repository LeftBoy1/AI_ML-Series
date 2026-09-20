#1	BASIC

CREATE DATABASE College;		#create database

/* Create database if not exists College;	 =  create database if not exist in a code */


Use college;		#use = select which database i want to work with


Create Table student (				 
ID INT PRIMARY KEY,					-- (Column_name Datatype Contraint),
name VARCHAR(50),
Age INT NOT NULL
);


INSERT INTO student VALUES(1, "Devansh",18);		#insert = used to insert data in tables
INSERT INTO student VALUES(2, "Harsh",21);

-- OR

INSERT INTO student
(ID, name, Age)
VALUES
(3,"Yashika",16),		
(4,"Rajat",13),
(5,"Anmol",8);
INSERT INTO student VALUES(6, "Unknow",12);


SELECT * FROM student;		#used to select all data from the database 
SELECT id, name FROM student;		#used to select id, name columns data from the database 
SELECT * FROM student WHERE age >= 16;		#selects all data with condition in a table

#SELECT DISTINCT col_name from table_name;	   -->>>   used to select distinct(unique) columns values
#SELECT * FROM table_name WHERE condition1 AND condition2; 			--->>> using 2 conditions at once

SHOW databases;
SHOW TABLES;

/* DROP DATABASE db_name;     =  is used to delete database
	Drop DATABASE if not exists db_name;     = is used to delete databse if it exist in code */
    
    
    
/* Constraint - SQL constraints are used to specify rules for data in a table.
	Types of constraint -
        1. NOT NULL - columns cannot have a null value.
        2. Unique - all values in column are different.
        3. Primary Key -  makes a column unique & not null but used only for one.
*/


/*
KEYS -
	1.Primary Key -
			It is a column (or set of columns) in a table that uniquely identifies each row. (a unique id)
			There is only 1 PK & it should be NOT null.
            
	2.Foreign Key -
			A foreign key is a column (or set of columns) in a table that refers to the primary key in another table.
			There can be multiple FKs.
			FKs can have duplicate & null values 
*/


#2	FOREIGN KEY
create table temp(
	cust_id int,
    Foreign Key (cust_id) references student(id)		#here it is connected to student table's id column
    );



#3	Default (values shows by default)
Create table emp(
	id int,
    salary int default 25000);
    
insert into emp(id) values(101);
select * from emp;



#4	CHECK (checks the condition)
create table city(
	id int primary key,
    age int,
    city varchar(50),
    
    CONSTRAINT age_check CHECK (age >=18 AND city= "Delhi")
    );
	/* OR */
create table city(
	age int CHECK (age >= 18),
    city varchar(50) CHECK (city = 'Delhi')
);