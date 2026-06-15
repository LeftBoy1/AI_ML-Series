/*
Alter - TO change the schema

1. ADD Column -
					ALTER TABLE table_name 
					ADD COLUMN column_name datatype constraint; 

2. DROP Column -
					ALTER TABLE table_name 
					DROP COLUMN column_name; 

3. RENAME Table -
					ALTER TABLE table_name 
					RENAME TO new_table_name; 

4. CHANGE Column (rename) -
							ALTER TABLE table_name 
							CHANGE COLUMN old_name new_name new_datatype new_constraint; 

5. MODIFY Column (modify datatype/ constraint)
												ALTER TABLE table_name 
												MODIFY col_name new_datatype new_constraint; 
*/



Create DATABASE alter_database;
use alter_database;

Create Table student (				 
ID INT PRIMARY KEY,					
name VARCHAR(50),
Age INT NOT NULL,
City VARCHAR(50),
marks int
);

#Alter
Alter table student
add column grades varchar(50);


#Rename Table
alter Table student
rename to students;


INSERT INTO student
(ID, name, Age, City, marks,grades)
VALUES
(1,"Yashika",16, "Alwar",98, "A+"),		
(2,"Rajat",10, "Gurugram",79, "C"),
(3,"Anmol",8, "Bhiwadi", 89,"B"),
(4, "Harsh",21, "Mysore", 99, "A+"),
(5, "Devansh",18, "Jaipur",97, "A+");

SELECT * from student;



select * from changing