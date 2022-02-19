def main():
    """ engine of the programme"""

    from parameters import client_name
    from parameters import project_source
    from parameters import project_category
    from parameters import project_scope
    from parameters import project_date
    from parameters import project_name
    from parameters import project_done_by
    from parameters import project_funds

    from database import create_tables
    from database import insert_project_funds_table
    from database import insert_project_details_table


    from configurations import project_source_derived

    print("*******FORMODE REPOSITORY**************")
    print("1) Add project to database\n"
          "2) Project_Configurations\n"
          "3) Check earnings\n")

    user_selection = int(input("insert option: "))

    if user_selection == 1:
        # Collecting the parameters

        client_name = client_name()
        project_category = project_category()

        change = True
        while change is True:
            project_source = project_source()
            if project_source is True:
                project_source_derived()
            else:
                project_source = project_source()
                change = False

        project_scope = project_scope()
        print("\n****PROJECT DATE COMMENCEMENT*****")
        date_commencement = project_date()
        print("\n****PROJECT DATE COMPLETION*****")
        date_completion = project_date()
        project_user = project_done_by()
        project_name = project_name(date_commencement, client_name, project_category)
        project_fund, company_fund, brian_income, symon_income, other_income = project_funds(project_user)

        # feeding to the database
        create_tables()
        insert_project_details_table(client_name, project_category, project_source, project_scope, date_commencement,
                                     date_completion, project_name)
        insert_project_funds_table(project_name, project_user, project_fund, company_fund, brian_income, symon_income,
                                   other_income)


main()
