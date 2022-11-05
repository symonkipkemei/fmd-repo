#connection
import sqlalchemy as s
from connect import engine
from connect import connection
from connect import metadata


# create table object, called selected table, st
st = s.Table("co_transaction", metadata, autoload=True, autoload_with=engine) #project_category


# the functions that are imported into the display table and view table, adapt/change this when updating a table.
#________________________________________________________________________________________________________________________
def select_table():
    # the query object
    query = s.select([st.columns.co_transaction_id, st.columns.money_in,st.columns.money_out])
    # execute query
    select_result_proxy = connection.execute(query)
    return select_result_proxy

def update_table(co_account_id,co_transaction_id,co_transtatus_id,co_loans_id,co_operations_id,co_salaries_id,money_in,money_out,date_of_transaction):
    update = s.update(st).values(co_account_id=co_account_id,
    co_loans_id=co_loans_id,
    co_operations_id=co_operations_id,
    co_salaries_id=co_salaries_id,
    co_transtatus_id=co_transtatus_id,
    money_in=money_in,
    money_out=money_out,
    date_of_transaction=date_of_transaction).where(st.columns.co_transaction_id  == co_transaction_id)
    proxy = connection.execute(update)
    ans = "selected id updated"
    return ans

def delete_table():
    co_transaction_id = int(input("Select co_transaction_id: "))
    query = s.delete(st).where(st.columns.co_transaction_id == co_transaction_id)
    proxy = connection.execute(query)
    ans = "selected id deleted"
    return ans


def insert_table_loans_money_in(co_account_id,co_loans_id,co_transtatus_id,money_in,date_of_transaction):
    insert = s.insert(st).values(co_account_id=co_account_id,
    co_loans_id=co_loans_id,
    co_transtatus_id=co_transtatus_id,
    money_in=money_in,
    date_of_transaction=date_of_transaction)
    proxy = connection.execute(insert)
    ans = f"Transaction inserted"

def insert_table_loans_money_out(co_account_id,co_loans_id,co_transtatus_id,money_out,date_of_transaction):
    insert = s.insert(st).values(co_account_id=co_account_id,
    co_loans_id=co_loans_id,
    co_transtatus_id=co_transtatus_id,
    money_out=money_out,
    date_of_transaction=date_of_transaction)
    proxy = connection.execute(insert)
    ans = f"Transaction inserted"

def insert_table_operations_money_in(co_account_id,co_operations_id,co_transtatus_id,money_in,date_of_transaction):
    insert = s.insert(st).values(co_account_id=co_account_id,
    co_operations_id=co_operations_id,
    co_transtatus_id=co_transtatus_id,
    money_in=money_in,
    date_of_transaction=date_of_transaction)
    proxy = connection.execute(insert)
    ans = f"Transaction inserted"

def insert_table_operations_money_out(co_account_id,co_operations_id,co_transtatus_id,money_out,date_of_transaction):
    insert = s.insert(st).values(co_account_id=co_account_id,
    co_operations_id=co_operations_id,
    co_transtatus_id=co_transtatus_id,
    money_out=money_out,
    date_of_transaction=date_of_transaction)
    proxy = connection.execute(insert)
    ans = f"Transaction inserted"

def insert_table_salaries_money_out(co_account_id,co_salaries_id,co_transtatus_id,money_out,date_of_transaction):
    insert = s.insert(st).values(co_account_id=co_account_id,
    co_salaries_id=co_salaries_id,
    co_transtatus_id=co_transtatus_id,
    money_out=money_out,
    date_of_transaction=date_of_transaction)
    proxy = connection.execute(insert)
    ans = f"Transaction inserted"

# the functions can be imported into another table
#________________________________________________________________________________________________________________________

def display_table(table_name) -> tuple:
    """View , select, update and insert the table:
    Args:
        table_name (str): the name of the table

    Returns:
        id - name (tuple): the id of the entry selected, and the name of entry selected

    """
    try_again = True
    while try_again:

        select = select_table()

        # DISPLAY ENTRIES IN DATABASE, CREATE, DELETE AND INSERT OPTIONS
        #_______________________________________________________________________________________
        # items to be iterated: the entries in database and options for the user
        items = [result for result in select] # 2d list with tuples inside
        items_dict = {item[0]:item[1] for item in items} #tuples to dict
        changes = {"u":"update","d":"delete","i":"insert" }

        print()
        print(F"{table_name}")
        print("***************************************************")
        for item in items:
            print(f"{item[0]}:{item[1]}")
        print("___________________________________________________")
        for key, value in changes.items():
            print(f"<> ({key}):{value} <> ", end="")
        print("\n***************************************************")

        user_selection = input("select: ")
    
        # SELECT ENTRY IN DATABASE LOGIC
        #_______________________________________________________________________________________
        if user_selection.isdigit():
            user_selection = int(user_selection)
            if user_selection in items_dict.keys():
                try_again = False
            else:
                print("Integer selected out of range")
                try_again = True

        # UPDATE , DELETE AND INSERT LOGIC
        #_______________________________________________________________________________________
        else:
            if user_selection in changes.keys():
                if user_selection == str.lower("u"):#update
                    print()
                    print("_____________________________")
                    print("Updating a database entry")
                    print("_____________________________")
                    update_table()
                    print("_____________________________\n")
                    try_again = True
                elif user_selection == "d":#delete the entries
                    print()
                    print("_____________________________")
                    print("Deleting a database entry")
                    print("_____________________________")
                    delete_table()
                    print("_____________________________\n")
                    try_again = True
                elif user_selection == "i":#insert
                    # insert new entries
                    print("_____________________________")
                    print("Inserting a database entry")
                    print("_____________________________")
                    print("insert role taken up by another function")
                    print("_____________________________\n")
                    try_again = True
                else:
                    print("Input selected is out of range")

    selected_category = items_dict[user_selection]
    # RETURN ID(PRIMARY KEY) OF SELECTED OPTION
    #_______________________________________________________________________________________   
    return (user_selection , selected_category)

def show_table(table_name):
    try_again = True
    while try_again:
        select = select_table()
 
        # STORING RESULTS PROXY IN A DICT
        #_______________________________________________________________________________________
        items = [result for result in select] #a list with tuples inside
        items_dict = {item[0]:item[1] for item in items}
    

        print(F"\n{table_name}")
        print("***************************************************")
        for item in items:
            print(f"{item[0]}:{item[1]}")
        print("***************************************************")

        # SELECT ENTRY IN DATABASE LOGIC
        #_______________________________________________________________________________________
        user_selection = input("select: ")
        if user_selection.isdigit():
            user_selection = int(user_selection)
            if user_selection in items_dict.keys():
                try_again = False
            else:
                print("Integer selected out of range")
                try_again = True
        else:
            print("Wrong input")

        selected_category = items_dict[user_selection]

    return (user_selection,selected_category)


if __name__ == "__main__":
    display_table("co_transaction")

