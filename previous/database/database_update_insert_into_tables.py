# connect to database
import sqlite3

with sqlite3.connect("formode_repository.db") as db:
    cursor = db.cursor()



####################INSERTING INTO THE TABLES#######################

# insert into project details table
def insert_project_details_table(client_name, project_category, project_source, project_scope,
                                 date_commencement, date_completion, project_name, project_status):
    """insert data into project_details_table"""
    cursor.execute("""INSERT INTO project_details(project_name,client_name,project_category,project_source,
    project_scope,date_commencement,date_completion,project_status)
                                VALUES(?,?,?,?,?,?,?,?)""",
                   (project_name, client_name, project_category, project_source,
                    project_scope, date_commencement, date_completion, project_status))
    print("project details added successfully")
    db.commit()

#  insert into project funds table
def insert_project_funds_table(project_name, project_fund, company_fund, salaries, tax):
    """insert data into project_funds_table"""
    # insert into project_funds table
    cursor.execute("""INSERT INTO project_funds(project_name,project_fund,company_fund,salaries,tax)
                                    VALUES(?,?,?,?,?)""", (project_name, project_fund, company_fund,
                                                                 salaries, tax))
    print("project funds details added successfully")
    db.commit()


# insert into salaries table
def insert_salaries_funds_table(project_name, project_user, director_1, director_2, employee_3, employee_4, employee_5, employee_6,employee_7):
    """insert data into project_funds_table"""
    cursor.execute("""INSERT INTO salaries_funds(project_name, project_doneby,director_1,director_2,employee_3,employee_4,employee_5,employee_6,employee_7)
                                    VALUES(?,?,?,?,?,?,?,?,?)""", (project_name, project_user, director_1, director_2, employee_3, employee_4, employee_5, employee_6,employee_7))
    print("Salaries funds details added successfully")
    db.commit()


# insert into pesa_funds table
def insert_into_pesafunds(time_id, funds_date, co_fund_type, co_sub_type, typology, currency,
                          amount, er_income):
    """insert data into project_funds_table"""
    cursor.execute("""INSERT INTO pesa_funds(time_id,funds_date,co_fund_type,co_sub_type,typology,
    currency,amount,er_income)
                                    VALUES(?,?,?,?,?,?,?,?)""", (time_id, funds_date, co_fund_type, co_sub_type,
                                                                 typology, currency, amount, er_income))
    print("pesa funds details added successfully")
    db.commit()


######################## UPDATING TABLES ################################

# update project details
def update_project_details_table(date_completion, project_name):
    """Update project details after project marked complete"""
    cursor.execute("""UPDATE project_details SET project_status = 'COMPLETE', date_completion = ? 
    WHERE project_name = ?""", [date_completion, project_name])
    db.commit()

# update project funds table
def update_project_funds_table(project_name, project_fund, company_fund,salaries, tax):
    """Update project details after project marked complete"""
    cursor.execute("""UPDATE project_funds SET project_fund=?,company_fund=?,salaries=?,tax =? 
    WHERE project_name = ?""", [project_fund, company_fund, salaries, tax, project_name])
    db.commit()

# update salaries table
def update_salaries_table(project_name, project_doneby, director_1, director_2, employee_3, employee_4, employee_5, employee_6,employee_7):
    """Update project details after project marked complete"""
    cursor.execute("""UPDATE salaries_funds SET project_doneby=?,director_1=?,director_2=?,employee_3=?,employee_4=?,employee_5=?,employee_6=?,employee_7=?
    WHERE project_name = ?""", [project_doneby, director_1, director_2, employee_3, employee_4,employee_5,employee_6,employee_7,project_name])
    db.commit()
