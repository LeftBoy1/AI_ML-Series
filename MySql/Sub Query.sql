/*
SQL Sub Queries-
				A Subquery or Inner query or a Nested query is a query within another SQL query.
				It involves 2 select statements.
					Syntax- 
							SELECT column(s)
							FROM table_name 
							WHERE col_name operator
							( subquery );
*/


Create DATABASE subquery;
use subquery;

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


select avg(marks) from student;

Select name, marks
from student
where marks > 92.4;			#this method is only used for constant value(like avg of class is 92.4)

#OR
select name, marks
from student
where marks > (select avg(marks) from student);			#this method is used for constant and dynamice values(like the avg of class changed, so the final output gets automatically changed

#finding max. marks in alwar city
#Method-1
select max(marks)
from ( select * from student where city ="alwar") as temp;

#Method-2
select max(marks)
from student
where city ="alwar";


#finding max. marks in alwar city with their names
SELECT name, marks FROM student
WHERE city = 'Alwar' AND marks = (SELECT MAX(marks) FROM student WHERE city = 'Alwar');
