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
                                 date_commencement, date_completion, project_name):

    """insert data into project_details_table"""
    # insert into project_details table
    cursor.execute("""INSERT INTO project_details(project_name,client_name,project_category,project_source,
    project_scope,date_commencement,date_completion)
                                VALUES(?,?,?,?,?,?,?)""", (project_name, client_name, project_category, project_source,
                                                         project_scope, date_commencement,date_completion))
    print("project details added successfully")
    db.commit()


def insert_project_funds_table(project_name,project_user,project_fund, company_fund, brian_income, symon_income,
                               other_income, tax):
    """insert data into project_funds_table"""
    # insert into project_funds table
    cursor.execute("""INSERT INTO project_funds(project_name,project_doneby,project_fund,company_fund,symon_income,
    brian_income,other_income,tax)
                                    VALUES(?,?,?,?,?,?,?,?)""", (project_name, project_user, project_fund, company_fund,
                                                             symon_income, brian_income, other_income, tax))
    print("project funds details added successfully")
    db.commit()



