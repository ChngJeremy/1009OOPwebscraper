import PySimpleGUI as gui
import os

gui.change_look_and_feel('BlueMono')
sourceSelection = ("GME", "DOGE", "AMC")
layout = [
    [gui.Text("Stocks")],
    [gui.Combo(sourceSelection, size=(40, 7), enable_events=True, key='-COMBO-')],
    [gui.Text("Source")],
    [gui.Checkbox('All', change_submits= True, key='-CheckAll-'),
     gui.Checkbox('Reddit', key=1),
     gui.Checkbox('Twitter', key=2),
     gui.Checkbox('StockTwits', key=3)],
    [gui.Button("GO")]
]

# Create the window
window = gui.Window("Data Crawler Application", layout, margins=(300, 250))





# Create an event loop
while True:
    socialMedia = []
    event, values = window.read()
    #Check all boxes when selected
    if values['-CheckAll-'] is True:
        window.find_element('-CheckAll-').Update(text='Deselect', value=True)
        for x in range(1,4):
            window.Element(x).Update(True)
    #Uncheck all boxes
    else:
        window.find_element('-CheckAll-').Update(text='All', value=False)
        for x in range(1, 4):
            window.Element(x).Update(False)



    #Once everything is selected, time to start crawling
    if event == "GO":
        #If check all is select, the first item in the array will store it
        if values['-CheckAll-'] is True:
            socialMedia.append('all')
        #Else assign the key of the social media into the array
        else:
            for x in range(1,4):
                print(window.find_element(x))
                if values[x] is True:
                    socialMedia.append(x)

        #Check for which stocks is selected
        if values['-COMBO-'] != '':
            combo = values['-COMBO-']  # use the combo key
            break

    if event == gui.WIN_CLOSED:
        exit()



window.close()

print(combo) #Which stock is chosen
print(socialMedia) #key of social media

os.system("java -classpath C:/Users/caizh/Desktop/Test.jar  MainPage") #(java -classpath -location- -mainclass-)

layout = [
                [gui.Text("This is the 2nd layout")],
                [gui.Text("Data should be shown here")],
                [gui.Button("Close")]]

secondWin = gui.Window("Test", layout, margins=(300, 300))

while True:
        event, values = secondWin.read()
        if event == 'Close':
            break
        if event == gui.WIN_CLOSED:
            exit()
secondWin.close()



