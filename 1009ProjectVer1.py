import PySimpleGUI as gui
import os

gui.theme = ('Dark Blue 3')
sourceSelection = ("GME", "DOGE", "AMC")
layout = [
    [gui.Text("Stocks")],
    [gui.Combo(sourceSelection, size=(40, 7), enable_events=True, key='-COMBO-')],
    [gui.Text("Source")],
    [gui.Button("GO")],
]

# Create the window
window = gui.Window("Data Crawler Application", layout, margins=(300, 300))

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button

    if event == "GO" or event == gui.WIN_CLOSED:
        combo = values['-COMBO-']  # use the combo key
        print(combo)

        if combo != '':
            window.close()
            os.system("java -classpath C:/Users/caizh/Desktop/Test.jar  MainPage")
            #Open Second Layout
            layout = [
                [gui.Text("This is the 2nd layouy")],
                [gui.Text("Data should be shown here")],
                [gui.Button("Close")]]

            secondWin = gui.Window("Test", layout, margins=(300, 300))
            while True:
                event, values = secondWin.read()
                if values == 'Close' or gui.WIN_CLOSED:
                    break
            secondWin.close()

        else:
            break

window.close()
