from parameters import client_name
from parameters import project_setup
from parameters import project_date
from parameters import project_name
from parameters import project_funds
from parameters import project_funds_distribution
from parameters import time_id

from database import create_tables
from database import insert_project_funds_table
from database import insert_project_details_table
from database import insert_into_pesafunds
from database import view_salary
from database import view_projects
from database import alter_table
from database import active_projects
from database import mark_active_complete
from database import retrieve_source_user
from database import delete_from_pesafunds, net_fund,income_breakdown


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
    else:
        project_fund = 0
        date_completion = None

    # project user
    filename = "files/project_done_by.csv"
    filetype = "project bee"
    project_user = project_setup(filename, filetype)

    # project name ( project key/unique identifier)
    name_project = project_name(date_commencement, name_client, str.lower(project_category))

    # project funds
    company_fund, brian_income, symon_income, other_income, tax = project_funds_distribution(project_source,
                                                                                             project_user,
                                                                                             project_fund)

    # feeding to the database
    create_tables()
    insert_project_details_table(name_client, project_category, project_source, project_scope,
                                 date_commencement,
                                 date_completion, name_project, project_status)
    insert_project_funds_table(name_project, project_user, project_fund, company_fund, brian_income,
                               symon_income,
                               other_income, tax)


def view_active_projects():
    option = active_projects()
    # project completion date
    print("\n****PROJECT DATE COMPLETION*****")
    date_completion = project_date()

    # project fund
    project_fund = project_funds()
    project_source, project_user = retrieve_source_user(option)

    # project funds
    company_fund, brian_income, symon_income, other_income, tax = project_funds_distribution(project_source,
                                                                                                 project_user,
                                                                                                 project_fund)

    mark_active_complete(option, date_completion, project_fund, company_fund, symon_income, brian_income,
                             other_income, tax)


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
            projects_income_dollars = int(input("insert income:"))
            rate = float(input("input $/ksh exchange rate:"))
            amount = projects_income_dollars * 100
            er_income = projects_income_dollars * (rate - 100)

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

    funds = (time_key, funds_date, co_fund_type, co_sub_type, typology, currency, amount, er_income)

    insert_into_pesafunds(time_key, funds_date, co_fund_type, co_sub_type, typology, currency, amount, er_income)
    net_fund()



def formode_funds():
    """controlling fuds in the wallet"""
    correct = True
    while correct:
        print("*******FORMODE FUNDS**************")
        print("1) Add funds to wallet\n"
              "2) Check net-funds\n"
              "3) Check total-income\n"
              "4) Check total-expenditure\n"
              "5) Delete funds\n"
              "6) Quit")
        print("**********************************")
        user_selection = int(input("insert option: "))

        if user_selection == 1:
            add_to_pesafunds()
        elif user_selection == 2:
            net_fund()
        elif user_selection == 3:
            income_breakdown()
        elif user_selection == 4:
            print("coming soon")
        elif user_selection == 5:
            delete_from_pesafunds()
        elif user_selection == 6:
            correct = False
            print("""Consistency is a key element, without which a leader is incapable of getting respect, 
            success or even developing confidence in others.\nThank you!""")

        else:
            print("Wrong input, try again")


