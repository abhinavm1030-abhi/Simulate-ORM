import mysql.connector

conn=mysql.connector.connect(host="localhost",user="root",password="root",database="DjangoORM")
cur=conn.cursor()

# cur.execute("create database DjangoORM")
# print("database created")

# cur.execute('''create table employee(
#             id int primary key  auto_increment,
#             name   varchar(20),
#             designation    varchar(20),
#             salary      decimal(10,2)
#         )''')

# print("Table created")

class Employee:
    def create(self,*args,**kwargs):
        keys=""
        placeholder=""
        for key in kwargs.keys():
            if keys!="":
                keys+=','
                placeholder+=','
            keys+=key
            placeholder+="%s"
        value=tuple(kwargs.values())
        query=f"insert into employee({keys}) values({placeholder})"
        cur.execute(query,value)
        conn.commit()
        print("Employee created successfully!")

    def list(self,*args,**kwargs):
        cur.execute("select * from employee")
        for emp in cur:
            print(emp)

    def retrieve(self,*args,**kwargs):
        for key in kwargs:
            cur.execute(f"select * from employee where {key}={kwargs.get(key)}")
            print(cur.fetchall())

    def update(self,*args,**kwargs):
        print(args,kwargs)
        for key in kwargs:
            cur.execute(f"update employee set  {key}='{kwargs.get(key)}' where id={args[0]}")
            conn.commit()
            print("Employee updated successfully!")

    def delete(self,*args,**kwargs):
        for key in kwargs:
            cur.execute(f"delete from employee where {key}={kwargs.get(key)}")
            conn.commit()
            print("Employee deleted successfully!")

    def filter(self,*args,**kwargs):
        # for key, value in kwargs.items():
        #     query = f"SELECT * FROM employee WHERE {key} = %s"
        #     cur.execute(query, (value,))
        #     print(cur.fetchall())
        for key in kwargs:
            cur.execute(F"select * from employee where {key}='{kwargs.get(key)}'")
            print(cur.fetchall())


employee=Employee()

while True:
    print("1. Create Employee")
    print("2. List all Employee")
    print("3. Employee detail view")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Filter Employee")
    print("7. Exit")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        name=input("Enter the employee name : ")
        desig=input("Enter the designation : ")
        salary=float(input("Enter the salary amount : "))
        employee.create(name=name,designation=desig,salary=salary)

    elif choice == 2:
        employee.list()

    elif choice == 3:
        id=int(input("Enter the employee ID : "))
        employee.retrieve(id=id)

    elif choice == 4:
        id=int(input("Enter the employee ID :"))
        print("Update")
        print("1. Name")
        print("2. Designation")
        print("3. Salary")
        choice=int(input("Enter choice :"))
        if choice==1:
            name=input("Enter new name :")
            employee.update(id,name=name)
        elif choice==2:
            desig=input("Enter new designation :")
            employee.update(id,designation=desig)
        elif choice==3:
            salary=float(input("Enter new salary :"))
            employee.update(id,salary=salary)
        else:
            print("Invalid choice....")
                
    elif choice == 5:
        id=int(input("Enter the employee ID : "))
        employee.delete(id=id)

    elif choice == 6:
        print("Filter Employee")
        print("1. Filter by id")
        print("2. Filter by name")
        print("3. Filter by designation")
        print("4. Filter by salary")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            id = int(input("Enter employee ID: "))
            employee.filter(id=id)
        elif choice == 2:
            name = input("Enter employee name: ")
            employee.filter(name=name)
        elif choice == 3:
            designation = input("Enter designation: ")
            employee.filter(designation=designation)
        elif choice == 4:
            salary = float(input("Enter salary: "))
            employee.filter(salary=salary)
        else:
            print("Invalid choice!")

    elif choice == 7:
        break

    else:
        print("Invalid Choice")

conn.close()
print("Connection Close")
