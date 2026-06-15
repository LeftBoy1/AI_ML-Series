/*
MYSQL View -
			A view is a virtual table based on the result-set of an SQL statement.

			*A view always shows up-to-date data. The
			database engine recreates the view, every time a
			user queries it.
SYNTAX -
		Create VIEW view_name AS
        SELECT col_names FROM table_name;
        
        SELECT * FROM view_name;
*/


Create DATABASE mysqlview;
use mysqlview;

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


CREATE View view1 as 
SELECT id, name from student;

select * from view1;