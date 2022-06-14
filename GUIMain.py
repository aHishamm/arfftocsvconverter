import arfftoCsv 
import PySimpleGUI as sg

sg.theme('Dark Red')

layout = [[sg.Text('Select an .arff file: ')], 
        [sg.Input(key='-FILE-',visible=False,enable_events=True),sg.FileBrowse()], 
        [sg.Button('Convert'),sg.Button('Cancel')]]

window = sg.Window('Window Title', layout) 
while True: 
    event,values = window.read() 
    print(values['-FILE-'])
    path_to_arff = values['-FILE-']
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break 
    if event == 'Convert': 
        csvList = arfftoCsv.main(path_to_arff)
        #csvList = arfftoCsv.main(layout[1])
window.close() 
