def main():
    """ engine of the programme"""

    from parameters import client_name
    from parameters import project_setup
    from parameters import project_date
    from parameters import project_name
    from parameters import project_funds
    from parameters import project_funds_distribution

    from database import create_tables
    from database import insert_project_funds_table
    from database import insert_project_details_table
    from database import view_salary
    from database import view_projects
    from database import alter_table
    from database import active_projects
    from database import mark_active_complete
    from database import retrieve_source_user

    print("*******FORMODE REPOSITORY**************")
    print("1) Add project to database\n"
          "2) Check earnings\n"
          "3) Completed projects\n"
          "4) Active projects\n"
          "5) Settings")

    user_selection = int(input("insert option: "))

    if user_selection == 1:
        # Collecting the parameters

        # project category
        client_name = client_name()

        # project category
        filename = "files/project_category.csv"
        filetype = "project category"
        project_category = project_setup(filename, filetype)

        # project source
        filename = "files/project_source.csv"
        filetype = "project source"
        project_source = project_setup(filename, filetype)

        # project scope
        filename = "files/project_scope.csv"
        filetype = "project scope"
        project_scope = project_setup(filename, filetype)

        # project commencement date
        print("\n****PROJECT DATE COMMENCEMENT*****")
        date_commencement = project_date()

        # project status
        filename = "files/project_status.csv"
        filetype = "project status"
        project_status = project_setup(filename, filetype)

        if project_status == "COMPLETE":
            # project completion date
            print("\n****PROJECT DATE COMPLETION*****")
            date_completion = project_date()
            # project fund
            project_fund = project_funds()
        else:
            project_fund = 0
            date_completion = None

        # project user
        filename = "files/project_done_by.csv"
        filetype = "project bee"
        project_user = project_setup(filename, filetype)

        # project name ( project key/unique identifier)
        project_name = project_name(date_commencement, client_name, str.lower(project_category))

        # project funds
        company_fund, brian_income, symon_income, other_income, tax = project_funds_distribution(project_source,
                                                                                                 project_user,
                                                                                                 project_fund)

        # feeding to the database
        create_tables()
        insert_project_details_table(client_name, project_category, project_source, project_scope, date_commencement,
                                     date_completion, project_name, project_status)
        insert_project_funds_table(project_name, project_user, project_fund, company_fund, brian_income, symon_income,
                                   other_income, tax)
    # check earnings
    elif user_selection == 2:
        view_salary()
    # view complete projects
    elif user_selection == 3:
        view_projects()

    # view active projects
    elif user_selection == 4:
        option = active_projects()
        if option is None:
            print("Thanks")
        else:
            # project completion date
            print("\n****PROJECT DATE COMPLETION*****")
            date_completion = project_date()

            # project fund
            project_fund = project_funds()
            project_source, project_user = retrieve_source_user(option)

            # project funds
            company_fund, brian_income, symon_income, other_income, tax = project_funds_distribution(project_source,
                                                                                                     project_user,
                                                                                                     project_fund)

            mark_active_complete(option, date_completion, project_fund, company_fund, symon_income, brian_income,
                                 other_income, tax)



    # settings
    elif user_selection == 5:
        alter_table()


main()
