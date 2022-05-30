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
    project_doneby text ,
    project_fund integer NOT NULL,
    company_fund integer NOT NULL,
    symon_income integer NOT NULL,
    brian_income integer NOT NULL,
    other_income integer NOT NULL,
    tax integer NOT NULL);""")

    # pesa_funds table
    cursor.execute("""CREATE TABLE IF NOT EXISTS pesa_funds(
        time_id text PRIMARY KEY,
        funds_date text NOT NULL,
        co_fund_type text NOT NULL,
        co_sub_type text NOT NULL,
        typology text,
        currency text NOT NULL,
        amount integer NOT NULL,
        er_income integer);""")

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


def alter_null_option():
    """Add column to a table"""
    print("******CHANGE COLUMN FROM NOT NULL TO NULL******")
    table_name = input("name of table:")
    column_name = input("name of column:")
    cursor.execute(f"""ALTER TABLE {table_name} MODIFY {column_name} columnType NULL;""")



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
        print(" 0.Go back")

        select_month = int(input("\nselect option: "))

        if select_month == 0:
            correct = False

        elif select_month in range(1, 13):
            company_sum = 0
            symon_sum = 0
            brian_sum = 0
            employee_sum = 0
            total_fund = 0

            # (date_completion,company_fund,symon_income,brian_income,other_income)

            cursor.execute("""SELECT project_details.date_completion, project_funds.company_fund,
            project_funds.symon_income,project_funds.brian_income,project_funds.other_income FROM project_funds, 
            project_details WHERE project_funds.project_name = project_details.project_name """)
            for row in cursor.fetchall():
                if row[0] is not None:
                    date_completion = row[0]
                    month = int(date_completion[5:7])
                    company_fund = row[1]
                    symon_income = row[2]
                    brian_income = row[3]
                    other_income = row[4]

                    if month == select_month:
                        company_sum += company_fund
                        symon_sum += symon_income
                        brian_sum += brian_income
                        employee_sum += other_income

            year = {1: "JANUARY", 2: "FEBRUARY", 3: "MARCH", 4: "APRIL", 5: "MAY", 6: "JUNE", 7: "JULY", 8: "AUGUST",
                    9: "SEPTEMBER", 10: "OCTOBER", 11: "NOVEMBER", 12: "DECEMBER", 0: "CLOSED"}

            print(f"\n******INCOME STATS {str.upper(year[select_month])}*******")

            print(f"COMPANY FUND = ${round(company_sum, 1)}")
            print(f"SYMON INCOME = ${round(symon_sum, 1)}")
            print(f"BRIAN INCOME = ${round(brian_sum, 1)}")
            print(f"EMPLOYEE INCOME = ${round(employee_sum, 1)}")

            print("********************************")
            print(f"TOTAL FUND = ${round((company_sum + symon_sum + brian_sum + employee_sum), 1)}\n")

        else:
            print("Guess you live in mars.There are 12 months here on Earth,try again.")


def view_projects():
    """View all projects in the database"""

    print("\n**************************************SELECT PROJECTS********************************")
    # months dictionary
    year = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun", 7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct",
            11: "Nov", 12: "Dec"}

    # loop through the month
    for months in year:
        print(f"{months}.{year[months]}", end="  ")
    print("\n")
    select_month = int(input("select month: "))

    year = {1: "JANUARY", 2: "FEBRUARY", 3: "MARCH", 4: "APRIL", 5: "MAY", 6: "JUNE", 7: "JULY", 8: "AUGUST",
            9: "SEPTEMBER", 10: "OCTOBER", 11: "NOVEMBER", 12: "DECEMBER"}

    print(
        f"\n*****************************PROJECTS COMPLETED ON {year[select_month]} *******************************")
    # Print projects
    projects = {}
    revenue_sum =0
    cursor.execute("""SELECT project_details.project_name,project_details.date_completion,project_funds.project_fund
     FROM project_details,project_funds WHERE project_details.project_name =project_funds.project_name""")
    
    for index, row in enumerate(cursor.fetchall()):
        value = row[0]
        date = row[1]
        funds = row[2]
        #revenue after taxation
        revenue = (funds * 0.8)

        # filter incomplete projects
        if date is not None:
            list_date = list(date)
            month = int(list_date[5] + list_date[6])

            if month == select_month:
                num = index + 1
                projects[num] = value
                print(f"{index + 1}. {value}--{funds} ")
                revenue_sum += revenue

    print("0. Go back")
    print("**************************************************************************************")
    print(f"REVENUE : {revenue_sum}")

    # select projects to be edited
    project_index_sel = int(input("select project: "))

    #return back
    if project_index_sel == 0:
        return None

    else:
        pj_name = projects[project_index_sel]
        print(f"\n****************{str.upper(pj_name)} MODIFICATION **************")
        print("1) Delete project\n"
          "2) Edit project parameters")
        user_select = int(input("user option:"))

        if user_select == 1:
            # delete from project funds
            cursor.execute("""DELETE FROM project_funds WHERE project_name =?""", [pj_name])
            # delete from project details
            cursor.execute("""DELETE FROM project_details WHERE project_name =?""", [pj_name])
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
        return 0

    else:
        selected_project = projects[selection]
        print(f"{selected_project} marked complete")
        return selected_project


def retrieve_source_user(data):
    """retrieve source and user of the selected project"""
    cursor.execute("""SELECT project_details.project_source FROM project_details WHERE project_details.project_name=?""", [data])

    for row in cursor.fetchall():
        values = row[0]
        return values


def mark_active_complete(project_name, project_doneby, date_completion, project_fund, company_fund, symon_income, brian_income,
                         other_income,
                         tax):
    """" mark project complete """
    # update project_details table
    cursor.execute("""UPDATE project_details SET project_status = 'COMPLETE', date_completion = ? 
    WHERE project_name = ?""", [date_completion, project_name])

    # update project_funds table
    cursor.execute("""UPDATE project_funds SET project_doneby=?,project_fund=?,company_fund=?,symon_income=?,
    brian_income=?,other_income=?,tax=? WHERE project_name = ?""",
                   [project_doneby,project_fund, company_fund, symon_income, brian_income,
                    other_income, tax, project_name])
    print("project updated completely")
    db.commit()


################## PESA FUNDS TABLE ##########################


def insert_into_pesafunds(time_id, funds_date, co_fund_type, co_sub_type, typology, currency,
                          amount, er_income):
    """insert data into project_funds_table"""
    # insert into project_funds table
    cursor.execute("""INSERT INTO pesa_funds(time_id,funds_date,co_fund_type,co_sub_type,typology,
    currency,amount,er_income)
                                    VALUES(?,?,?,?,?,?,?,?)""", (time_id, funds_date, co_fund_type, co_sub_type,
                                                                 typology, currency, amount, er_income))
    print("pesa funds details added successfully")
    db.commit()


def delete_from_pesafunds():
    """insert item to be deleted from pesa funds"""
    id = str(input("insert id: "))
    cursor.execute("""DELETE FROM pesa_funds WHERE time_id =?""", [id])
    cursor.fetchall()

    print(f"{id} has been deleted")
    db.commit()


def net_fund():
    """The difference between the income and expenditure"""
    print(
        f"\n*****************************FUND STATS**************************************")
    total_income = 0
    total_expenditure = 0
    cursor.execute("""SELECT co_fund_type,amount,er_income FROM pesa_funds""")
    for index, row in enumerate(cursor.fetchall()):
        co_fund_type = row[0]
        amount = int(row[1])
        er_income = int(row[2])

        if co_fund_type == "INCOME":
            total_income += (amount + er_income)
        elif co_fund_type == "EXPENDITURE":
            total_expenditure += (amount + er_income)
        else:
            print("wrong input")

    net_funds = total_income - total_expenditure
    print(f"total income:ksh {total_income}")
    print(f"total expenditure:Ksh {total_expenditure}")
    print(f"Net fund:ksh {net_funds}")

    print("*****************************************************************************\n")


def income_breakdown():
    """breakdown income into respective sources"""


    # VARIABLES
    er_income_total = 0
    fiverr_total = 0
    physical_total = 0
    repayed_loans_total = 0
    competition_total = 0

    print("\n**************************************SELECT MONTH**********************************************")
    # months dictionary
    year = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun", 7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct",
            11: "Nov", 12: "Dec"}

    # loop through the month
    for months in year:
        print(f"{months}.{year[months]}", end="  ")
    print(" 0.Go back")

    select_month = int(input("select month: "))

    year = {1: "JANUARY", 2: "FEBRUARY", 3: "MARCH", 4: "APRIL", 5: "MAY", 6: "JUNE", 7: "JULY", 8: "AUGUST",
            9: "SEPTEMBER", 10: "OCTOBER", 11: "NOVEMBER", 12: "DECEMBER"}

    print(f"\n************INCOME ON {year[select_month]} (AMOUNT DEPOSITED TO BANK ACCOUNT) ***************")

    cursor.execute("""SELECT funds_date, co_fund_type,co_sub_type,currency,amount,er_income FROM pesa_funds""")
    for index, row in enumerate(cursor.fetchall()):
        date = row[0]
        co_fund_type = row[1]
        co_sub_type = row[2]
        currency = row[3]
        amount = int(row[4])
        er_income = int(row[5])

        # filter incomplete projects, remain with apppropiate month
        if date is not None:
            list_date = list(date)
            month = int(list_date[5] + list_date[6])
            if month == select_month:

                # filter expenditure,remain with income
                if co_fund_type == "INCOME":
                    # filter,remain with projects
                    if co_sub_type == "PROJECTS":
                        if currency == "DOLLAR":
                            fiverr_total += amount
                            er_income_total += er_income
                        elif currency == "KSH":
                            physical_total += amount
                    elif co_sub_type == "R_LOANS":
                        repayed_loans_total += amount

    print("\n***********PROJECTS ************")
    print(f"FIVERR PROJECTS: {fiverr_total}/=\nPHYSICAL PROJECTS : {physical_total}/=\nCOMPETITION PROJECTS : {competition_total}/=")
    print("********************************")
    projects_total = fiverr_total + physical_total + competition_total
    print(f"PROJECTS TOTAL:{projects_total}/=")

    print(f"EXCHANGE RATE INCOME : {er_income_total}/=")
    print(f"REPAYED LOANS : {repayed_loans_total}/=")
    
    total_income = projects_total + repayed_loans_total + er_income_total
    print("\n*********************************************************************************")
    print(f"TOTAL INCOME: {total_income}/=")

def income_summary():
    "summary of income 2022"
    print(f"\n*****************************INCOME SUMMARY 2022 *********************************")
    total_income = 0
    fiverr_total = 0
    physical_total = 0
    r_loans_total = 0
    er_total = 0
    cursor.execute("""SELECT co_fund_type,co_sub_type,currency,amount,er_income FROM pesa_funds""")
    for index, row in enumerate(cursor.fetchall()):
        co_fund_type = row[0]
        co_sub_type = row[1]
        currency = row[2]
        amount = int(row[3])
        er_income = int(row[4])

        if co_fund_type == "INCOME":
            if co_sub_type == "PROJECTS":
                if currency == "DOLLAR":
                    fiverr_total += amount
                    er_total += er_income
                elif currency == "KSH":
                    physical_total += amount

            elif co_sub_type == "R_LOANS":
                r_loans_total += amount

    total_income = fiverr_total + er_total + physical_total + r_loans_total

    print(f"fiverr_total:ksh {fiverr_total}")
    print(f"exchange rate_total:Ksh {er_total}")
    print(f"physical_total:ksh {physical_total}")
    print(f"re-payed loans:ksh {r_loans_total}")
    print("**************************************************************************")
    print(f"total_income:ksh {total_income}\n")



def expenditure_breakdown():
    """breakdown expenditure into salaries, running cost, loans for every 
    particular month, have an option that shows the total sum of running cost, salaries and loans"""


    # SALARIES VARIABLES
    brian_salary= 0
    symon_salary = 0
    employee_salary = 0

    # RUNNING COST VARIABLES
    rent_cost = 0
    electricity_cost = 0
    internet_cost = 0
    gas_cost = 0
    domain_cost = 0
    e_purchase_repair_cost = 0
    co_registration_cost = 0
    retreat_cost = 0
    csr_cost = 0
    shopping_cost = 0

    # LOAN COAST VARIABLES
    malcom_loan  = 0
    brian_loan = 0

    print("\n**************************************SELECT MONTH**********************************************")
    # months dictionary
    year = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun", 7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct",
            11: "Nov", 12: "Dec"}

    # loop through the month
    for months in year:
        print(f"{months}.{year[months]}", end="  ")
    print(" 0.Go back")

    select_month = int(input("select month: "))

    year = {1: "JANUARY", 2: "FEBRUARY", 3: "MARCH", 4: "APRIL", 5: "MAY", 6: "JUNE", 7: "JULY", 8: "AUGUST",
            9: "SEPTEMBER", 10: "OCTOBER", 11: "NOVEMBER", 12: "DECEMBER"}

    print(f"\n************{year[select_month]} EXPENDITURE ***************\n")

    cursor.execute("""SELECT funds_date, co_fund_type,co_sub_type,typology,amount FROM pesa_funds""")
    for index, row in enumerate(cursor.fetchall()):
        date = row[0]
        co_fund_type = row[1]
        co_sub_type = row[2]
        typology = row[3]
        amount = int(row[4])

        # filter incomplete projects, remain with apppropiate month
        if date is not None:
            list_date = list(date)
            month = int(list_date[5] + list_date[6])
            if month == select_month:

                # filter income,remain with expenditure
                if co_fund_type == "EXPENDITURE":
                    # filter,remain with salaries
                    if co_sub_type == "SALARIES":
                        if typology == "SYMON":
                            symon_salary += amount
                        elif typology == "BRIAN":
                            brian_salary += amount
                        elif typology == "EMPLOYEE":
                            employee_salary += amount
                    #filter,remain with running cost
                    elif co_sub_type == "RUNNING_COST":
                        if typology == "RENT":
                            rent_cost += amount
                        elif typology == "ELECTRICITY":
                            electricity_cost += amount
                        elif typology == "INTERNET":
                            internet_cost += amount
                        elif typology == "RETREAT":
                            retreat_cost += amount
                        elif typology == "DOMAIN":
                            domain_cost += amount
                        elif typology == "SHOPPING":
                            shopping_cost += amount
                        elif typology == "GAS":
                            gas_cost += amount
                        elif typology == "CSR":
                            csr_cost += amount
                        elif typology == "E-PURCHASE_REPAIR":
                            e_purchase_repair_cost += amount
                        elif typology == "C0-REGISTRATION":
                            co_registration_cost += amount

                    #filter, remain with loans
                    elif co_sub_type == "LOANS":
                        if typology == "MALCOM":
                            malcom_loan += amount
                        elif typology == "BRIAN":
                            brian_loan += amount


    print("***********SALARIES ************")
    print(f"BRIAN : {brian_salary}/=\nSYMON : {symon_salary}/=\nEMPLOYEE : {employee_salary}/=")
    print("********************************")
    total_salaries = brian_salary + symon_salary + employee_salary
    print(f"TOTAL:{total_salaries}/=")


    print("\n***********RUNNING COST ********")
    print(f"RENT : {rent_cost}/=\nELECRICTY : {electricity_cost}/=\nINTERNET : {internet_cost}/=\nGAS : {gas_cost}/=\nDOMAIN : {domain_cost}/=\nE-PURCHASE_REPAIR : {e_purchase_repair_cost}/=\nC0_REGISTRATION : {co_registration_cost}/=\nRETREAT : {retreat_cost}/=\nCSR : {csr_cost}/=\nSHOPPING : {shopping_cost}/=")
    print("********************************")
    total_running_cost = rent_cost + electricity_cost + internet_cost + gas_cost + domain_cost + e_purchase_repair_cost + co_registration_cost + retreat_cost + csr_cost + shopping_cost
    print(f"TOTAL:{total_running_cost}/=")

    print("\n***********LOANS ***************")
    print(f"BRIAN : {brian_loan}/=\nMALCOM : {malcom_loan}/=")
    print("********************************")
    total_loans = brian_loan + malcom_loan
    print(f"TOTAL:{total_loans}/=")

    print("\n**********************************************")
    cumulative_total = total_salaries + total_running_cost + total_loans
    print(f"TOTAL EXPENDITURE :{cumulative_total}/=")
