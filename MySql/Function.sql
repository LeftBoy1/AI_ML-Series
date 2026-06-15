/* Aggregate Functions - it performs a calculation on a set of values, and return a single value.
	1. COUNT()
    2. MAX()
    3. MINI()
    4. AVG()
    5. SUM()*/


Create DATABASE Management;
use Management;

Create Table student (				 
ID INT PRIMARY KEY,					
name VARCHAR(50),
Age INT NOT NULL,
City VARCHAR(50),
marks int
);

INSERT INTO student
(ID, name, Age, City, marks)
VALUES
(1,"Yashika",16, "Alwar",98),		
(2,"Rajat",10, "Gurugram",79),
(3,"Anmol",8, "Bhiwadi", 89),
(4, "Harsh",21, "Mysore", 99),
(5, "Devansh",18, "Jaipur",97),
(6, "Shyam", 11, "Delhi", 100),
(7 , "Ram", 9, "Mumbai", 95);


Select sum(marks) from student;		#SUM() Function - ask for sum of column