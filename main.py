def main():
    """ engine of the programme"""

    from database import view_salary
    from database import view_projects
    from database import alter_table

    from parameters import time_id

    from sub_programs import add_project_to_database, view_active_projects, formode_funds

    correct = True
    while correct:
        print("*******FORMODE REPOSITORY**************")
        print("1) Add project to database\n"
              "2) Check earnings\n"
              "3) Completed projects\n"
              "4) Active projects\n"
              "5) Formode Fund\n"
              "6) Settings\n"
              "0) Quit")
        print("**************************************")
        user_selection = int(input("insert option: "))

        if user_selection == 1:
            add_project_to_database()

        # check earnings
        elif user_selection == 2:
            view_salary()
        # view complete projects
        elif user_selection == 3:
            view_projects()
        # view active projects
        elif user_selection == 4:
            view_active_projects()
        # formode fund
        elif user_selection == 5:
            formode_funds()
        # settings
        elif user_selection == 6:
            alter_table()
        # Quit
        elif user_selection == 0:
            correct = False
            print("""Unless the Lord builds the house,
    those who build it labor in vain.\nThank you!""")

        else:
            print("Wrong input, try again")


main()