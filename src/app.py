"""
This application keep track of the bmi so that one
can control his health
"""
import db
import PySimpleGUI as sg
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
            WINDOWS1.read()
