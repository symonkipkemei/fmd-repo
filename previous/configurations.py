def project_configuration(filename, filetype):
    """The following function helps you modify the project parameters,
    by allowing you to add or remove the individual items"""

    global user_index, user_item
    import csv

    # Look at what is available first
    with open(filename, "r") as f:
        iterable = csv.reader(f)
        dd_iterable = list(iterable)
        index_list = []
        source_list = []
        # store the index and the category
        for item in dd_iterable:
            index_list.append(item[0])
            source_list.append(item[1])

    print(f"\n*****modify {filetype}****\n"
          f"1). Add \n"
          f"2). Delete")

    user_selection = int(input("option : "))

    if user_selection == 1:
        print(f"\n*****adding {filetype}****")
        # check if index is already used
        try_again_index = True
        while try_again_index:
            user_index = str(input(f"insert index:"))
            if user_index in index_list:
                print(f"{user_index} already used, try another.")
            # it should be a digit
            elif not user_index.isdigit():
                print(f"{user_index} is not a digit, try again.")
            # 0 is already used
            elif user_index == str(0):
                print("0 already used, try another.")

            # test passed , user_index released for use
            else:
                try_again_index = False

        # check if category already used
        try_again_category = True
        # subjecting the user category to test
        while try_again_category:
            user_item = str.upper(input(f"insert item:"))
            if user_item in source_list:
                print(f"{user_item} already used, try again.")
            else:
                print(f"{user_item} recorded")
                try_again_category = False

        # store data
        data = str(user_index) + "," + str(user_item) + "\n"
        with open(filename, "a") as f:
            f.write(data)

    elif user_selection == 2:
        print(f"\n*****deleting {filetype} ****")
        delete_index = int(input("insert index: "))
        tmp_list = []

        # isolating the identified item (death by isolation)
        for x in dd_iterable:
            if delete_index == int(x[0]):
                print(f"{x[1]} deleted")
            else:
                tmp_list.append(x)

        # empty the csv file , anticipating the new kids in town
        f = open(filename, "w")
        f.close()

        # overriding the csv with the new generation
        for y in tmp_list:
            data = str(y[0]) + "," + str(y[1]) + "\n"
            with open(filename, "a") as f:
                f.write(data)
    else:
        print("Wrong input, Try again")


