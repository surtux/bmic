"""
This application keep track of the bmi so that one
can control his health
"""

import ui, db, health
import PySimpleGUI as sg

WINDOWS = sg.Window("BMI CALCULATION", ui.BMI)

while True:
    EVENTS, VALUES = WINDOWS.read()
    if EVENTS == sg.WIN_CLOSED:
        break
    
    if EVENTS == 'calculate':
        HEIGHT = float(VALUES['height'])
        WEIGHT = float(VALUES['weight'])
        BMI = health.imc(HEIGHT, WEIGHT)
        WINDOWS['bmi'].update(str(BMI))