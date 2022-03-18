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
from database import insert_pesa_funds_table
from database import view_salary
from database import view_projects
from database import alter_table
from database import active_projects
from database import mark_active_complete
from database import retrieve_source_user


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
    if option is None:
        print("Thanks")
    else:
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


def formode_funds():
    """This section controls how the company funds are distributed and used """
    # primary key
    time_key = time_id()

    # date of funding
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
            projects_income = int(input("insert project income:"))
            er_income = 0

        elif currency == "DOLLAR":
            # Amount of income
            print(f"\n**** AMOUNT OF INCOME({currency})*****")
            projects_income_dollars = int(input("insert income:"))
            rate = int(input("input $/ksh exchange rate:"))
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

    insert_pesa_funds_table(time_key, funds_date, co_fund_type, co_sub_type, typology, currency, amount, er_income)

