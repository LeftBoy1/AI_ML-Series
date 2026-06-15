/*
  On Delete Cascade -
					When we create a foreign key using this option, it deletes the referencing rows in the child table
					when the referenced row is deleted in the parent table which has a primary key.
  On Update Cascade -
					When we create a foreign key using UPDATE CASCADE the referencing rows are updated in the child
					table when the referenced row is updated in the parent table which has a primary key.
*/


Create DATABASE cascading;
use cascading;

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

SELECT * from student;


Create table changing(
ID INT PRIMARY KEY,					
name VARCHAR(50),
Age INT NOT NULL,
City VARCHAR(50),
marks int,
grades varchar(50),
FOREIGN KEY (id) references student(id)
ON UPDATE CASCADE
ON DELETE CASCADE
);

INSERT INTO changing
(ID, name, Age, City, marks,grades)
VALUES
(1,"Yashika",16, "Alwar",98, "A+"),		
(2,"Rajat",10, "Gurugram",79, "C"),
(3,"Anmol",8, "Bhiwadi", 89,"B"),
(4, "Harsh",21, "Mysore", 99, "A+"),
(5, "Devansh",18, "Jaipur",97, "A+");

Update student
set id = "10"
where id = "5";

select * from changing