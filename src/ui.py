"""
This is the UI code. One thing, actually I don't now
how to test the elements of this UI.
"""
import PySimpleGUI as sg
import health

#The layout for bmi calculation windows
BMI = [
  [sg.Text('Weight'), [sg.Input(key='input1')]],
  [sg.Text('height'), [sg.Input(key='input2')]],
  [sg.Button('Calculate', key='calculate')],
  [sg.Text('N/A', key='bmi')]
]
#The layout for registration windows
REGISTRATION = [
  [sg.Text("Phone Number"), [sg.Input(key="phone")]],
  [sg.Text("First Name"), [sg.Input(key="first name")]],
  [sg.Text("Last Name"), [sg.Input(key="last name")]],
  [sg.Text("Date of Birth"), [sg.Input(key="birth")]],
  [sg.Text("weight"), [sg.Input(key="weight")]],
  [sg.Text("Height"), [sg.Input(key="height")]]
]
#The layout for notification windows
NOTIFICATION = [
    [sg.Text("Notification", key="notification")]
]
#The layout for login windows
LOGIN = [
  [sg.Text("username"), [sg.Input(key="username")]],
  [sg.Text("password"), [sg.Input(key="password")]]
]
