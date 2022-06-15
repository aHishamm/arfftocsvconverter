import arfftoCsv 
import PySimpleGUI as sg

sg.theme('Dark Red')
layout = [[sg.Text('Select an .arff/.csv file: ')], 
        [sg.Input(key='-FILE-',visible=False,enable_events=True),sg.FileBrowse()], 
        [sg.Button('Convert/Transpose'),sg.Button('Cancel')]]

window = sg.Window('Window Title', layout) 
while True: 
    event,values = window.read() 
    print(values['-FILE-'])
    path_to_file = values['-FILE-']
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break 
    if event == 'Convert': 
        if path_to_file.endswith('.arff'): 
            print('the file selected is an arff file')
            csvList = arfftoCsv.main(path_to_file)
        if path_to_file.endswith('.csv'): 
            print('The file that is selected is a csv file')
            csvTranspose = arfftoCsv.transposition(path_to_file)
window.close() 
