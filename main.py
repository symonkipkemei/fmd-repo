
from parameters import *

print("*******FORMODE REPOSITORY**************")
print("Record New project")
print("1) Date of project commencement\n"
      "2) Date of project completion")

user_selection = int(input("insert option"))

if user_selection == 1:
    date_commence = recording_date()


# we are going to continue as from tomorrow morning