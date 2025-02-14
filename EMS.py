import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sujalcode",
    database="signifytest"
)

cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS newDB")
cursor.execute("USE newDB")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Employees (
    id INT PRIMARY KEY,
    name VARCHAR(30),
    age INT
)
""")

def add_employee():
    try:
        emp_id = int(input("Enter Employee ID: "))
        name = input("Enter Employee Name: ")
        age = int(input("Enter Employee Age: "))
        cursor.execute("INSERT INTO Employees (id, name, age) VALUES (%s, %s, %s)", (emp_id, name, age))
        conn.commit()
        print("Employee added successfully!")
    except mysql.connector.IntegrityError:
        print("Error: Employee ID already exists.")

def view_employees():
    cursor.execute("SELECT * FROM Employees")
    rows = cursor.fetchall()
    if rows:
        print("\nEmployees Data:")
        for row in rows:
            print(row)
    else:
        print("No employees found.")

def delete_employee():
    emp_id = int(input("Enter Employee ID to delete: "))
    cursor.execute("DELETE FROM Employees WHERE id = %s", (emp_id,))
    conn.commit()
    if cursor.rowcount > 0:
        print("Employee deleted successfully!")
    else:
        print("Employee not found.")

while True:
    print("\n1. Add Employee\n2. View Employees\n3. Delete Employee\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employees()
    elif choice == "3":
        delete_employee()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

cursor.close()
conn.close()
