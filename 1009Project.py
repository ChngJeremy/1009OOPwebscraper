import PySimpleGUI as gui
import sqlite3
import matplotlib.pyplot as plt
import os


conn = sqlite3.connect('crawler.db')
sql = conn.cursor()

sql.execute('''CREATE TABLE IF NOT EXISTS stockdb
           ([ID] INTEGER PRIMARY KEY,[Stock] text, [Source] text, [Date_created] date, [Comment] text,[Sentiment] text)''')
#sql.execute('''DELETE FROM stockdb''')

conn.commit()

#for row in sql.execute('''SELECT * FROM stockdb '''):
#   print(row)


gui.change_look_and_feel('BlueMono')
sourceSelection = ("GME", "AMC")
layout = [
    [gui.Text("Stocks")],
    [gui.Combo(sourceSelection, size=(40, 7), enable_events=True, key='-COMBO-')],
    [gui.Text("Source")],
    [gui.Checkbox('All', change_submits= True, default=False, key='-CheckAll-'),
     gui.Checkbox('Reddit', key=1),
     gui.Checkbox('Twitter', key=2),],
    [gui.Button("GO")]
]

# Create the window
window = gui.Window("Data Crawler Application", layout, margins=(300, 250))





# Create an event loop
while True:
    socialMedia = []
    event, values = window.read()
    #Check all boxes when selected

    if event == '-CheckAll-':
        if values['-CheckAll-'] is True:
            window.find_element('-CheckAll-').Update(text='Deselect', value=True)
            for x in range(1,3):
                window.Element(x).Update(True)
        #Uncheck all boxes
        else:
            window.find_element('-CheckAll-').Update(text='All', value=False)
            for x in range(1, 3):
                window.Element(x).Update(False)



    #Once everything is selected, time to start crawling
    if event == "GO":
        #If check all is select, the first item in the array will store it
        if values['-CheckAll-'] is True:
            socialMedia.append('all')
        #Else assign the key of the social media into the array
        else:
            for x in range(1,3):
                print(window.find_element(x))
                if values[x] is True:
                    socialMedia.append(x)

        #Check for which stocks is selected
        if values['-COMBO-'] != '':
            combo = values['-COMBO-']  # use the combo key
            break

    if event == gui.WIN_CLOSED:
        print("Deleting...")
        #sql.execute('''DELETE FROM stockdb''')
        conn.close()
        quit()


window.close()

print(combo) #Which stock is chosen
print(socialMedia) #key of social media
socialMedia = socialMedia[0]
#os.system("java -classpath C:/Users/caizh/Desktop/reddit.jar  MainPage " + str(socialMedia) + " " + combo) #(java -classpath -location- -mainclass-)


if socialMedia == 1 or socialMedia == 2:

    sql.execute('''SELECT * FROM stockdb''')
    sentimentTotal = sql.fetchone()
    sentimentTotal = sentimentTotal[0]

    sql.execute('''SELECT COUNT(*) FROM stockdb WHERE Sentiment = "Positive"''')
    sentimentPositive = sql.fetchone()
    sentimentPositive = sentimentPositive[0]/sentimentTotal

    sql.execute('''SELECT COUNT(*) FROM stockdb WHERE Sentiment = "Super Positive"''')
    sentimentSuperPositive = sql.fetchone()
    sentimentSuperPositive = sentimentSuperPositive[0]/sentimentTotal

    sql.execute('''SELECT COUNT(*) FROM stockdb WHERE Sentiment = "Neutral"''')
    sentimentNeutral = sql.fetchone()
    sentimentNeutral = sentimentNeutral[0]/sentimentTotal

    sql.execute('''SELECT COUNT(*) FROM stockdb WHERE Sentiment = "Negative"''')
    sentimentNegative = sql.fetchone()
    sentimentNegative = sentimentNegative[0]/sentimentTotal

    sql.execute('''SELECT COUNT(*) FROM stockdb WHERE Sentiment = "Super Negative"''')
    sentimentSuperNegative = sql.fetchone()
    sentimentSuperNegative = sentimentSuperNegative[0]/sentimentTotal

    labels=[]
    sizes =[]
    if sentimentPositive != 0:
        labels.append("Positive")
        sizes.append(sentimentPositive)
    if sentimentSuperPositive !=0:
        labels.append("Super Positive")
        sizes.append(sentimentSuperPositive)
    if sentimentNeutral != 0:
        labels.append("Neutral")
        sizes.append(sentimentNeutral)
    if sentimentNegative != 0:
        labels.append("Negative")
        sizes.append(sentimentNegative)
    if sentimentSuperNegative !=0:
        labels.append("Super Negative")
        sizes.append(sentimentSuperNegative)
    print(sizes)
    print(labels)
    #sizes = [sentimentPositive, sentimentSuperPositive, sentimentNeutral, sentimentNegative, sentimentSuperNegative]
    #explode = (0, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.savefig('Sentiments.png')
    sql.execute('''SELECT Comment,Sentiment FROM stockdb ORDER BY Sentiment''')
    queryComments = sql.fetchall()
    data = []
    for rows in queryComments:
        data.append([rows[0],rows[1]])
    #data = [[j for j in range[20]] for i in queryComments]

    #15 rows 6 columns
    #data = [[row for row in queryComments[0]] for col in queryComments]

    header_list = ['Comments', 'Sentiment']
    table = gui.Table(values=data,
                        max_col_width=50,
                        headings=header_list,
                        auto_size_columns=True,
                        num_rows=100,
                        justification='center',
                        alternating_row_color='lightblue',
                        display_row_numbers=True,
                        key='tableyt')
    tab1_layout = [[gui.Text(combo,size="90")], [gui.Image(r'Sentiments.png')],[table]]
else:
    pass
######GUI

#
# if socialMedia == 1:
#     pass
#     # tab1_layout = [[gui.Text('Reddit')],
#     #                [gui.Text('Put your layout in here')],
#     #                [gui.Text('Input something')], [gui.Image(r'Sentiments.png')]]
# elif socialMedia[0] == 2:
#     tab1_layout = [[gui.Text('Twitter')],
#                    [gui.Text('Put your layout in here')],
#                    [gui.Text('Input something')], [gui.Image(r'Sentiments.png')]]
# elif socialMedia == '-CheckAll-':
#     tab1_layout = [[gui.Text('Reddit')],
#                    [gui.Text('Put your layout in here')],
#                    [gui.Text('Input something')], [gui.Image(r'Sentiments.png')]]
#     tab2_layout = [[gui.Text('Twitter')],
#                    [gui.Text('Put your layout in here')],
#                    [gui.Text('Input something')], [gui.Image(r'Sentiments.png')]]

# tab2_layout = [[gui.Text('Tab 2')]]
# tab3_layout = [[gui.Text('Tab 3')]]
# tab4_layout = [[gui.Text('Tab 3')]]

# The TabgGroup layout - it must contain only Tabs
tab_group_layout = [[gui.Tab('Reddit', tab1_layout,table, font='Courier 15', key='-TAB1-')]]

# The window layout - defines the entire window
col = [[gui.TabGroup(tab_group_layout,
                       enable_events=True,
                       key='-TABGROUP-')]]
layout = [[gui.Column(col,size=(700,500),scrollable=True)]]

secondWin = gui.Window('Data Crawler Application', layout)


while True:
        event, values = secondWin.read()
        if event == gui.WIN_CLOSED:
            print("Deleting...")
            #sql.execute('''DELETE FROM stockdb''')
            conn.close()
            os.remove("Sentiments.png")
            exit()

secondWin.close()



