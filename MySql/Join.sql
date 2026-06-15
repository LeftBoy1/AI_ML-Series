/*
Joins in SQL -
				Join is used to combine rows from two or more tables, based on a related column between them.
                
1. INNER JOIN -
				Returns records that have matching values in both tables
						Syntax-
								SELECT column(s) 
								FROM tableA 
								INNER JOIN tableB 
								ON tableA.col_name = tableB.col_name; 

2. OUTER JOIN - 
	A.) Left Join -
					Returns all records from the left table, and the matched records from the right table
						Syntax-
								SELECT column(s) 
								FROM tableA 
								LEFT JOIN tableB 
								ON tableA.col_name = tableB.col_name; 
                                
	B.) Right Join - 
					Returns all records from the right table, and the matched records from the left table
						Syntax-
								SELECT column(s) 
								FROM tableA 
								RIGHT JOIN tableB 
								ON tableA.col_name = tableB.col_name; 
      
	C.) Full Join -
					Returns all records when there is a match in either left or right table Syntax in MySQL. It is the union of left & right joins.
						Syntax - 
								SELECT column(s) 
								FROM tableA 
								LEFT JOIN tableB 
								ON tableA.col_name = tableB.col_name; 
                                
                                UNION
                                
                                SELECT column(s) 
								FROM tableA 
								RIGHT JOIN tableB 
								ON tableA.col_name = tableB.col_name; 
                                
3. Left Exclusive Join -
					only selects the left side part (in venn diagram)
						Syntax -
								Select * from table1 as a
                                Left Join table2 as b
                                ON a.col_name = b.col_name
                                WHERE b.col_name IS NULL;
                                

4. Right Exclusive Join -
					only selects the right side part (in venn diagram)
						Syntax -
								Select * from table1 as a
                                Right Join table2 as b
                                ON a.col_name = b.col_name
                                WHERE b.col_name IS NULL;                                
5. SELF JOIN -
				It is a regular join but the table is joined with itself.
						Syntax- 
								SELECT column(s) 
								FROM table as a 
								JOIN table as b 
								O N a.col_name = b.col_name;
                */