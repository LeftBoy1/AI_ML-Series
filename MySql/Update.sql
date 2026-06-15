/*Update - updating existing rows*/


Create DATABASE updating;
use updating;

Create Table student (				 
ID INT PRIMARY KEY,					
name VARCHAR(50),
Age INT NOT NULL,
City VARCHAR(50),
marks int
);

#adding new column in table (if u execute the whole code and then add a new column , then use this method to add becuase if u are going to add column directly it throws an error
ALTER TABLE student
ADD grades VARCHAR(50);



INSERT INTO student
(ID, name, Age, City, marks,grades)
VALUES
(1,"Yashika",16, "Alwar",98, "A+"),		
(2,"Rajat",10, "Gurugram",79, "C"),
(3,"Anmol",8, "Bhiwadi", 89,"B"),
(4, "Harsh",21, "Mysore", 99, "A+"),
(5, "Devansh",18, "Jaipur",97, "A+"),
(6, "Shyam", 11, "Delhi", 100, "A+"),
(7 , "Ram", 9, "Mumbai", 95, "A"),
(8, "Bhumika",20, "Ajmer", 99, "A+"),
(9, "Poorvanshi",18, "Ajmer",97, "A+"),
(10, "Asha", 40, "Alwar", 100, "A+"),
(11, "Ramesh", 11, "Mumbai", 95, "A"),
(12, "Harish", 34, "Delhi",67, "D");

SET SQL_SAFE_UPDATES = 0;		#it is used to turn off & on the safe mode in mysql, 0= "OFF" while 1= "ON"

#updating the marks of student
UPDATE student
SET marks = "90"
WHERE name = "Ramesh";


#updating the grade
Update student
set grades = "A"
Where marks between 90 and 100;


#updating marks of all students
Update student
set marks = marks+1;

SELECT * from student;
