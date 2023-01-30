"""
This is the UI code. One thing, actually I don't now
how to test the elements of this UI.
"""
import PySimpleGUI as sg
import health

#I declare the layout here
LAYOUT = [
  [sg.Text('Weight'), [sg.Input(key='input1')]],
  [sg.Text('height'), [sg.Input(key='input2')]],
  [sg.Button('Calculate', key='calculate')],
  [sg.Text('BMI', enable_events=True), [sg.Text('N/A', key='bmi')]]
]

#The line below create the windows
WINDOW = sg.Window('Calculate your BMI', LAYOUT)

#infinite loop to catch different events related to the application
while True:
    #The line use below, allowed to catch windows events an their values
    EVENT, VALUES = WINDOW.read()
    #Line use to close the windows when the user hit the cross icon above the windows
    if EVENT == sg.WIN_CLOSED:
        break
    #From the line below, we get the value of the height and weight and compute the bmi
    if EVENT == 'calculate':
        HEIGHT = float(VALUES['input2'])
        WEIGHT = float(VALUES['input1'])
        BMI = health.imc(HEIGHT, WEIGHT)
        WINDOW['bmi'].update(str(BMI))
#Just to be sure that the window will be close properly
WINDOW.close()
