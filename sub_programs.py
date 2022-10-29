
import sqlalchemy as s
from connect import engine
from connect import connection
from connect import metadata

import algos

import project_category as project_category 
import project_source as project_source
import project_status as project_status
import scope as scope
import project as project
import project_scope as project_scope
import project_fund as project_fund
import project_bees as project_bees
import pay

st = s.Table("project", metadata, autoload=True, autoload_with=engine) #selected table
ps = s.Table("project_scope", metadata, autoload=True, autoload_with=engine) #project_scope


def add_project_to_database():

    CLIENT_NAME = algos.client_name()
    DATE_COMMENCMENT = algos.date_setup("date of commencment")

    #extract the category name in order to create the project name
    return_value = project_category.show_table("project_category")
    PROJECT_CATEGORY_ID = return_value[0]
    PROJECT_CATEGORY = str.lower(return_value[1])

    PROJECT_NAME = algos.project_name(DATE_COMMENCMENT,CLIENT_NAME,PROJECT_CATEGORY)
    PROJECT_SOURCE_ID = project_source.display_table("project_source")
    PROJECT_STATUS_ID = project_status.display_table("project_status")

     # ADD PROJECT FUND
    PROJECT_FUND_ID =project_fund.insert_table(PROJECT_SOURCE_ID)


    if PROJECT_STATUS_ID == 4:
        # ADD PROJECT TABLE
        project.insert_table(CLIENT_NAME,DATE_COMMENCMENT,PROJECT_CATEGORY_ID,PROJECT_NAME,PROJECT_SOURCE_ID,PROJECT_STATUS_ID,PROJECT_FUND_ID,date_completion=False)
        
        # retirieve project id
        PROJECT_ID = project.retrieve_project_id()

        # ADD PROJECT SCOPE
        project_scope.insert_table(PROJECT_ID)

       


    elif PROJECT_STATUS_ID == 5:

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
    



add_project_to_database()