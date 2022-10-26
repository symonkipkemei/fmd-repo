# connect to database
import sqlite3

with sqlite3.connect("formode_repository.db") as db:
    cursor = db.cursor()




# collect all projects done, date commencment & date of completion where projects done by a particular bee (honey_collection)


#DEBITS

def honey_preperation_director_2():
    """"collect all projects done, date commencment & date of completion where projects done by a particular bee (honey_collection)"""
    total = 0
    print("**********PROJECTS COMPLETED BY BRIAN 2022************")
    cursor.execute("""SELECT project_details.project_name,project_details.date_completion,salaries_funds.director_2 FROM project_details,salaries_funds WHERE project_details.project_name = salaries_funds.project_name AND salaries_funds.director_2 != 0""")
    for index,row in enumerate(cursor.fetchall()):
        print(str(index + 1) + "." + str(row[0]) + " ** " + str(row[1]) + " ** " + str(row[2]))
        total += int(row[2])
    
    print("******************************************************")
    print(f"TOTAL REVENUE (dollars) :{total}")
    total_ksh = total * 110
    print(f"TOTAL REVENUE (ksh) :{total_ksh}")

def honey_preparation_director_1():
    """"collect all projects done, date commencment & date of completion where projects done by a particular bee (honey_collection)"""
    total = 0
    print("**********PROJECTS COMPLETED BY SYMON 2022************")
    cursor.execute("""SELECT project_details.project_name,project_details.date_completion,salaries_funds.director_1 FROM project_details,salaries_funds WHERE project_details.project_name = salaries_funds.project_name AND salaries_funds.director_1 
     != 0""")
    for index,row in enumerate(cursor.fetchall()):
        print(str(index + 1) + "." + str(row[0]) + " ** " + str(row[1]) + " ** " + str(row[2]))
        total += int(row[2])
    
    print("******************************************************")
    print(f"TOTAL REVENUE (dollars) :{total}")
    total_ksh = total * 110
    print(f"TOTAL REVENUE (ksh) :{total_ksh}")

def loans_repayed_2():
    """Sum of all loans repayed"""
    total = 0
    print("**********REPAYED LOANS************")
    cursor.execute("""SELECT pesa_funds.funds_date,pesa_funds.co_sub_type,pesa_funds.amount FROM pesa_funds WHERE pesa_funds.typology = "BRIAN" AND pesa_funds.co_sub_type = "R_LOANS" """)
    for index,row in enumerate(cursor.fetchall()):
        print(str(index + 1) + "." + str(row[0]) + " ** " + str(row[1]) + " ** " + str(row[2]))
        total += int(row[2])
    
    print("******************************************************")
    print(f"TOTAL REVENUE (ksh) :{total}")


#CREDITS

#salary

def honey_collection_salaries_director_2():
    """"collect all projects done, date commencment & date of completion where projects done by a particular bee (honey_collection)"""
    total = 0
    print("**********lOANS & SALARIES 2022************")
    cursor.execute("""SELECT pesa_funds.funds_date,pesa_funds.co_sub_type,pesa_funds.amount FROM pesa_funds WHERE pesa_funds.typology = "BRIAN" AND pesa_funds.co_sub_type = "SALARIES"  """)
    for index,row in enumerate(cursor.fetchall()):
        print(str(index + 1) + "." + str(row[0]) + " ** " + str(row[1]) + " ** " + str(row[2]))
        total += int(row[2])
    
    print("******************************************************")
    print(f"TOTAL REVENUE (ksh) :{total}")

def honey_collection_loans_director_2():
    """"collect all projects done, date commencment & date of completion where projects done by a particular bee (honey_collection)"""
    total = 0
    print("**********lOANS & SALARIES 2022************")
    cursor.execute("""SELECT pesa_funds.funds_date,pesa_funds.co_sub_type,pesa_funds.amount FROM pesa_funds WHERE pesa_funds.typology = "BRIAN" AND pesa_funds.co_sub_type = "LOANS"  """)
    for index,row in enumerate(cursor.fetchall()):
        print(str(index + 1) + "." + str(row[0]) + " ** " + str(row[1]) + " ** " + str(row[2]))
        total += int(row[2])
    print("******************************************************")
    print(f"TOTAL REVENUE (ksh) :{total}")





# Company debit


def funds_summary():
    """"collect all projects done, date commencment & date of completion where projects done by a particular bee (honey_collection)"""
    total_project_funds = 0
    company_funds = 0
    salaries = 0
    tax = 0
    print("**********PROJECTS COMPLETED 2022************")
    cursor.execute("""SELECT project_funds.project_fund,project_funds.company_fund,project_funds.salaries,project_funds.tax FROM project_funds """)
    for index,row in enumerate(cursor.fetchall()):
        print(str(index + 1) + "." + str(row[0]) + " ** " + str(row[1]) + " ** " + str(row[2]) + " ** " + str(row[3]))
        total_project_funds += int(row[0])
        company_funds += int(row[1])
        salaries += int(row[2])
        tax += int(row[3])
        
    
    print("******************************************************")
    print(f"TOTAL PROJECT FUNDS (ksh) :{(total_project_funds * 110)}")
    print(f"TOTAL COMPANY FUNDS (ksh) :{(company_funds * 110)}")
    print(f"SALARIES (ksh) :{(salaries * 110)}")
    print(f"TAX (ksh) :{(tax * 110)}")


def salary_summary():
    """"collect all projects done, date commencment & date of completion where projects done by a particular bee (honey_collection)"""
    director_1 = 0
    director_2 = 0
    employee_3 = 0
    employee_4 = 0
    employee_5 = 0
    employee_6 = 0
    
    print("**********SALARIES OVERVIEW************")
    cursor.execute("""SELECT salaries_funds.director_1,salaries_funds.director_2,salaries_funds.employee_3,salaries_funds.employee_4,salaries_funds.employee_5,salaries_funds.employee_6 FROM salaries_funds """)
    for index,row in enumerate(cursor.fetchall()):
        director_1 += int(row[0])
        director_2 += int(row[1])
        employee_3 += int(row[2])
        employee_4 += int(row[3])
        employee_5 += int(row[4])
        employee_6 += int(row[5])

    
    
    print(f" director-1 (symon):{(director_1 * 110)}")
    print(f" director_2 (Brian):{(director_2 * 110)}")
    print(f" employee_3 (Winny) :{(employee_3 * 110)}")
    print(f" employee_4 (Jeff_Koduk) :{(employee_4 * 110)}")
    print(f" employee_5 (James_Kuria) :{(employee_5 * 110)}")
    print(f" employee_6 (Mutiso) :{(employee_6 * 110)}")
    print("******************************************************")
    print(f" Total:{((director_1 + director_2 + employee_3 + employee_4 + employee_5 + employee_6) * 110)}")


salary_summary()


def company_fund():
    """"collect all projects done, date commencment & date of completion where projects done by a particular bee (honey_collection)"""
    total = 0
    print("**********PROJECTS COMPLETED 2022************")
    cursor.execute("""SELECT project_details.project_name,project_details.date_completion,project_funds.company_fund FROM project_details,project_funds WHERE project_details.project_name = project_funds.project_name AND project_details.project_status = "COMPLETE" """)
    for index,row in enumerate(cursor.fetchall()):
        print(str(index + 1) + "." + str(row[0]) + " ** " + str(row[1]) + " ** " + str(row[2]))
        total += int(row[2])
    
    print("******************************************************")
    print(f"TOTAL REVENUE (dollars) :{total}")
    total_ksh = total * 110
    print(f"TOTAL REVENUE (ksh) :{total_ksh}")




def exchange_rate_income():
    """Sum of all loans repayed"""
    total = 0
    print("**********EXCHANGE RATE INCOME************")
    cursor.execute("""SELECT pesa_funds.funds_date,pesa_funds.co_sub_type,pesa_funds.er_income FROM pesa_funds WHERE pesa_funds.currency = "DOLLAR" AND pesa_funds.co_sub_type = "PROJECTS" """)
    for index,row in enumerate(cursor.fetchall()):
        print(str(index + 1) + "." + str(row[0]) + " ** " + str(row[1]) + " ** " + str(row[2]))
        total += int(row[2])
    
    print("******************************************************")
    print(f"TOTAL REVENUE (ksh) :{total}")



def repayed_loans():
    """Sum of all loans repayed"""
    total = 0
    print("**********REPAYED LOANS************")
    cursor.execute("""SELECT pesa_funds.funds_date,pesa_funds.co_sub_type,pesa_funds.amount FROM pesa_funds WHERE pesa_funds.co_sub_type = "R_LOANS" """)
    for index,row in enumerate(cursor.fetchall()):
        print(str(index + 1) + "." + str(row[0]) + " ** " + str(row[1]) + " ** " + str(row[2]))
        total += int(row[2])
    
    print("******************************************************")
    print(f"TOTAL REVENUE (ksh) :{total}")






def running_cost():
    total = 0
    print("**********RUNNING COST************")
    cursor.execute("""SELECT pesa_funds.funds_date,pesa_funds.co_sub_type,pesa_funds.typology,pesa_funds.amount FROM pesa_funds WHERE pesa_funds.co_sub_type = "RUNNING_COST" """)
    for index,row in enumerate(cursor.fetchall()):
        print(str(index + 1) + "." + str(row[0]) + " ** " + str(row[1]) + " ** " + str(row[2]) + " ** " + str(row[3]))
        total += int(row[3])
    
    print("******************************************************")
    print(f"TOTAL REVENUE (ksh) :{total}")




def unpayed_loans():
    total = 0
    print("**********LOANS************")
    cursor.execute("""SELECT pesa_funds.funds_date,pesa_funds.co_sub_type,pesa_funds.typology,pesa_funds.amount FROM pesa_funds WHERE pesa_funds.co_sub_type = "LOANS" """)
    for index,row in enumerate(cursor.fetchall()):
        print(str(index + 1) + "." + str(row[0]) + " ** " + str(row[1]) + " ** " + str(row[2]) + " ** " + str(row[3]))
        total += int(row[3])
    
    print("******************************************************")
    print(f"TOTAL REVENUE (ksh) :{total}")



