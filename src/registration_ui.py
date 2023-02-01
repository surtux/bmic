"""
This is the registration form for our project app
"""
import PySimpleGUI as sg
import db
import datetime as dat

LAYOUT1 = [
    [sg.Text("First Name", key='first'), [sg.Input(key='input1')]],
    [sg.Text("Last Name", key='last'), [sg.Input(key='input2')]],
    [sg.Text("Date of Birth", key='birth'), [sg.Input(key='input3')]],
    [sg.Text("weight", key='weight'), [sg.Input(key='input4')]],
    [sg.Text("Height", key='height'), [sg.Input(key='input5')]]
]

LAYOUT2 = [
    [sg.Text("registration answer", key='answer')]
]

def create_registration(layout):
    """I use this function to create registration form"""
    return sg.window("registration", LAYOUT1)

def registration_answer(layout):
    """I use this function to create registration answer window"""
    return sg.window("answer", LAYOUT2)