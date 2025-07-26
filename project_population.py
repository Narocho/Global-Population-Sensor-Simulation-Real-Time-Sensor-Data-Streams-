import pymysql
import time
from datetime import datetime, timedelta
import pymysql.cursors
import pandas as pd

# Database Connection Configuration
host = 'your_host'
user = 'your_user'
password = 'your_password'
database = 'your_database'

try:
   # Establish a connection to the database.
   connection = pymysql.connect(
       port=3306,
       host='localhost',
       user='pythonuser',
       password='',
       database='final_558',
       cursorclass=pymysql.cursors.DictCursor  # Use a dictionary cursor for easier data manipulation
   )

   # Create a cursor object to execute SQL queries.
   cursor = connection.cursor()

   # Print a success message if the connection is successful.
   print("Connected to the database successfully!")


except pymysql.Error as e:
    # Print an error message if the connection fails
    print(f"Error: Unable to connect to the database. {e}")

# Read your filtered_data CSV
filtered_data = pd.read_csv('filtered_data.csv')

# creating a loop to simulate a live stream of data.
for index, row in filtered_data.iterrows():
    current_date = pd.to_datetime(row['updated_datetime'])
    # Remove commas from 'current_population' and convert to int
    row['current_population'] = int(row['current_population'].replace(',', ''))
    # Insert data into the MySQL table(named filtered_population)
    query = f"INSERT INTO filtered_population (iso_code, country, current_population, updated_datetime) VALUES ('{row['iso_code']}', '{row['country']}', {row['current_population']}, '{row['updated_datetime']}')"
    print("Query:", query)

    # Print the values for further inspection
    print("Values:", row)

    cursor.execute(query)
    connection.commit()



    # Sleep to simulate real-time updates (adjust sleep duration as needed)
    time.sleep(3)


