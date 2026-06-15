/*Group By Clause - Groups rows that have the same value into summary rows. 
					It collects data from multiple records and groups the result by one or more column.
                    Generaly we use group by with aggegration function. 
*/
Create DATABASE Grp_Clause;
use Grp_Clause;

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


#count numbers of students in city 
#1
select city, count(name) 	#count(), max(), mini(), avg()
from student 
GROUP BY city;		

#2
select city,name , count(name) 
from student 
GROUP BY city, name;	