"""
This application keep track of the bmi so that one
can control his health
"""
# pylint: disable=invalid-name
import PySimpleGUI as sg
import db
import ui
from dico import check_missing_value, dict_emptiness, get_empty_values
import sys

WINDOWS = sg.Window("Login Screen", ui.LOGIN)
WINDOWS1 = sg.Window("Registration Screen", ui.REGISTRATION, element_justification='r')
service = db.authenticate_db()

while True:
    #display login screen
    events1, values1 = WINDOWS.read()

    #if the user click on the close window icon, just close  the window and exit program
    if events1 == sg.WIN_CLOSED:
        break

    #If the combination of user id exist in remote cloudant db, test if password is correct.
    #If password is correct, display dashbord. Otherwise invite the user to enter the correct password 
    #Those login window event should take place in a while loop. For the implementation, we'll add 
    #another sg.Text with key as the test condition

    #if user click on register button or after clicked on login button his userid is not in the remote cloudant db, 
    # close the login window and then display registration window
    if (events1 == "register") or (events1 == "login" and db.get_record(values1["username"], "bmi", service) == False):
        WINDOWS.close()
        events2, values2 = WINDOWS1.read()
    #Registration should take place in a while loop. For this, i'll add a field on the registration windows.
    #The sole purpose of this field will be to make the test condition to exit the loop
    #Normaly i'll use a sg.Text with a key. The value of this key should be use to exit the loop
    #if the user smash the register button on registration windows, check to see if the form is no empty or doesn't have any missing value
        if events2 == "register":
            #we  will add the for loop here with the test condition spoken previously
            first_check = dict_emptiness(values2)
            second_check = check_missing_value(values2) 
    #optionally you can check if his password conform to standard password
            #This check will be implemented in the future
    #Also check if the user id provided is not for someone in the db. This check generate an exception if values2["_id"] is empty string
            third_check = db.get_record(values2["_id"], "bmi", service)
    #If the above three check are OK, register the user an then redisplay a new login window to the user for him to enter his credential.
    # Otherwise prompt them to change password or to fill missing values
            if first_check > 0 and second_check == False and third_check == False:
                db.insert_doc("bmi", values2, service)
                WINDOWS1.close()
                break
            else:
                sg.Popup(f"Please fill this field {get_empty_values(values2)} to complete registration process")
                events2, values2 = WINDOWS1.read()
    #The user should close the notification window before filling the missing value.
    # And another turn of check should be passed until the field are compliant with our politic