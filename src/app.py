"""
This application keep track of the bmi so that one
can control his health
"""
#import db
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
WINDOWS = sg.Window("Login Screen", ui.LOGIN).read()
