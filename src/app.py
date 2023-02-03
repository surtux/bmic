"""
This application keep track of the bmi so that one
can control his health
"""
# pylint: disable=invalid-name
import PySimpleGUI as sg
import db
import ui
#import health

#WINDOWS = sg.Window("BMI CALCULATION", ui.BMI)

#while True:
    #EVENTS, VALUES = WINDOWS.read()
    #if EVENTS == sg.WIN_CLOSED:
        #break
    #The code use to extract values from input element and then calculate BNI
    #if EVENTS == 'calculate':
        #HEIGHT = float(VALUES['height'])
        #WEIGHT = float(VALUES['weight'])
        #BMI = health.imc(HEIGHT, WEIGHT)
        #WINDOWS['bmi'].update(str(BMI))
#sg.theme("LightBlue2")
WINDOWS = sg.Window("Login Screen", ui.LOGIN)
WINDOWS1 = sg.Window("Registration Screen", ui.REGISTRATION, element_justification='r')
while True:
    events, values = WINDOWS.read()
    if events == sg.WIN_CLOSED:
        break
    if events == "login":
        user_id = values['username']
        password = values['password']
        service = db.authenticate_db()
        response = db.get_record(user_id, "bmi", service)
        print(response)
        if bool(response):
            pass
        else:
            WINDOWS.close()
            while True:
                events1, values1 = WINDOWS1.read()
                if events1 == 'register':
                    DOCUMENT = {}
                    DOCUMENT["_id"] = values1["user id"]
                    DOCUMENT["first name"] = values1["first name"]
                    DOCUMENT["last name"] = values1["last name"]
                    DOCUMENT["Date of birth"] = values1["birth"]
                    DOCUMENT["weight"] = values1["weight"]
                    DOCUMENT["height"] = values1["height"]
                    DOCUMENT["password"] = values1["password"]
                    print(DOCUMENT)
                    service = db.authenticate_db()
                    db.insert_doc("bmi", DOCUMENT, service)
                    break
