from parameters import client_name
from parameters import project_setup
from parameters import project_setup_cooperation
from parameters import project_date
from parameters import project_name
from parameters import project_funds
from parameters import project_funds_distribution_V2
from parameters import time_id
from parameters import salaries_matrix
from parameters import dollars_ksh

from database import create_tables
from database import insert_project_funds_table
from database import insert_project_details_table
from database import insert_salaries_funds_table
from database import insert_into_pesafunds
from database import retrieve_project_quote
from database import view_projects
from database import alter_table
from database import active_projects

from database import update_project_details_table
from database import update_project_funds_table
from database import update_salaries_table
from database import retrieve_source_user
from database import delete_from_pesafunds, net_fund,income_breakdown,expenditure_breakdown

import csv

def add_project_to_database():
    """adding project to database"""
    # Collecting the parameters

    # project category
    name_client = client_name()

    # project category
    filename = "files/project_category.csv"
    filetype = "project category"
    project_category = project_setup(filename, filetype)

    # project source
    filename = "files/project_source.csv"
    filetype = "project source"
    project_source = project_setup(filename, filetype)

    # project scope
    filename = "files/project_scope.csv"
    filetype = "project scope"
    project_scope = project_setup(filename, filetype)

    # project commencement date
    print("\n****PROJECT DATE COMMENCEMENT*****")
    date_commencement = project_date()

    # project status
    filename = "files/project_status.csv"
    filetype = "project status"
    project_status = project_setup(filename, filetype)

    if project_status == "COMPLETE":
        # project completion date
        print("\n****PROJECT DATE COMPLETION*****")
        date_completion = project_date()

        # project fund
        project_fund = project_funds()

        # project user
        filename = "files/project_done_by.csv"
        filetype = "project bee"
        project_user = project_setup(filename, filetype)




    else:
        if project_source == "PHYSICAL":
            print ("\n***funds in ksh****")
            project_fund = project_funds()
            exchange_rate = 110
            project_fund = round(project_fund/exchange_rate)
        else:
            project_fund = project_funds()

        date_completion = None
        project_user = "FORMODE"

        director_1 = 0
        director_2 = 0
        employee_3 = 0
        employee_4 = 0
        employee_5 = 0
        employee_6 = 0

    
    # project name ( project key/unique identifier)
    name_project = project_name(date_commencement, name_client, str.lower(project_category))

    # project funds
    company_fund, salaries, tax = project_funds_distribution_V2(project_source, project_fund)

    # feeding to the database
    create_tables()
    insert_project_details_table(name_client, project_category, project_source, project_scope,
                                 date_commencement,
                                 date_completion, name_project, project_status)
    insert_project_funds_table(name_project, project_fund, company_fund, salaries, tax)

    insert_salaries_funds_table(name_project, project_user, director_1, director_2, employee_3, employee_4, employee_5, employee_6)


def view_active_projects():


    print("************ACTIVE PROJECTS**********")
    print("1. View project Quote\n2. Mark project Complete")
    print("************************************")
    user_input = int(input("insert option: "))

    if user_input == 1:
        option = active_projects()
        if option == 0:
            return None
        else:
            retrieve_project_quote(option)

    elif user_input == 2:
        option = active_projects()
        if option == 0:
            return None
        else:
            # project completion date
            print("\n****PROJECT DATE COMPLETION*****")
            date_completion = project_date()

            project_source = retrieve_source_user(option)
            # project fund

    
            if project_source == "PHYSICAL":
                print ("\n***funds in ksh****")
                project_fund = project_funds()
                exchange_rate = 110
                project_fund = round(project_fund/exchange_rate)
            else:
                project_fund = project_funds()
                
            
            company_fund, salaries, tax = project_funds_distribution_V2(project_source, project_fund)

            # update the database on the project details
            update_project_details_table(date_completion, option)

            # update the project funds details
            update_project_funds_table(option,project_fund,company_fund,salaries,tax)

            # project user
            print("\n*********PROJECT BEE TYPE*********")
            print(" 1. Single Bee\n 2. Colony of bees")

            user_input = int(input("insert option above: "))


            filename = "files/project_done_by.csv"
            filetype = "project bee"

            if user_input == 1:
                project_user = project_setup(filename, filetype)
                # check the index of the name in csv file(project _doneby) if it matches with the name picked
                director_1 = 0
                director_2 = 0
                employee_3 = 0
                employee_4 = 0
                employee_5 = 0
                employee_6 = 0

                #if indecise match, then you've identified the righht person, pay him/her salary
                with open(filename, "r") as f:

                    iterable = csv.reader(f)
                    list_iterable = list(iterable)
                    for x in list_iterable:
                        if x[1] == project_user:
                            bee_code = int(x[0])
                            if bee_code == 1:
                               director_1 = salaries
                            elif bee_code == 2:
                               director_2 = salaries
                            elif bee_code == 3:
                               employee_3 = salaries
                            elif bee_code == 4:
                               employee_4 = salaries
                            elif bee_code == 5:
                               employee_5 = salaries
                            elif bee_code == 6:
                               employee_6 = salaries
                            else:
                                print("new employer detected, kindly update his/her database.")
                # update salaries table in the database
                update_salaries_table(option,project_user,director_1,director_2,employee_3,employee_4,employee_5,employee_6)

            elif user_input == 2:
                project_user = "COOPERATE"
                bees_index = project_setup_cooperation(filename, filetype)
                salaries_distribution = salaries_matrix(filename,salaries,bees_index)

                director_1 = 0
                director_2 = 0
                employee_3 = 0
                employee_4 = 0
                employee_5 = 0
                employee_6 = 0

            
                # loop through the salaries distribution and allocate appropiately

                for x in salaries_distribution:            
                    if x == 1:
                        director_1 = salaries_distribution[x]
                    elif x == 2:
                        director_2 = salaries_distribution[x]
                    elif x == 3:
                        employee_3 = salaries_distribution[x]
                    elif x == 4:
                        employee_4 = salaries_distribution[x]
                    elif x == 5:
                        employee_5 = salaries_distribution[x]
                    elif x == 6:
                        employee_6 = salaries_distribution[x]
                    else:
                        print("Employee records not yet updated in the database.")

                # update salaries table in the database
                update_salaries_table(option,project_user,director_1,director_2,employee_3,employee_4,employee_5,employee_6)

def add_to_pesafunds():
    """This section controls how the company funds are distributed and used """
    # primary key
    time_key = time_id()

    # date of funding
    print("\n********DATE OF TRANSACTION****** ")
    funds_date = project_date()

    # co_fund_type
    filename = "files/co_fund_type.csv"
    filetype = "company Fund type"
    co_fund_type = project_setup(filename, filetype)

    # parameters
    co_sub_type = ""
    typology = ""
    currency = ""
    amount = 0
    er_income = 0

    # ****************INCOME******************
    if co_fund_type == "INCOME":
        # co_sub_type (income)
        filename = "files/co_income_type.csv"
        filetype = "company Income type"
        co_sub_type = project_setup(filename, filetype)

        # currency type
        filename = "files/currency.csv"
        filetype = "Type of currency"
        currency = project_setup(filename, filetype)

        if currency == "KSH":
            # Amount of income
            print(f"\n**** AMOUNT OF INCOME({currency})*****")
            amount = int(input("insert project income:"))
            er_income = 0

        elif currency == "DOLLAR":
            # Amount of income
            print(f"\n**** AMOUNT OF INCOME({currency})*****")
            amount, er_income = dollars_ksh()


    # ****************EXPENDITURE*****************

    elif co_fund_type == "EXPENDITURE":
        # co_sub_type (expenditure)
        filename = "files/co_expenditure_type.csv"
        filetype = "company Expenditure type"
        co_sub_type = project_setup(filename, filetype)

        if co_sub_type == "SALARIES":
            # typology salaries
            filename = "files/co_salaries_allocation.csv"
            filetype = "Company Salaries Allocation"
            typology = project_setup(filename, filetype)

        elif co_sub_type == "RUNNING_COST":
            # typology running_cost
            filename = "files/co_run_cost_type.csv"
            filetype = "Company Running Cost type"
            typology = project_setup(filename, filetype)

        elif co_sub_type == "LOANS":
            # typology loans
            filename = "files/co_loan_allocation.csv"
            filetype = "Company Loan Allocation"
            typology = project_setup(filename, filetype)

        # currency type
        filename = "files/currency.csv"
        filetype = "Type of currency"
        currency = project_setup(filename, filetype)

        # Amount expenditure
        amount = input("insert expenditure:")

    insert_into_pesafunds(time_key, funds_date, co_fund_type, co_sub_type, typology, currency, amount, er_income)
    net_fund()



def formode_funds():
    """controlling fuds in the wallet"""
    correct = True
    while correct:
        print("\n*******FORMODE FUNDS**************")
        print("1) Add funds to wallet\n"
              "2) Check net-funds\n"
              "3) Check total-income\n"
              "4) Check total-expenditure\n"
              "5) Delete funds\n"
              "0) Go back")
        print("**********************************")
        user_selection = int(input("insert option: "))

        if user_selection == 1:
            add_to_pesafunds()
        elif user_selection == 2:
            net_fund()
        elif user_selection == 3:
            income_breakdown()
        elif user_selection == 4:
            expenditure_breakdown()
        elif user_selection == 5:
            delete_from_pesafunds()
        elif user_selection == 0:
            correct = False
            print("""Consistency is a key element, without which a leader is incapable of getting respect, 
            success or even developing confidence in others.\nThank you!""")

        else:
            print("Wrong input, try again")


