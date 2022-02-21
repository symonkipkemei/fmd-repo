def main():
    """ engine of the programme"""

    from parameters import client_name
    from parameters import project_setup
    from parameters import project_date
    from parameters import project_name
    from parameters import project_fund
    from parameters import project_funds_distribution

    from database import create_tables
    from database import insert_project_funds_table
    from database import insert_project_details_table

    print("*******FORMODE REPOSITORY**************")
    print("1) Add project to database\n"
          "2) Check earnings\n")

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

        # project completion date
        print("\n****PROJECT DATE COMPLETION*****")
        date_completion = project_date()

        # project fund
        project_fund = project_fund()

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
                                     date_completion, project_name)
        insert_project_funds_table(project_name, project_user, project_fund, company_fund, brian_income, symon_income,
                                   other_income, tax)


main()
