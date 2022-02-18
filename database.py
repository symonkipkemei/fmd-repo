# connect to database
import sqlite3

with sqlite3.connect("formode_repository.db") as db:
    cursor = db.cursor()


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
    project_name text NOT NULL,
    project_doneby text PRIMARY KEY,
    project_fund integer NOT NULL,
    company_fund integer NOT NULL,
    symon_income integer NOT NULL,
    brian_income integer NOT NULL,
    other_income integer NOT NULL);""")

    print("Tables connected")


create_tables()


# insert into project_details table
def insert_project_details_table():
    """insert data into project_details_table"""
    selection = int(input("user selection: "))

    if selection == 1:
        # data to be inserted
        global artist_id
        correct = True
        while correct:
            artist_id = int(input("insert artist_id: "))
            if artist_id in list_of_id:
                print("Id already used, try another")
            else:
                correct = False

        name = input("insert name:")
        address = input("insert address:")
        town = input("insert town:")
        county = input("insert county:")
        post_code = input("Insert postcode:")

        # insert into artist_contact_details table
        cursor.execute("""INSERT INTO artist_contact_details(ArtistID,Name,Address,Town,County,Postcode)
                            VALUES(?,?,?,?,?,?)""", (artist_id, name, address, town, county, post_code))
        print("artist added successfully")
        db.commit()

    elif selection == 2:
        # table 2
        # data to be inserted
        global piece_id
        correct = True
        while correct:
            piece_id = int(input("insert piece_id: "))
            if piece_id in list_of_piece:
                print("Id already used, try another")
            else:
                correct = False
        artist_id = int(input("insert artist_id: "))
        title = input("insert title:")
        medium = input("insert medium:")
        price = int(input("insert price:"))

        # insert into artist_contact_details table
        cursor.execute("""INSERT INTO pieces_of_art(PieceID,ArtistID,Title,Medium,Price)
                                VALUES(?,?,?,?,?)""", (piece_id, artist_id, title, medium, price))
        print("piece of art added successfully")
        db.commit()

    elif selection == 3:
        correct = False

    else:
        print("wrong input")






def check_artist_id():
    """Check if artist id is already in the database"""
    cursor.execute("""SELECT * FROM artist_contact_details""")
    list_of_ids = []
    for row in cursor.fetchall():
        iterable = list(row)
        list_of_ids.append(iterable[0])

    return list_of_ids


def check_piece_id():
    """Check if piece id is already in the database"""
    cursor.execute("""SELECT * FROM pieces_of_art""")
    list_of_piece = []
    for row in cursor.fetchall():
        iterable = list(row)
        list_of_piece.append(iterable[0])

    return list_of_piece


def view_table():
    correct = True
    while correct:
        print("\nSearch art by ")
        print("1) artist\n"
              "2) medium.\n"
              "3) price\n"
              "4) Quit selection\n"
              "5) View entire database\n")
        select = int(input("Choose option: "))

        # by artist
        if select == 1:
            artist = input("insert name of artist: ")
            cursor.execute("""SELECT pieces_of_art.Title FROM pieces_of_art, artist_contact_details
            WHERE pieces_of_art.ArtistID =artist_contact_details.ArtistID AND 
            artist_contact_details.Name=? """, [artist])
            for row in cursor.fetchall():
                print(list(row))

        # by medium
        elif select == 2:
            medium = input("insert medium: ")
            cursor.execute("""SELECT pieces_of_art.Title FROM pieces_of_art WHERE pieces_of_art.Medium=? """, [medium])
            for row in cursor.fetchall():
                print(list(row))

        # by price
        elif select == 3:
            price = int(input("insert price: "))
            cursor.execute("""SELECT pieces_of_art.Title FROM pieces_of_art WHERE pieces_of_art.Price=? """, [price])
            for row in cursor.fetchall():
                print(list(row))

        elif select == 4:
            correct = False

        elif select == 5:
            cursor.execute("""SELECT * FROM pieces_of_art""")
            for row in cursor.fetchall():
                print(list(row))
        else:
            print("wrong selection,Try again")


def sell_piece_item():
    """list all items per id and ask the user which one he wants to purchase"""
    # display

    print("The following are the available art on sale")
    cursor.execute("""SELECT pieces_of_art.PieceID,pieces_of_art.Title FROM pieces_of_art""")
    for row in cursor.fetchall():
        list_row = list(row)
        print(f"{list_row[0]}.{list_row[1]}")

    # selected option
    choice = int(input("choose one:"))
    print(f"You just bought art index {choice}.Thank you!")

    # information about selected option
    cursor.execute("""SELECT * FROM pieces_of_art WHERE PieceID=?""", [choice])
    for row in cursor.fetchall():
        list_row = list(row)
        data = str(list_row[0]) + "," + str(list_row[1]) + "," + str(list_row[2]) + "," \
               + str(list_row[3]) + "," + str(list_row[4]) + "\n"
        with open("sold.txt", "a") as f:
            f.write(data)

    # delete item from database
    cursor.execute("""DELETE FROM pieces_of_art WHERE PieceID=?""", [choice])
