# connect to database
import sqlite3

with sqlite3.connect("formode_repository.db") as db:
    cursor = db.cursor()


####################CREATTING TABLES#######################
def create_tables():
    """create tables"""
    # project_details table
    cursor.execute("""CREATE TABLE IF NOT EXISTS project_details(
    project_name text PRIMARY KEY,
    client_name text NOT NULL,
    project_category text NOT NULL,
    project_source text NOT NULL,
    project_scope text NOT NULL,
    date_commencement text NOT NULL,
    date_completion text );""")

    # project_funds table
    cursor.execute("""CREATE TABLE IF NOT EXISTS project_funds(
    project_name text PRIMARY KEY,
    project_doneby text NOT NULL,
    project_fund integer NOT NULL,
    company_fund integer NOT NULL,
    symon_income integer NOT NULL,
    brian_income integer NOT NULL,
    other_income integer NOT NULL,
    tax integer NOT NULL);""")

    print("Tables connected")


create_tables()


####################INSERTING INTO THE TABLES#######################

def insert_project_details_table(client_name, project_category, project_source, project_scope,
                                 date_commencement, date_completion, project_name, project_status):
    """insert data into project_details_table"""
    # insert into project_details table
    cursor.execute("""INSERT INTO project_details(project_name,client_name,project_category,project_source,
    project_scope,date_commencement,date_completion,project_status)
                                VALUES(?,?,?,?,?,?,?,?)""",
                   (project_name, client_name, project_category, project_source,
                    project_scope, date_commencement, date_completion, project_status))
    print("project details added successfully")
    db.commit()


def insert_project_funds_table(project_name, project_user, project_fund, company_fund, brian_income, symon_income,
                               other_income, tax):
    """insert data into project_funds_table"""
    # insert into project_funds table
    cursor.execute("""INSERT INTO project_funds(project_name,project_doneby,project_fund,company_fund,symon_income,
    brian_income,other_income,tax)
                                    VALUES(?,?,?,?,?,?,?,?)""", (project_name, project_user, project_fund, company_fund,
                                                                 symon_income, brian_income, other_income, tax))
    print("project funds details added successfully")
    db.commit()


def alter_table():
    """Add column to a table"""
    print("******ADD COLUMN TO DATABASE******")
    table_name = input("name of table:")
    column_name = input("name of column:")
    data_type = input("data type:")
    cursor.execute(f"""ALTER TABLE {table_name} ADD {column_name} {data_type} ;""")


def view_salary():
    """Change the values recorded and ammend with new values"""

    from datetime import datetime
    correct = True
    while correct:
        print("\n*****************************************VIEW INCOME*****************************************")
        # months dictionary
        year = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun", 7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct",
                11: "Nov", 12: "Dec"}

        year_indexed = list(year)

        # loop through the month
        for months in year:
            print(f"{months}.{year[months]}", end="  ")
        print(" 0.Quit")

        select_month = int(input("\nselect option: "))

        if select_month == 0:
            correct = False

        elif select_month in range(1, 13):
            company_fund = 0
            symon_income = 0
            brian_income = 0
            other_income = 0
            total_fund = 0

            # company fund

            cursor.execute("""SELECT project_funds.company_fund, project_details.date_completion FROM project_funds, 
                                project_details """)
            for row in cursor.fetchall():
                if row[1] is not None:
                    value = row[0]
                    date = row[1]
                    month = int(date[5:7])
                    if month == select_month:
                        company_fund += value

            # symon income
            cursor.execute("""SELECT project_funds.symon_income, project_details.date_completion FROM project_funds, 
                                project_details """)
            for row in cursor.fetchall():
                if row[1] is not None:
                    value = row[0]
                    date = row[1]
                    month = int(date[5:7])
                    if month == select_month:
                        symon_income += value

            # Brian income
            cursor.execute("""SELECT project_funds.brian_income, project_details.date_completion FROM project_funds, 
                                project_details """)
            for row in cursor.fetchall():
                if row[1] is not None:
                    value = row[0]
                    date = row[1]
                    month = int(date[5:7])
                    if month == select_month:
                        brian_income += value

            # employee income
            cursor.execute("""SELECT project_funds.other_income, project_details.date_completion FROM project_funds, 
                                project_details """)
            for row in cursor.fetchall():
                if row[1] is not None:
                    value = row[0]
                    date = row[1]
                    month = int(date[5:7])
                    if month == select_month:
                        other_income += value

            year = {1: "JANUARY", 2: "FEBRUARY", 3: "MARCH", 4: "APRIL", 5: "MAY", 6: "JUNE", 7: "JULY", 8: "AUGUST",
                    9: "SEPTEMBER", 10: "OCTOBER", 11: "NOVEMBER", 12: "DECEMBER", 0: "CLOSED"}

            print(f"\n******INCOME STATS {str.upper(year[select_month])}*******")

            print(f"COMPANY FUND = ${company_fund}")
            print(f"SYMON INCOME = ${symon_income}")
            print(f"BRIAN INCOME = ${brian_income}")
            print(f"EMPLOYEE INCOME = ${other_income}")

            print("********************************")
            print(f"TOTAL FUND = ${company_fund + brian_income + symon_income + other_income}\n")

        else:
            print("Guess you live in mars.There are 12 months here on Earth,try again.")


def view_projects():
    """View all projects in the database"""

    print("\n**************************************SELECT PROJECTS**********************************************")
    # months dictionary
    year = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun", 7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct",
            11: "Nov", 12: "Dec"}

    # loop through the month
    for months in year:
        print(f"{months}.{year[months]}", end="  ")
    print(" 0.Quit")

    select_month = int(input("select month: "))

    year = {1: "JANUARY", 2: "FEBRUARY", 3: "MARCH", 4: "APRIL", 5: "MAY", 6: "JUNE", 7: "JULY", 8: "AUGUST",
            9: "SEPTEMBER", 10: "OCTOBER", 11: "NOVEMBER", 12: "DECEMBER"}

    print(
        f"\n*****************************PROJECTS COMPLETED ON {year[select_month]} **************************************")
    # Print projects
    projects = {}
    cursor.execute("""SELECT project_funds.project_name FROM project_funds""")
    for index, row in enumerate(cursor.fetchall()):
        value = row[0]
        #date = row[1]
        month = 2

        if month == select_month:
            num = index + 1
            projects[num] = value
            print(f"{index + 1}. {value} ")

    print("******************************************************************************************")

    # select projects to be edited
    project_index_sel = int(input("select project: "))
    pj_name = projects[project_index_sel]

    print(f"\n****************{str.upper(pj_name)} MODIFICATION **************")
    print("1) Delete project\n"
          "2) Edit project parameters")
    user_select = int(input("user option:"))

    if user_select == 1:
        cursor.execute("""DELETE FROM project_funds WHERE project_name =?""", [pj_name])
        cursor.fetchall()
        print(f"{pj_name} deleted")
        db.commit()


def active_projects():
    """Display active projects, ask user if he/she wants to complete them"""
    cursor.execute("""SELECT project_name FROM project_details WHERE project_status = 'ACTIVE'""")

    print(f"\n*****************************ACTIVE PROJECTS **************************************")
    projects = {}
    for index, row in enumerate(cursor.fetchall()):
        num = index + 1
        value = row[0]
        projects[num] = value
        print(f"{num}. {value}")
    print("0. Go back")
    print(f"************************************************************************************")

    selection = int(input("Mark project complete:"))

    if selection == 0:
        return None

    else:
        selected_project = projects[selection]
        print(f"{selected_project} marked complete")
        return selected_project


def retrieve_source_user(data):
    """retrieve source and user of the selected project"""
    cursor.execute("""SELECT project_details.project_source,project_funds.project_doneby 
    FROM project_details, project_funds WHERE project_details.project_name = project_funds.project_name 
    AND project_details.project_name=?""", [data])

    for row in cursor.fetchall():
        values = (row[0], row[1])
        return values


def mark_active_complete(project_name, date_completion, project_fund, company_fund, symon_income, brian_income,
                         other_income,
                         tax):
    """" mark project complete """
    # update project_details table
    cursor.execute("""UPDATE project_details SET project_status = 'COMPLETE', date_completion = ? 
    WHERE project_name = ?""", [date_completion, project_name])

    # update project_funds table
    cursor.execute("""UPDATE project_funds SET project_fund=?,company_fund=?,symon_income=?,
    brian_income=?,other_income=?,tax=? WHERE project_name = ?""",
                   [project_fund, company_fund, symon_income, brian_income,
                    other_income, tax, project_name])
    print("project updated completely")
    db.commit()
