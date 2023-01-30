"""
This is the UI code. One thing, actually I don't now
how to test the elements of this UI.
"""
import PySimpleGUI as sg
from bmic.src import health

#I declare the layout here
layout = [
  [sg.Text('Weight'), [sg.Input(), key='input1']]
  [sg.Text('height'), [sg.input(), key='input2']],
  [sg.Button('Calculate'), key='button1']
  [sg.Text('BMI'), [sg.text('N/A')]]
]

#The line below create the windows
window = sg.Windows('Calculate your BMI', layout)

#infinite loop to catch different events related to the application
while True:
  #The line use below, allowed to catch windows events an their values
  event, values = window.read()
  #Line use to close the windows when the user hit the cross icon above the windows
  if event == sg.WIN_CLOSED:
    break
    
#Just to be sure that the window will be close properly
window.close()
