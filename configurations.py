
def project_category_derived():
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


def project_source_derived():
    """Establish the source of the project"""

    global user_index, user_source
    import csv

    pesa_dict = {}
    correct = True
    while correct:
        select = str.lower(input("Insert project source (y/n):"))

        # Look at what is available first
        with open("files/project_source.csv", "r") as f:
            iterable = csv.reader(f)
            dd_iterable = list(iterable)
            index_list = []
            source_list = []
            # store the index and the category
            for item in dd_iterable:
                index_list.append(item[0])
                source_list.append(item[1])

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
                    try_again_index = False

            # check if category already used
            try_again_category = True
            # subjecting the user category to test
            while try_again_category:
                user_source = str.upper(input("insert new source:"))
                if user_source in source_list:
                    print(f"{user_source} already used, try again.")
                else:
                    print(f"{user_source} recorded")
                    try_again_category = False

            # store data
            data = str(user_index) + "," + str(user_source) + "\n"
            with open("files/project_source.csv", "a") as f:
                f.write(data)

        elif select == str.lower("n"):
            correct = False

        else:
            print("Wrong input, Try again")


def project_scope_of_work_derived():
    """Scope of work established """

    global user_index, scope
    import csv

    pesa_dict = {}
    correct = True
    while correct:
        select = str.lower(input("Insert project scope of work (y/n):"))

        # Look at what is available first
        with open("files/project_scope.csv", "r") as f:
            iterable = csv.reader(f)
            dd_iterable = list(iterable)
            index_list = []
            scope_list = []
            # store the index and the category
            for item in dd_iterable:
                index_list.append(item[0])
                scope_list.append(item[1])

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
                    try_again_index = False

            # check if category already used
            try_again_category = True
            # subjecting the user category to test
            while try_again_category:
                scope = str.upper(input("insert new scope of work:"))
                if scope in scope_list:
                    print(f"{scope} already used, try again.")
                else:
                    print(f"{scope} recorded")
                    try_again_category = False

            # store data
            data = str(user_index) + "," + str(scope) + "\n"
            with open("files/project_scope.csv", "a") as f:
                f.write(data)

        elif select == str.lower("n"):
            correct = False

        else:
            print("Wrong input, Try again")