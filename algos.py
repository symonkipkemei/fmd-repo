
import csv
from curses.ascii import isdigit
from datetime import date

#_____________________________________________________________________________________________________________#

def project_name(date, clientName, category):
    """establish the name of the project, should be used as primary key"""
    # date converted to string
    date_object = str(date)
    # date string abstracted to the 2 digits of the year,month and day
    record_date = date_object[2:4] + date_object[5:7] + date_object[8:10]
    prjt_name = record_date + "_" + str(clientName) + "_" + str(category)
    return prjt_name


def client_name()-> str:
    """record the client name for the project

    Returns:
        str: client name
    """
    
    global name
    print("\n client name")
    print("***************************************************")
    while True:
        name = str.lower(input("insert name:"))
        if " " in name:
            print("first and surname should be joined by hyphen\n")
        elif name is None:
            print("a project must have a client, how do you pay bills, without him/her?")
        else:
            break
    print("***************************************************")

    return name


# Date algorithim
def datetime_enforcer(description: str, lower_limit:int,upper_limit:int)-> int:
    """_summary_

    Args:
        description (str): enforces the input provided by the user; can be date, month or year
        lower_limit (int): it should not surpass this point
        upper_limit (int): it should not go above this point

    Returns:
        int: the correct value for date, month or year
    """
    while True:
        custom_date = input(f"{description}:")
        if custom_date.isdigit():
            custom_date = int(custom_date)
            if custom_date >= lower_limit and custom_date <= upper_limit :
                break
        print("Try again")
    return custom_date

def date_setup(date_purpose:str)-> str:
    """Set up the string format for a date

    Args:
        date_purpose (str): The description of the use of the date i.e commencment date, completion date

    Returns:
        str: date in str format
    """
    while True:
        print()
        print(f"{date_purpose}")
        print("***************************************************")
        print( "1) Today's date\n"
              "2) Custom date")
        print("___________________________________________________")
        user_option = input("insert: ")
        print("***************************************************")

        if user_option.isdigit():
            user_option = int(user_option)
            if user_option == 1:
                current_date = date.today()
                break
            elif user_option == 2:
                custom_date = datetime_enforcer("date", 1,31)
                custom_month = datetime_enforcer("month",1,12)
                custom_year = datetime_enforcer("year",2022,2022)
                print("***************************************************")
                current_date = date(custom_year, custom_month, custom_date)
                break
            else:
                print("Wrong input, try again.")
        else:
            print("Wrong input, try again.")

    # format date to string format 
    current_date =current_date.strftime('%Y-%m-%d %H:%M:%S')

    return current_date



## project fund algos
#_____________________________________________________________________________________________________________#

def money_setup(money_purpose):
    """Records all transactions done in kenya shillings"""
    print()
    print(f"{money_purpose}")
    print("***************************************************")
    amount = float(input("Amount:"))
    print("***************************************************")
    return amount


def project_fund(money_purpose, usd = True):
    """All project funds are recorded in usd

    Args:
        money_purpose (_type_): description of money type
        usd (bool, optional): if not true amount is converted from ksh to usd. Defaults to True.

    Returns:
        _type_: amount to be recorderd in usd
    """
    print()
    print(f"{money_purpose}")
    print("***************************************************")
    amount = float(input("Amount:"))
    print("***************************************************")
    if not usd:
        exchange_rate = 110
        amount = round(amount/exchange_rate)
    return amount


def project_funds_distribution_V2(project_source_id, project_fund):
    # client_fee (is the projectFund aggreed between the sellar and buyer)
    # real_fee ( fee visible to the world)
    # optical_fee (fee visible only by directors) 
    # distribution_factor ( factor that controls the amount of real_fee and optical fee)
    # formode_tax (amount the company makes for facilitating business)
    # fiverr_tax (amount fiverr deducts as profits)
    # project_bee_salary(amount payable to the project bee)

    # company_fund ( sum of formode_tax_o + formode_tax-r)
    # tax ( fiverr_tax_o + fiverr_tax_r)
    # symon_income ( director 1)
    # brian_income ( director 2)
    # other_income  (employee)

    if project_source_id == 1: #fiverr
        client_fee = float(project_fund)
        distribution_factor = (2/3) # distribution to reality
        real_fee = distribution_factor * client_fee
        
        # real_fee should always be a whole number rounded to 0 or 5 to make it convincing
        base = 5
        real_fee = base * round(real_fee /5)

        # optical illusion achieved
        optical_fee = client_fee - real_fee
        fiverr_tax_o = 0.2 * optical_fee
        formode_tax_o = optical_fee - fiverr_tax_o

        # back to reality
        fiverr_tax_r = 0.2 * real_fee
        project_bee_salary =round(0.7 * real_fee)
        formode_tax_r = ( real_fee - ( fiverr_tax_r + project_bee_salary))

        company_fund = formode_tax_o + formode_tax_r
        salaries = project_bee_salary
        tax = fiverr_tax_o + fiverr_tax_r

        # consultancies
        consultancies = 0

        funds = (company_fund,consultancies, salaries, tax, real_fee,formode_tax_r,fiverr_tax_r)
        
    elif project_source_id == 2: #physical
        client_fee = project_fund
        distribution_factor = (2/3) # distribution to reality
        real_fee = distribution_factor * client_fee
        
        # real_fee should always be a whole number rounded to 0 or 5 to make it convincing
        base = 5
        real_fee = base * round(real_fee /5)


        # optical illusion achieved
        optical_fee = client_fee - real_fee
        tax_charge = 0
        physical_tax_o = tax_charge * optical_fee
        formode_tax_o = optical_fee - physical_tax_o

        # back to reality
        # percentage of tax/100
        visible_tax = 0
        # amount of tax
        physical_tax_r = visible_tax * real_fee
        formode_tax_r = round(0.1 * real_fee)
        project_bee_salary = ( real_fee - ( formode_tax_r + physical_tax_r))


        company_fund = formode_tax_o + formode_tax_r
        salaries = project_bee_salary
        tax = physical_tax_o + physical_tax_r

        # consultancies
        consultancies = 0

        funds = (company_fund, consultancies, salaries, tax,real_fee,formode_tax_r,physical_tax_r)

    elif project_source_id == 3: #competition
        print("Gopillar projects yet to be factored")
    
    elif project_source_id == 5: #paypal
        client_fee = project_fund
        distribution_factor = (2/3) # distribution to reality
        real_fee = distribution_factor * client_fee
        
        # real_fee should always be a whole number rounded to 0 or 5 to make it convincing
        base = 5
        real_fee = base * round(real_fee /5)

        # optical illusion achieved
        optical_fee = client_fee - real_fee
        paypal_tax_o = 0.05 * optical_fee
        formode_tax_o = optical_fee - paypal_tax_o

        # back to reality
        paypal_tax_r = 0.05 * real_fee
        project_bee_salary =round(0.85 * real_fee)
        formode_tax_r = ( real_fee - ( paypal_tax_r + project_bee_salary))

        company_fund = formode_tax_o + formode_tax_r
        salaries = project_bee_salary
        tax = paypal_tax_o + paypal_tax_r

        # consultancies
        consultancies = 0

        funds = (company_fund,consultancies, salaries, tax,real_fee,formode_tax_r,paypal_tax_r)

    else:
        print("projects fund yet to be included")

    return funds


def dollars_ksh():
    # establish amount of dollars withdrawn
    dollars_withdrawn = float(input("insert amount withdrawn (dollars):"))
    amount_recieved = float(input("insert amount recieved (ksh):"))

    # establish an exchange rate fee a constant used for the project
    #anything above this becomes company's profit

    rate = 110

    # establish project amount ()
    project_amount = dollars_withdrawn * rate
    er_income = amount_recieved - project_amount

    money = (project_amount, er_income)

    return money



#bees algos
#_____________________________________________________________________________________________________________#

def gender_type():
    gender_dict= {1:"MALE",2:"FEMALE"}

    print("Choose one of the gender options")
    for key, value in gender_dict.items():
        print(f"{key}: {value}")

    user_input = int(input("choose:"))

    return gender_dict[user_input]


#pay algos
#_____________________________________________________________________________________________________________#

def salaries_matrix(salary, bees_no_dict: dict):
    """Picks up the salaries fund and sub divides among the bees"""
    # loop to control greed/inappropiate allocation
    salary_app = {}

    for key, value in bees_no_dict.items():
        amount_earned = float(input(f"{key}:{value} SHARE : "))
        amount_remaining = (float(salary)) - amount_earned
        print(f"AMOUNT REMAINING {amount_remaining}")

        salary_app=[key]=amount_earned

        salary = amount_remaining
    return salary_app


def display_fee_distribution(project_source_id,project_fund,timeline = True):

    project_bounty,formode_fee,tax,salaries = project_funds_distribution_V3(project_source_id,project_fund,optical_illusion=True)

    print()
    print(f"Fee distribution")
    print("***************************************************")
    print(f"project bounty : {project_bounty}")
    print(f"tax : {tax}")
    print(f"formode fee : {formode_fee}")
    print(f"Your fee : {salaries}")


    if timeline is True:
    
        # Optical deadlines to ensure projects are completed on time always
        expected_timeline = int(input("Real Timeline (days):"))
        optical_timeline = round(2/3 * (expected_timeline)) 

        print(f"Timeline: {optical_timeline} days")
        
    else:
        pass
    print("___________________________________________________")

    

def project_funds_distribution_V3(project_source_id, project_fund,optical_illusion= False):

    client_fee = float(project_fund)
    distribution_factor = (2/3) # distribution to reality
    real_fee = distribution_factor * client_fee

    # real_fee should always be a whole number rounded to 0 or 5 to make it convincing
    base = 5
    real_fee = base * round(real_fee /5)

    # optical illusion achieved
    optical_fee = client_fee - real_fee


    if project_source_id == 1: #fiverr
        #  illusion
        illusion_tax = 0.2 * optical_fee
        illusion_formode_fee = optical_fee - illusion_tax

        # reality 
        reality_tax = 0.2 * real_fee
        bee_fees =round(0.7 * real_fee)
        reality_formode_fee = ( real_fee - ( reality_tax + bee_fees))

    elif project_source_id == 2: #physical
        #  illusion
        illusion_tax = 0
        illusion_formode_fee = optical_fee - illusion_tax
        # reality 
        reality_tax = 0
        bee_fees =round(0.9 * real_fee)
        reality_formode_fee = ( real_fee - ( reality_tax + bee_fees))

    elif project_source_id == 3: #competition
        print("Gopillar projects yet to be factored")
    
    elif project_source_id == 5: #paypal
        #  illusion
        illusion_tax = 0.05 * optical_fee
        illusion_formode_fee = optical_fee - illusion_tax
        # reality 
        reality_tax = 0.05 * real_fee
        bee_fees =round(0.85 * real_fee)
        reality_formode_fee = ( real_fee - ( reality_tax + bee_fees))

    else:
        print("projects fund yet to be included")

    company_fund = reality_formode_fee + illusion_formode_fee
    tax = reality_tax + illusion_tax
    salaries = bee_fees
    project_bounty = real_fee
    illusion_tax = illusion_tax
    illusion_formode = illusion_formode_fee

    if optical_illusion is True:
        package = (project_bounty,illusion_formode,illusion_tax,salaries)

    else:
        package = (company_fund,salaries,tax)

    return package
