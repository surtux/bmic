"""
This is the UI code. One thing, actually I don't now
how to test the elements of this UI.
"""
import PySimpleGUI as sg

#I declare the layout here
layout = [
  [sg.Text('Weight'), [sg.Input()]]
  [sg.Text('height'), [sg.input()]],
  [sg.Text('BMI'), [sg.text('N/A')]]
]

windows = sg.Windows('Calculate your BMI', layout).read()
