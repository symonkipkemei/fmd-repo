
def main():
    """ engine of the programme"""

    from parameters import client_name
    from parameters import project_source
    from parameters import project_category
    from parameters import project_scope
    from parameters import project_date
    from parameters import project_name
    from parameters import project_done_by
    from parameters import project_total_fund

    print("*******FORMODE REPOSITORY**************")
    print("1) Add project to database\n"
          "2) Project_Configurations\n"
          "3) Check earnings\n")

    user_selection = int(input("insert option: "))

    if user_selection == 1

        # Collecting the parameters

        client_name = client_name()
        project_category = project_category()
        project_source = project_source()
        project_scope = project_scope()
        print("\n****PROJECT DATE COMMENCEMENT*****")
        date_commencement = project_date()
        print("\n****PROJECT DATE COMPLETION*****")
        date_completion = project_date()
        project_user = project_done_by()
        project_fund = project_total_fund(project_user)
        project_name = project_name(date_commencement, client_name, project_category)

        # feeding to the database




main()