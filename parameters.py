# record the commencement and completion date
def project_date():
    """generate the date object at time of the recording"""
    global current_date
    from datetime import date
    print("Insert \n"
          "1) Today's date\n"
          "2) Custom date")

    user_option = int(input("insert: "))

    if user_option == 1:
        current_date = date.today()

    elif user_option == 2:
        custom_date = int(input("date:"))
        custom_month = int(input("month:"))
        custom_year = int(input("year"))

        current_date = date(custom_year, custom_month, custom_date)
    return current_date


# record the client name

def client_name():
    """record the client name for the project"""
    global name
    print("\n****NAME OF CLIENT****")
    correct = True
    while correct:
        name = str.lower(input("insert name:"))

        if " " in name:
            correct = True
            print("first and surname should be joined by hyphen\n"
                  "check instructions")
        elif name is None:
            correct = True
            print("a project must have a client, how do you pay bills, without him?")

        else:
            correct = False

    return name

def project_setup(filename, filetype):
    """establish project source"""
    global purpose
    import csv
    from configurations import project_configuration

    file_type_upper = str.upper(filetype)

    try_again = True
    while try_again:
        category_dict = {}
        print(f"\n****{file_type_upper}*****")
        with open(filename, "r") as f:
            iterable = csv.reader(f)
            list_iterable = list(iterable)
            for x in list_iterable:
                print(f"{x[0]}. {x[1]}")
                category_dict[int(x[0])] = x[1]
            print("0. (modify list)")
        user_selection = int(input("Insert option above: "))

        for x in category_dict:
            if user_selection == x:
                purpose = category_dict[x]
                try_again = False
                return purpose
        if user_selection == 0:
            project_configuration(filename, filetype)


def project_funds(doneby):
    """The total amount payable for the particular project
    The """
    print("\n****PROJECT FUND*****")

    project_fund = int(input("Insert project fund in dollars:"))
    company_fund = 0
    brian_income = 0
    symon_income = 0
    other_income = 0
    if doneby == "BRIAN":
        company_fund = (project_fund / 100) * 50
        brian_income = project_fund - company_fund
    elif doneby == "SYMON":
        company_fund = (project_fund / 100) * 50
        symon_income = project_fund - company_fund

    elif doneby == "SYMON-BRIAN":
        company_fund = (project_fund / 100) * 50
        remainder = project_fund - company_fund
        brian_income = int(input("amount : "))
        symon_income = int(input("amount : "))

    elif doneby == "OTHER":
        company_fund = (project_fund / 100) * 10
        other_fund = project_fund - company_fund

    funds = (project_fund, company_fund, brian_income, symon_income, other_income)
    return funds


def project_name(date, client_name, category):
    """establish the name of the project, should be used as primary key"""
    prjt_name = str(date) + "_" + str(client_name) + "_" + str(category)
    return prjt_name
