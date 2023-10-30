import PySimpleGUI as sg

sg.theme('LightGray1')   # Add a touch of color

def calcButton(message='N/A'):  #Function that makes the buttons update calculation line
    window['input'].update(values['input'] + message)
    values['input'] = values['input'] + message
    print(message)

def calcAnswer(calculation='0'):    #Takes string as input and calculates math answer from that.
    result = eval(calculation)
    window['output'].update(result)

#All the stuff inside the window
layout = [  [sg.InputText('', enable_events=True, key='input'), sg.Text('Answer', key='output')],
            [sg.Button('(', key=lambda: calcButton('(')), sg.Button(')', key=lambda: calcButton(')')), sg.Button('/', key=lambda: calcButton('/'))],
            [sg.Button('7', key=lambda: calcButton('7')), sg.Button('8', key=lambda: calcButton('8')), sg.Button('9', key=lambda: calcButton('9')), sg.Button('*', key=lambda: calcButton('*'))],
            [sg.Button('4', key=lambda: calcButton('4')), sg.Button('5', key=lambda: calcButton('5')), sg.Button('6', key=lambda: calcButton('6')), sg.Button('-', key=lambda: calcButton('-'))],
            [sg.Button('1', key=lambda: calcButton('1')), sg.Button('2', key=lambda: calcButton('2')), sg.Button('3', key=lambda: calcButton('3')), sg.Button('+', key=lambda: calcButton('+'))],
            [sg.Button('0', key=lambda: calcButton('0')), sg.Button('.', key=lambda: calcButton('.')), sg.Button('(-)', key=lambda: calcButton('(-)')), sg.Button('=')] ]

# Create the Window
window = sg.Window('Python Calculator', layout, finalize=True)
window['input'].bind("<Return>", "_Enter")

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    elif event == '=':  # Actually calls the calculate function
        calcAnswer(values['input'])
    elif callable(event):   # Generic function call for all the buttons that just input stuff on the input line
        event()
    if event == 'input':    # Gets called when the user types something in the text box to be calculated
      if(len(values['input']) > 0):
        if (values['input'][-1] not in ('0123456789-+/*()')):
            sg.popup("Only math operators (+-/*()) and numbers")
            window['input'].update(values['input'][:-1])
            values['input'] = values['input'][:-1]
    if event == 'input' + '_Enter':
        calcAnswer(values['input'])

window.close()