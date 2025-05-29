import FreeSimpleGUI as sg

label1 = sg.Text('Enter feet:')
input1 = sg.InputText()

label2 = sg.Text('Enter inches:')
input2 = sg.InputText()

btn = sg.Button('Convert')

window = sg.Window('Converter', layout = [[label1, input1],[label2, input2],[btn]])

window.read()
window.close()
