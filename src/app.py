"""
This application keep track of the bmi so that one
can control his health
"""
# pylint: disable=invalid-name
# pylint: disable=line-too-long
import PySimpleGUI as sg
import db
import ui
from dico import check_missing_value, dict_emptiness

WINDOWS = sg.Window("Login Screen", ui.LOGIN)
WINDOWS1 = sg.Window("Registration Screen", ui.REGISTRATION, element_justification='r')
service = db.authenticate_db()

while True:
    #display login screen
    print("Dans la boucle de base")
    events1, values1 = WINDOWS.read()

    #if the user click on the close window icon, just close  the window and exit program
    if events1 == sg.WIN_CLOSED:
        break

    #If the user id exist in remote cloudant db, test if password is correct.
    #If password is correct, display dashbord.
    # Otherwise invite the user to enter the correct password
    #Those login window event should take place in a while loop. For the implementation, we'll add
    #another sg.Text with key as the test condition

    #The line below test to see if the user id is already in the db
    while (events1 == "login" and db.get_record(values1["_id"], "bmi", service)):
        #The line below check to see if the password provided is correct
        if db.retrieve_document(values1["_id"], "bmi", service)["password"] == values1["password"]:
            #Normally we should display the dashboard of the user
            print("The password is correct")
        else:
            print("The password is incorrect")
        print("Je suis toujours dans la boucle")
        #This condition is necessary so that the
        #loop will pause here to get the values of events and values
        events1, values1 = WINDOWS.read()
    print("Je suis a l'exterieur de la boucle")

    if not((events1 == "register") or (events1 == "login" and db.get_record(values1["_id"], "bmi", service))):
        WINDOWS.close()
        events2, values2 = WINDOWS1.read()
        while events2 == "register":
            if (check_missing_value(values2) or dict_emptiness(values2)) is True:
                print("Please fill the missing values")
            else:
                db.insert_doc("bmi", values2, service)
                break

            events2, values2 = WINDOWS1.read()
