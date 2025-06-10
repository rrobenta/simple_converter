import FreeSimpleGUI as sg
from converters import convert

label1 = sg.Text('Enter feet:')
input1 = sg.InputText(key="feet")

label2 = sg.Text('Enter inches:')
input2 = sg.InputText(key="inches")

btn = sg.Button('Convert')
output_label = sg.Text("", key="output")

window = sg.Window('Converter', layout = [[label1, input1],[label2, input2],[btn, output_label]])

while True:
    event, values = window.read()
    feet = float(values["feet"])
    inches = float(values['inches'])
    result = convert(feet, inches)
    window["output"].update(value=f"{result} m", text_color='white')

window.close()
