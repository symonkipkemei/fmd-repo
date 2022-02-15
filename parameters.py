
# record the commencement and completion date
def recording_date ():
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
    print("\n****NAME OF CLIENT*****")
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
        else:
            correct = False

    return name


def project_genre_type_derived():
    """Should be derived based on the typology of the project, the user should be
    able to edit this add or subtract"""
    global user_index, user_category
    import csv

    pesa_dict = {}
    correct = True
    while correct:
        select = str.lower(input("Insert project category (y/n):"))

        # Look at what is available first
        with open("files/project_category.csv", "r") as f:
            iterable = csv.reader(f)
            dd_iterable = list(iterable)
            index_list = []
            category_list = []
            # store the index and the category
            for item in dd_iterable:
                index_list.append(item[0])
                category_list.append(item[1])

        # if yes, lets check if our entry is already used
        if select == str.lower("y"):
            # check if index is already used
            try_again_index = True
            while try_again_index:
                user_index = str(input("\ninsert index:"))
                if user_index in index_list:
                    print(f"{user_index} already used, try another.")
                # it should be a digit
                elif not user_index.isdigit():
                    print(f"{user_index} is not a digit, try again.")
                # test passed , user_index released for use
                else:
                    print(f"{user_index} recorded")
                    try_again_index = False

            # check if category already used
            try_again_category = True
            # subjecting the user category to test
            while try_again_category:
                user_category = str.upper(input("insert new category:"))
                if user_category in category_list:
                    print(f"{user_category} already used, try again.")
                else:
                    print(f"{user_category} recorded")
                    try_again_category = False

            # store data
            data = str(user_index) + "," + str(user_category) + "\n"
            with open("files/project_category.csv", "a") as f:
                f.write(data)

        elif select == str.lower("n"):
            correct = False

        else:
            print("Wrong input, Try again")



project_genre_type_derived()


