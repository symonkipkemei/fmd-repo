
from select import select
import sqlalchemy as s
from connect import engine
from connect import connection
from connect import metadata

import algos

import tables.project_category as project_category 

import tables.project_source as project_source
import tables.project_status as project_status
import tables.scope as scope
import tables.project as project
import tables.project_scope as project_scope
import tables.project_fund as project_fund
import tables.project_bees as project_bees
import tables.pay as pay

st = s.Table("project", metadata, autoload=True, autoload_with=engine) #selected table
ps = s.Table("project_scope", metadata, autoload=True, autoload_with=engine) #project_scope


def insert_data():

    #ensure the ids are intandem with the database for it to work
    # PROJECT STATUS ID
    ACTIVE_ID = 1
    COMPLETE_ID = 2
    CANCELLED_ID = 3

    CLIENT_NAME = algos.client_name()
    DATE_COMMENCMENT = algos.date_setup("date of commencment")

    #extract the category name in order to create the project name
    return_value = project_category.display_table("project_category")
    PROJECT_CATEGORY_ID = return_value[0]
    PROJECT_CATEGORY = str.lower(return_value[1])

    PROJECT_NAME = algos.project_name(DATE_COMMENCMENT,CLIENT_NAME,PROJECT_CATEGORY)
    PROJECT_SOURCE_ID = project_source.display_table("project_source")
    PROJECT_STATUS_ID = project_status.display_table("project_status")

     # ADD PROJECT FUND
    PROJECT_FUND_ID =project_fund.insert_table(PROJECT_SOURCE_ID)


    if PROJECT_STATUS_ID == ACTIVE_ID:
        # ADD PROJECT TABLE
        project.insert_table(CLIENT_NAME,DATE_COMMENCMENT,PROJECT_CATEGORY_ID,PROJECT_NAME,PROJECT_SOURCE_ID,PROJECT_STATUS_ID,PROJECT_FUND_ID,date_completion=False)
        
        # retirieve project id
        PROJECT_ID = project.retrieve_project_id()

        # ADD PROJECT SCOPE
        project_scope.insert_table(PROJECT_ID)

       


    elif PROJECT_STATUS_ID == COMPLETE_ID:

        # ADD PROJECT TABLE + DATE COMPLETION
        project.insert_table(CLIENT_NAME,DATE_COMMENCMENT,PROJECT_CATEGORY_ID,PROJECT_NAME,PROJECT_SOURCE_ID,PROJECT_STATUS_ID,PROJECT_FUND_ID,date_completion=True)

        # retirieve project id
        PROJECT_ID = project.retrieve_project_id()

        # ADD PROJECT SCOPE
        project_scope.insert_table(PROJECT_ID)

        # ADD FUND BEES ( BEES WHO DID THE WORK)
        project_bees.insert_table(PROJECT_ID)

        # show them salaries to be distributed.
        salaries = project_fund.select_salaries(PROJECT_ID)

        # pay the active bees
        pay.insert_table(PROJECT_ID,salaries)
    

def update_project_table():
    completion_status_id = 5
    while True:
        print("\nUPDATING PROJECT TABLE")

        #show all projects that have the status active or null
        PROJECT_ID = project.active_projects()

        # project_catgory_id
        return_value = project_category.display_table("project_category")
        PROJECT_CATEGORY_ID = return_value[0]
        PROJECT_CATEGORY = str.lower(return_value[1])

        # project_source_id
        PROJECT_SOURCE_ID = project_source.display_table("project_source")

        #date_completion
        DATE_COMPLETION = algos.date_setup("date completion")

        #project_status_id
        PROJECT_STATUS_ID = completion_status_id

        # project_update
        project.selective_update(PROJECT_ID,PROJECT_CATEGORY_ID,PROJECT_SOURCE_ID,DATE_COMPLETION,PROJECT_STATUS_ID)

        #UPDATING PROJECT_SCOPE TABLE
        project_scope.insert_table(PROJECT_ID)

        print("*************************************************************")
        user_selection = str.lower(input("\ninsert another project (y/n)?: "))

        if user_selection == "y":
            print("PROJECT COMPLETED")
            print("**")
            print("proceed to adding another project")
            pass
        elif user_selection =="n":
            print("PROJECT COMPLETED")
            print("**")
            print("Thank you")
            break
        else:
            print("wrong input")


def insert_project_scope():
    while True:
        PROJECT_ID = project.active_projects()
        project_scope.insert_table(PROJECT_ID)

        user_input = str.lower(input("insert another (y/n):"))
        if user_input == "y":
            pass
        elif user_input == "n":
            break
        project.update_status(PROJECT_ID,2)
        


def insert_project_bee_salary():
    while True:
        PROJECT_ID = project.active_projects()
        project_bees.insert_table(PROJECT_ID)
        # show them salaries to be distributed.
        salaries = project_fund.select_salaries(PROJECT_ID)

        # pay the active bees
        pay.insert_table(PROJECT_ID,salaries)

        print()
        user_input = str.lower(input("insert another bee-salary (y/n):"))
        
        project.update_status(PROJECT_ID,2)

        if user_input == "y":
            pass
        elif user_input == "n":
            break

        
        


if __name__ == "__main__":
    insert_project_bee_salary()
    #add_project_to_database()

