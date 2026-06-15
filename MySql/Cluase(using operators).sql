#Clause USing Operators 

Create Database School;
Use School;

Create Table student (				 
ID INT PRIMARY KEY,					
name VARCHAR(50),
Age INT NOT NULL,
City VARCHAR(50)
);

INSERT INTO student
(ID, name, Age, City)
VALUES
(1,"Yashika",16, "Alwar"),		
(2,"Rajat",10, "Gurugram"),
(3,"Anmol",8, "Bhiwadi"),
(4, "Harsh",21, "Mysore"),
(5, "Devansh",18, "Jaipur"),
(6, "Shyam", 11, "Delhi"),
(7 , "Ram", 9, "Mumbai");


SELECT * FROM student WHERE age+5 >= 16;	#means if we add 5 in age then who are the peoples which are above 16
