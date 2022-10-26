
import sqlalchemy as s
from connect import engine
from connect import connection
from connect import metadata

import algos

import project_category 
import project_source
import project_status
import scope
import project
import project_scope

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
    PROJECT_SOURCE_ID = project_source.show_table("project_source")
    PROJECT_STATUS_ID = project_status.show_table("project_status")

    if PROJECT_STATUS_ID == 1:
        # Do not add completion date, skip, proceed with recording the project into the project table
        project.insert_table(CLIENT_NAME,DATE_COMMENCMENT,PROJECT_CATEGORY_ID,PROJECT_NAME,PROJECT_SOURCE_ID,PROJECT_STATUS_ID,date_completion=False)
        # retirieve id and proceed with the project_scope
        PROJECT_ID = project.retrieve_project_id()
        project_scope.insert_table(PROJECT_ID)

        # add funds to the table


    elif PROJECT_STATUS_ID == 2:
        project.insert_table(CLIENT_NAME,DATE_COMMENCMENT,PROJECT_CATEGORY,PROJECT_NAME,PROJECT_SOURCE_ID,PROJECT_STATUS_ID,date_completion=True)

add_project_to_database()