# connect to database
import sqlite3

with sqlite3.connect("formode_repository.db") as db:
    cursor = db.cursor()



# delete from pesa funds table

def delete_from_pesafunds():
    """insert item to be deleted from pesa funds"""
    id = str(input("insert id: "))
    cursor.execute("""DELETE FROM pesa_funds WHERE time_id =?""", [id])
    cursor.fetchall()

    print(f"{id} has been deleted")
    db.commit()
