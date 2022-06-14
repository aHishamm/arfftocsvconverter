import PySimpleGUI as sg 

#sg.theme('DarkAmber')

layout = [ [sg.Text('Some text on row 1')], 
        [sg.Text('Enter something on row 2'), sg.InputText()], 
        [sg.Button('Ok'),sg.Button('Cancel')]] 

window = sg.Window('Window Title', layout) 
while True: 
    event,values = window.read() 
    if event == sg.WIN_CLOSED or event == 'Cancel': 
        break 
    print('You entered',values[0])
window.close() 