
import csv

def project_name(date, clientName, category):
    """establish the name of the project, should be used as primary key"""
    # date converted to string
    date_object = str(date)
    # date string abstracted to the 2 digits of the year,month and day
    record_date = date_object[2:4] + date_object[5:7] + date_object[8:10]
    prjt_name = record_date + "_" + str(clientName) + "_" + str(category)
    return prjt_name


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


# Date algorithim

def date_setup(purpose):
    """generate the date object at time of the recording"""
    global current_date
    from datetime import date
    print()
    print(f"{purpose}")
    print("***************************************************")
    print( "1) Today's date\n"
          "2) Custom date")
    print("___________________________________________________")
    user_option = int(input("insert: "))
    print("***************************************************")

    if user_option == 1:
        current_date = date.today()

    elif user_option == 2:
        custom_date = int(input("date:"))
        custom_month = int(input("month:"))
        custom_year = int(input("year:"))
        print("***************************************************")

        current_date = date(custom_year, custom_month, custom_date)

    # format date to string format
    current_date =current_date.strftime('%Y-%m-%d %H:%M:%S')
    
    return current_date


## project fund algos
def project_fund():
    """Total amount paid for the project"""
    print("\n****PROJECT FUND*****")
    projectFund = float(input("Amount paid:"))
    return projectFund


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

    if project_source_id == 1:
        client_fee = project_fund
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

        funds = (company_fund,consultancies, salaries, tax)
        
        return funds

    elif project_source_id == 2:
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

        funds = (company_fund, consultancies, salaries, tax)

        return funds
    
    else:
        print("ther projects yet to be included")


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


def salaries_matrix(filename, salary, bees_no):
     """Picks up the salaries fund and sub divides among the bees"""
     # store keys to the bees
     category_dict = {}
     # store amount allocated to each bee
     pesa_dict = {}


     # determine the bees from the index
     with open(filename, "r") as f:
             iterable = csv.reader(f)
             list_iterable = list(iterable)
             for x in list_iterable:
                 category_dict[int(x[0])] = x[1]

     print(f"TOTAL SALARIES FUND:{salary}")
     count = 0

     # loop through the bees-index
     for x in bees_no:
         # determine the keys in dictionary
         for y in category_dict:
             #if key in dict is similar to item in bees-index, then you've found the right person
             if x == y:
                 # loop to control greed/inappropiate allocation
                 try_again = True
                 while try_again == True:
                     amount_earned = float(input(f"{category_dict[y]} SHARE : "))
                     rem = (float(salary)) - amount_earned
                     count += rem
                     if  count <= 0:
                         print("Don't be greedy, share the funds appropiately. Try again")
                     else:
                         print (f"Unallocated amount is {rem}")
                         # record the amount allocated to the individual to the dictionary
                         pesa_dict [x] = amount_earned
                         try_again = False

     print(pesa_dict)
     return pesa_dict



#bees algos

def gender_type():
    gender_dict= {1:"MALE",2:"FEMALE"}

    print("Choose one of the gender options")
    for key, value in gender_dict.items():
        print(f"{key}: {value}")

    user_input = int(input("choose:"))

    return gender_dict[user_input]




#pay algos

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