/*Having Clause - Similar to where clause, apllies some condition on rows, used when we want to apply any condition after grouping*/

Create DATABASE Having_Clause;
use Having_Clause;

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
(7 , "Ram", 9, "Mumbai", 95),
(8, "Bhumika",20, "Ajmer", 99),
(9, "Poorvanshi",18, "Ajmer",97),
(10, "Asha", 40, "Alwar", 100),
(11, "Ramesh", 11, "Mumbai", 95),
(12, "Harish", 34, "Delhi",67);

#Count no. of students in each city where max marks cross 90

Select city, count(id) from student Group by city
Having max(marks)>90;
