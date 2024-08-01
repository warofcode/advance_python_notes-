import csv
import mysql.connector

# Establish a connection to MySQL
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin"
)

# Create a new database
cursor = cnx.cursor()
cursor.execute("CREATE DATABASE bhaskar_database")

# Connect to the new database
cnx.database = "bhaskar_database"

# Create the "table" table
create_table_query = """
    CREATE TABLE `bhaskar_table` (
        bike_name VARCHAR(255),
        price DECIMAL(10, 2),
        city VARCHAR(255),
        kms_driven INT,
        owner VARCHAR(255),
        age INT,
        power INT,
        brand VARCHAR(255)
    )
"""
cursor.execute(create_table_query)

# Open the CSV file
with open('task_2_used_bikes.csv', 'r') as file:
    # Create a CSV reader
    csv_data = csv.reader(file)
    next(csv_data)  # Skip the header row

    # Iterate over each row in the CSV file
    for row in csv_data:
        # Extract the values from the CSV row
        bike_name, price, city, kms_driven, owner, age, power, brand = row

        # Prepare the SQL query to insert a new row into the table
        insert_query = """
            INSERT INTO `bhaskar_table` (bike_name, price, city, kms_driven, owner, age, power, brand)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (bike_name, price, city, kms_driven, owner, age, power, brand)

        # Execute the query
        cursor.execute(insert_query, values)

# Commit the changes and close the connection
cnx.commit()
cursor.close()
cnx.close()
