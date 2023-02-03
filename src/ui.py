"""
This is the UI code. One thing, actually I don't now
how to test the elements of this UI.
"""
import PySimpleGUI as sg

#The layout for bmi calculation windows
BMI = [
  [sg.Push(), sg.Text('Weight'), sg.Input(key='-WEIGHT-')],
  [sg.Text('height'), sg.Input(key='-HEIGHT-')],
  [sg.Button('Calculate', key='-CALCULATE-'), sg.Text('N/A', key='-BMI-')]
]
#The layout for registration windows
REGISTRATION = [
  [sg.Text("User ID"), sg.Input(key="user id")],
  [sg.Text("First Name"), sg.Input(key="first name")],
  [sg.Text("Last Name"), sg.Input(key="last name")],
  [sg.Text("Date of Birth"), sg.Input(key="birth")],
  [sg.Text("weight"), sg.Input(key="weight")],
  [sg.Text("Height"), sg.Input(key="height")]
]
#The layout for notification windows
NOTIFICATION = [
    [sg.Text("Notification", key="notification")]
]
#The layout for login windows
LOGIN = [
  [sg.Text("username"), sg.Input(key="username")],
  [sg.Text("password"), sg.Input(key="password")],
  [sg.Push(), sg.Button("Login",key="login"),sg.Text("Forgot Password", key="forgot password"), sg.Button("register", key="register")]
]
