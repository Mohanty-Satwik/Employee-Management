import mysql.connector as a
con = a.connect(host = "localhost",
                user = "root",
                password="1112",
                database="employee")

def npersonal():
    n = input("Enter Employee Name : ")
    c = input("Enter Employee's City Name : ")
    d = input("Enter Employee's D.O.B : ")
    p = input("Enter Employee Phone No. : ")
    data = (n,c,d,p)
    sql = 'INSERT INTO personal(Name, City, Birthdate, Phone) VALUES(%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Entered Successfully")
    main()

def personal():
    sql = "select * from personal"
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    for i in d:
        print(i)
    main()

def noffice():
    ec = input("Enter Employee Code : ")
    n = input("Enter Employee Name : ")
    ps = input("Enter Employee's Post : ")
    j = input("Enter Employee joining date : ")
    bp = int(input("Enter Assigned Salary : "))
    data = (ec,n,ps,j,bp)
    sql = 'INSERT INTO office(Ecode, Name, Post, Joining, BasicPay) VALUES(%s,%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Entered Successfully")
    main()

def office():
    sql = "select * from office"
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    for i in d:
        print(i)
    main()

def nsalary():
    ec = input("Enter Employee Code :")
    v = (ec,)
    sql = "select BasicPay from office where Ecode = %s"
    c = con.cursor()
    c.execute(sql,v)
    bs = c.fetchone()
    n = input("Enter Employee Name : ")
    y = input("Enter Year : ")
    m = input("Enter Month : ")
    wd = int(input("Enter Working Days : "))
    td = int(input("Enter Total Days : "))
    fp = bs[0]/td*wd
    data = (ec,n,y,m,wd,fp)
    sql = 'INSERT INTO salary(Ecode, Name, Year, Month, WorkingD, FinalPay) VALUES(%s,%s,%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Entered Successfully")
    main()

def salary():
    sql = "select * from salary"
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    for i in d:
        print(i)
    main()

def main():
    print("""1. Add New Employee Personal Details
2. Display Employee Personal Details
3. Add New Employee Office Details
4. Display Employee Office Details
5. Enter Salary Details of Employee
6. Display Salary Details of Employee""")
    choice = input("Enter Task No. : ")
    while True:
        if(choice == '1'):
            npersonal()
        elif(choice == '2'):
            personal()
        elif(choice == '3'):
            noffice()
        elif(choice == '4'):
            office()
        elif(choice == '5'):
            nsalary()
        elif(choice == '6'):
            salary()
        else:
            print("Wrong Choice....")
    main()

main()

    


    
