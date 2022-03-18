
from parameters import project_date, project_setup


def formode_funds():

    """This section controls how the company funds are distributed and used """
    # date of funding
    Funds_date = project_date()

    # co_fund_type
    filename = "files/co_fund_type.csv"
    filetype = "company Fund type"
    co_fund_type = project_setup(filename, filetype)

    if co_fund_type == "INCOME":
        # co_income
        filename = "files/co_income_type.csv"
        filetype = "company Income type"
        co_income_type = project_setup(filename, filetype)

    elif co_fund_type == "EXPENDITURE":
        filename = "files/co_expenditure_type.csv"
        filetype = "company Expenditure type"
        co_expenditure_type = project_setup(filename, filetype)

        if co_expenditure_type == "SALARIES":
            filename = "files/co_salaries_allocation.csv"
            filetype = "Company Salaries Allocation"
            co_salaries_employee = project_setup(filename, filetype)

        elif co_expenditure_type == "RUNNING_COST":
            filename = "files/co_run_cost_type.csv"
            filetype = "Company Running Cost type"
            co_run_cost_type = project_setup(filename, filetype)

        elif co_expenditure_type == "LOANS":
            filename = "files/co_loan_allocation.csv"
            filetype = "Company Loan Allocation"
            co_loan_allocation = project_setup(filename, filetype)


formode_funds()












