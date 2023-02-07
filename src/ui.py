"""
This is the UI code. One thing, actually I don't now
how to test the elements of this UI.
"""
# pylint: disable=trailing-whitespace
import PySimpleGUI as sg

#The layout for bmi calculation windows
BMI = [
  [sg.Push(), sg.Text('Weight'), sg.Input(key='-WEIGHT-')],
  [sg.Text('height'), sg.Input(key='-HEIGHT-')],
  [sg.Button('Calculate', key='-CALCULATE-'), sg.Text('N/A', key='-BMI-')]
]
#The layout for registration windows
REGISTRATION = [
  [sg.Text("User ID"), sg.Input(key="_id")],
  [sg.Text("First Name"), sg.Input(key="first name")],
  [sg.Text("Last Name"), sg.Input(key="last name")],
  [sg.Text("Date of Birth"), sg.Input(key="Date of Birth")],
  [sg.Text("weight"), sg.Input(key="weight")],
  [sg.Text("Height"), sg.Input(key="height")],
  [sg.Text("password"), sg.Input(key="password")],
  [sg.Button("Register", key='register')]
]
#The layout for notification windows
NOTIFICATION = [
    [sg.Text("Notification", key="notification")],
    [sg.Text("message", enable_events=True, key="-MESSAGE-")]
]
#The layout for login windows
LOGIN = [
  [sg.Text("username"), sg.Input(key="_id")],
  [sg.Text("password"), sg.Input(key="password")],
  [sg.Push(), sg.Button("Login", key="login"), sg.Text("Forgot Password", key="forgot password")]
]
