# record the commencement and completion date
from pickle import FALSE
from re import U

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
        custom_year = int(input("year:"))

        current_date = date(custom_year, custom_month, custom_date)
    return current_date


# the timestamp id

def time_id():
    """the following function records the year/month/day/hour/minute/seconds
    and uses it as a key in a database"""
    from datetime import datetime

    now = datetime.now()
    time_key = now.strftime("%Y%m%d%H%M%S")
    return time_key

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
    restart = True
    while restart :
        try:
            global purpose
            import csv
            from configurations import project_configuration

            # announce what we are doing here

            file_type_upper = str.upper(filetype)



            try_again = True
            while try_again:
                category_dict = {}
                with open(filename, "r") as f:
                    print(f"\n****{file_type_upper}*****")
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

                restart = False

        except FileNotFoundError:
            f = open(filename, "w")
            f.close()
            restart = True



def project_setup_cooperation(filename, filetype):
    """establish project source"""
    selected_bees = []
    bees_index = []
    global user_selection
    import csv
            

    # announce what we are doing here

    file_type_upper = str.upper(filetype)

    # loop until all the bees have been mentioned.

    try_again = True
    while try_again:
        category_dict = {}
        # all bees displayed from csv file
        with open(filename, "r") as f:
            # display  bees available
            print("\n*******AVAILABLE BEES*******")
            iterable = csv.reader(f)
            list_iterable = list(iterable)
            for x in list_iterable:
                print(f"{x[0]}. {x[1]}")
                category_dict[int(x[0])] = x[1]
            # option to terminate the loop
            print("0. (stop the count)")
            print("****************************\n")

        # bee selection
        user_selection = int(input("Insert option above: "))
                

            #check if bee selected is within the list

        for x in category_dict:
            if user_selection == x:
                purpose = category_dict[x]
                # if selected bee in list, announce the selected one (within a list)
                
                selected_bees.append (category_dict[x])
                print (f"\nselected bee: {selected_bees} ")
                
                # store the index ( identifier of the bees ) in a different list
                bees_index.append (x)
                print("\n*******ADD ANOTHER BEE******")
                
        
                
        if user_selection == 0:
            print("Bees selected")
            try_again = False
            

    print(bees_index)

    return bees_index
    

def project_funds():
    """Total amount paid for the project"""
    print("\n****PROJECT FUND*****")
    projectFund = float(input("Amount paid:"))

    return projectFund


def project_funds_distribution(projectSource, doneBy, projectFund):
    """The total amount payable for the particular project as per the guy working on it"""
    company_fund = 0
    brian_income = 0
    symon_income = 0
    other_income = 0
    tax = 0

    # estbalish what is to be shared after , fiverr's cut

    if projectSource == "FIVERR":
        shareable_fund = (projectFund / 100) * 80
        tax = (projectFund / 100) * 20
    else:
        shareable_fund = projectFund

    if doneBy == "BRIAN":
        company_fund = (shareable_fund / 100) * 50
        brian_income = shareable_fund - company_fund
    elif doneBy == "SYMON":
        company_fund = (shareable_fund / 100) * 50
        symon_income = shareable_fund - company_fund

    elif doneBy == "SYMON-BRIAN":
        company_fund = (shareable_fund / 100) * 50
        sharable_income = (shareable_fund / 100) * 50
        print("\n*****SHAREABLE_FORMULA *****\n"
              "Symon(s):Brian(B)\n"
              "1)50%S : 50%B \n"
              "2)15%S : 85B% \n"
              "3)85%S : 15B% \n"
              "4)80%S : 20B% \n"
              "5)20%S : 80%B ")
        shareable_formula = int(input("insert formula:"))

        if shareable_formula == 1:
            symon_income = sharable_income / 2
            brian_income = sharable_income / 2

        elif shareable_formula == 2:
            symon_income = (sharable_income / 100) * 15
            brian_income = (sharable_income / 100) * 85

        elif shareable_formula == 3:
            symon_income = (sharable_income / 100) * 85
            brian_income = (sharable_income / 100) * 15

        elif shareable_formula == 4:
            symon_income = (sharable_income / 100) * 80
            brian_income = (sharable_income / 100) * 20

        elif shareable_formula == 5:
            symon_income = (sharable_income / 100) * 20
            brian_income = (sharable_income / 100) * 80
    elif doneBy == "SYMON-EMPLOYEE":
        company_fund = (shareable_fund / 100) * 50
        sharable_income = (shareable_fund / 100) * 50
        other_income = int(input("insert employee income:"))
        symon_income = sharable_income - other_income
        print(f"symon income is {symon_income}")

    elif doneBy == "BRIAN-EMPLOYEE":
        company_fund = (shareable_fund / 100) * 50
        sharable_income = (shareable_fund / 100) * 50
        other_income = int(input("insert employee income:"))
        brian_income = sharable_income - other_income
        print(f"Brian income is {brian_income}")

    elif doneBy == "EMPLOYEE":
        company_fund = (shareable_fund / 100) * 10
        other_income = (shareable_fund / 100) * 90

    print(other_income)

    funds = (company_fund, brian_income, symon_income, other_income, tax)
    return funds


def project_funds_distribution_V2(projectSource, projectFund):

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

    if projectSource == "FIVERR":
        client_fee = projectFund
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

        funds = (company_fund, salaries, tax)
        
        return funds

    elif projectSource == "PHYSICAL":
        client_fee = projectFund
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

        funds = (company_fund, salaries, tax)

        return funds
    
    else:
        print("Other projects yet to be included")



def test():
    real_fee = int(input("insert a number: "))
    base = 5
    real_fee = base * round(real_fee /5)
    print(real_fee)



def project_name(date, clientName, category):
    """establish the name of the project, should be used as primary key"""
    # date converted to string
    date_object = str(date)
    # date string abstracted to the 2 digits of the year,month and day
    record_date = date_object[2:4] + date_object[5:7] + date_object[8:10]
    prjt_name = record_date + "_" + str(clientName) + "_" + str(category)
    return prjt_name


def salaries_matrix(filename, salary, bees_index):

    """Picks up the salaries fund and sub divides among the bees"""
    import csv
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
    for x in bees_index:
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

#filename1 = "files/project_done_by.csv"
#salary = 600
#bees = [2,3,4,1]
#salaries_matrix(filename1 ,salary, bees)



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

