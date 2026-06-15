/*
Truncate - It delets the table's data 
		   While "DROP" delete the whole table 
           
Syntax - Truncate Table table_name
*/

Create DATABASE truncate_database;
use truncate_database;

Create Table student (				 
ID INT PRIMARY KEY,					
name VARCHAR(50),
Age INT NOT NULL,
City VARCHAR(50),
marks int,
grades varchar(50)
);


INSERT INTO student
(ID, name, Age, City, marks,grades)
VALUES
(1,"Yashika",16, "Alwar",98, "A+"),		
(2,"Rajat",10, "Gurugram",79, "C"),
(3,"Anmol",8, "Bhiwadi", 89,"B"),
(4, "Harsh",21, "Mysore", 99, "A+"),
(5, "Devansh",18, "Jaipur",97, "A+");

Truncate Table student;

SELECT * from student;

