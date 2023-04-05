					 MySQL advanced

				Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

				General

1. How to create tables with constraints
2. How to optimize queries by adding indexes
3. What is and how to implement stored procedures and functions in MySQL
4. What is and how to implement views in MySQL
5. What is and how to implement triggers in MySQL


				Creating tables with Constraints

You can use the CREATE TABLE statement along with the appropriate constraints.
Here's an example of creating a table with constraints:

```CREATE TABLE users (
    id INT PRIMARY KEY,
    hobby VARCHAR(50) NOT NULL,
    place VARCHAR(50) UNIQUE,
    age INT CHECK (age > 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);```


				Optimizing queries by adding indexes

	Indexes are used to speed up the search or retrieval of data from tables.
Adding indexes to tables can significantly improve the performance of queries.
syntax:
```CREATE INDEX index_name ON table_name (column1, column2, column3);```

				
				Implementing stored procedures and functions in MySQL


	Stored procedures and functions are database objects in MySQL that allow you to group a set of SQL statements
together and execute them as a single unit. They can be used to simplify complex tasks


Creating procedures:					
	In other to create a procedure that helps view all the user_info in a user_info table we run the following syntax:
``` CREATE PROCEDURE nameOfProcedure() 
	SELECT * FROM user_info $$ ```	

Now with that in place rather than having to type out all the above query syntax all you need do is call the procedure by its name using the following syntax
```CALL user_data()$$ ```
		
To display and check the properties of a created procedure, you use the syntax:
``` SHOW CREATE PROCEDURE proc_name ```


				 implementing views in MySQL

what is a view?
	A view is a virtual table that is based on the result set of an SQL statement.
The view is not an actual table, but a stored query that can be used as a table in queries

syntax:
```CREATE VIEW my_view AS
	SELECT column1, column2, column3
	FROM my_table
	WHERE column1 = 'some_value'; ```

```SELECT * FROM my_view ```

				 implementing triggers in MySQL

what is a trigger?
	A trigger is a database object that is associated with a table and is activated automatically when a particular event occurs for the table,
such as inserting, updating or deleting data.
The main purpose of a trigger is to perform a specific action or set of actions when the associated event occurs.

syntax:
	```CREATE TRIGGER update_column AFTER INSERT ON mytable
		FOR EACH ROW
		BEGIN
    			UPDATE mytable SET column2 = column1 * 2 WHERE id = NEW.id;
		END; ```

