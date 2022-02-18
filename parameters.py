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
        print("\nNote the name should be:\n"
              "1. Small caps\n"
              "2. first and surname should be joined by hyphen\n"
              "3. numbers are allowed")
        name = str.lower(input("\nclient's name:"))

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


def project_category():
    """establish the category by reading through the csv file and recording to a
    dictionary for the user to choose"""
    global purpose
    import csv
    category_dict = {}
    print("\n****PROJECT CATEGORY*****")
    with open("files/project_category.csv", "r") as f:
        iterable = csv.reader(f)
        list_iterable = list(iterable)
        for x in list_iterable:
            print(f"{x[0]}. {x[1]}")
            category_dict[int(x[0])] = x[1]
    user_selection = int(input("Insert category option above: "))
    for x in category_dict:
        if user_selection == x:
            purpose = category_dict[x]
    return purpose


def project_source():
    """establish project source"""
    global purpose
    import csv
    category_dict = {}
    print("\n****PROJECT SOURCE*****")
    with open("files/project_source.csv", "r") as f:
        iterable = csv.reader(f)
        list_iterable = list(iterable)
        for x in list_iterable:
            print(f"{x[0]}. {x[1]}")
            category_dict[int(x[0])] = x[1]
    user_selection = int(input("Insert option above: "))
    for x in category_dict:
        if user_selection == x:
            purpose = category_dict[x]
    return purpose


def project_scope():
    global purpose
    import csv
    category_dict = {}

    print("\n****PROJECT SCOPE*****")
    with open("files/project_scope.csv", "r") as f:
        iterable = csv.reader(f)
        list_iterable = list(iterable)
        for x in list_iterable:
            print(f"{x[0]}. {x[1]}")
            category_dict[int(x[0])] = x[1]
    user_selection = int(input("Insert option above: "))
    for x in category_dict:
        if user_selection == x:
            purpose = category_dict[x]
    return purpose


def project_done_by():
    global purpose
    import csv

    category_dict = {}
    print("\n****PROJECT DONE BY*****")

    with open("files/project_done_by.csv", "r") as f:
        iterable = csv.reader(f)
        list_iterable = list(iterable)
        for x in list_iterable:
            print(f"{x[0]}. {x[1]}")
            category_dict[int(x[0])] = x[1]
    user_selection = int(input("Insert option above: "))
    for x in category_dict:
        if user_selection == x:
            purpose = category_dict[x]
    return purpose


def project_total_fund(doneby):
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
        remainder = project_fund -company_fund
        brian_income = int(input("amount : "))
        symon_income = int(input("amount : "))

    elif doneby == "OTHER":
        company_fund = (project_fund / 100) * 10
        other_fund = project_fund - company_fund

    funds = (project_fund, company_fund, brian_income, symon_income, other_income)
    return funds

def project_name(date,client_name,category):
    """establish the name of the project, should be used as primary key"""
    prjt_name = str(date)+"_"+str(client_name)+"_"+str(category)
    return prjt_name



