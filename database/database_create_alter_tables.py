# connect to database
import sqlite3

with sqlite3.connect("formode_repository.db") as db:
    cursor = db.cursor()


####################CREATING TABLES#######################
def create_tables():
    """create tables"""
    # project_details table
    cursor.execute("""CREATE TABLE IF NOT EXISTS project_details(
    project_name text PRIMARY KEY,
    client_name text NOT NULL,
    project_category text NOT NULL,
    project_source text NOT NULL,
    project_scope text NOT NULL,
    date_commencement text NOT NULL,
    date_completion text );""")

    # project_funds table
    cursor.execute("""CREATE TABLE IF NOT EXISTS project_funds(
    project_name text PRIMARY KEY,
    project_fund integer NOT NULL,
    company_fund integer NOT NULL,
    salaries integer NOT NULL,
    tax integer NOT NULL);""")

    # salaries_funds
    cursor.execute("""CREATE TABLE IF NOT EXISTS salaries_funds(
    project_name text PRIMARY KEY,
    project_doneby text,
    director_1 integer,
    director_2 integer,
    employee_3 integer,
    employee_4 integer,
    employee_5 integer,
    employee_6 integer);""")


    # pesa_funds table
    cursor.execute("""CREATE TABLE IF NOT EXISTS pesa_funds(
        time_id text PRIMARY KEY,
        funds_date text NOT NULL,
        co_fund_type text NOT NULL,
        co_sub_type text NOT NULL,
        typology text,
        currency text NOT NULL,
        amount integer NOT NULL,
        er_income integer);""")
    


    db.commit()
    print("project_details connected\nproject_funds connected\nsalaries_funds connected\npesa_funds connected\nYou can now proceed")



#################### ALTERING TABLES#######################

# change name of column 
def alter_column_name():
    """change the name of a column in a table"""
    print("******ADD COLUMN TO DATABASE******")
    table_name = input("name of table:")
    old_column_name = input("old_column_name:")
    new_column_name = input("new_column_name:")
    cursor.execute(f"""ALTER TABLE {table_name} RENAME COLUMN {old_column_name} to {new_column_name} ;""")

    db.commit()
    print("column name changed successfully")


# alter null option
def alter_column_null_option():
    """alter the column null option"""
    print("******CHANGE COLUMN FROM NOT NULL TO NULL******")
    table_name = input("name of table:")
    column_name = input("name of column:")
    cursor.execute(f"""ALTER TABLE {table_name} MODIFY {column_name} columnType NULL;""")

    db.commit()
    print("column null option changed successfully")


# add column to table
def alter_table_add_column():
    """Add column to a table"""
    print("******ADD COLUMN TO TABLE IN DATABASE******")
    table_name = input("name of table:")
    column_name = input("name of column:")
    cursor.execute(f"""ALTER TABLE {table_name} ADD {column_name};""")

    db.commit()
    print("column added successfully")


# delete column in table
def delete_column_table():
    """" Delete column from an existing table"""
    table_name = input("name of table:")
    column_name = input("name of column:")

    cursor.execute(f"""ALTER TABLE {table_name} DROP COLUMN {column_name} ;""")

    db.commit()
    print("column deleted successfully")


def move_data_from_table():
    """Move data from one table to another"""
    print("******MOVE DATA FROM TABLE TO ANOTHER******")
    from_table_name = input("from table:")
    to_table_name = input("to table:")
    cursor.execute(f"""INSERT INTO {to_table_name} SELECT * FROM {from_table_name};""")

    db.commit()
    print("Transfer was successfully")

# drop table from database

def drop_table():
    cursor.execute("""DROP TABLE formode_repository.salaries_funds1;""")
    print("dropped succesfully")

 