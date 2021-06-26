# pip install mysql-connector-python

# Creating a Connection with MySQL Server
import mysql.connector

host_name = "localhost"
user_name = "root"
password = "Shirin@123"


my_con = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=password
        )

# Creating a Database inside MySQL Server

cursor = my_con.cursor()
query = "CREATE DATABASE patient_db"
cursor.execute(query)

# Connecting to the newly created database
host_name = "localhost"
user_name = "root"
password = "Shirin@123"
db_name = "patient_db"

my_db_con = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=password,
            database=db_name
        )

# Creating a table inside the database


create_table_query = """
CREATE TABLE IF NOT EXISTS patients (
id INT AUTO_INCREMENT,
name TEXT NOT NULL,
age INT,
sex TEXT,
PRIMARY KEY (id)
) ENGINE = InnoDB
"""

cursor = my_db_con.cursor()
cursor.execute(create_table_query)
my_db_con.commit()

# Inserting Records in a Table

create_patients_query = """
INSERT INTO
`patients` (`name`, `age`, `sex`)
VALUES
('Laura', 24, 'female'),
('Jospeh', 41, 'male'),
('Angel', 33, 'female'),
('Elisabeth', 37, 'female'),
('Joel', 19, 'male');
"""

cursor = my_db_con.cursor()
cursor.execute(create_patients_query)
my_db_con.commit()

# Selecing Records from a Table

select_patients_query = "SELECT * FROM patients"
cursor.execute(select_patients_query)

patients = cursor.fetchall()

for patient in patients:
    print(patient)

# Updating Records in a Table

update_patients_query = """
UPDATE
patients
SET
sex = 'f'
WHERE
sex = 'female'

"""

cursor.execute(update_patients_query)
my_db_con.commit()

# Deleting Records from a Table

delete_patients_query =  "DELETE FROM patients WHERE sex = 'male'"

cursor.execute(delete_patients_query)
my_db_con.commit()