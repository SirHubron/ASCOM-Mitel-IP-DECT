import os
from pathlib import Path

'''MAIN PROGRAMM'''
#README-BEREICH

print(
    'PRINZIP-EASYREG TOOL' '\n'
    'Sie werden dazu aufgefordert einen Internnummernbereich anzugeben.' '\n'
    '(Bitte den Bereich der IP-DECT Telefone angeben)' '\n'
    'In den nächsten Schritten wird immer die erste Internnummer mit der ersten IPEI verknüpft,' '\n'
    'und das immer so weiter bis es keine Angaben mehr gibt von Ihnen.' '\n\n'
    'Tool by Aaron Huber' '\n\n'
)


'''Programmierung'''
#Konfigurationsbereich

'''Path-definder'''

home = str(Path.home())
myPath = os.path.join(home, "Desktop")


'''File Creator'''

class TextFile(): #File erstellen mit Spezifischem Titel
    def __init__(self,title):
        self.title = title

    def createfile(self,num1,num2,run):
        with open(f'{myPath}{self.title}.txt','a') as newtxt:
                if run == False:
                    print('Es werden keine IPEI aufgefordert!')
                    for i in range(num1,num2 + 1):
                        newtxt.write(f'{str(i)};;{str(i)};;;;;;\n')
                while run is True:
                    for i in range(num1,num2 + 1):
                        ipeiinput = input('IPEI: ')
                        if ipeiinput != 'quit':
                            ipei(ipeiinput)
                            newtxt.write(f'{str(i)};;{str(i)};;;;{str(ipeiinput)};;\n')
                        else:
                            print('ENDE!!')
                            run = 'Finished'
                            break



'''Internernummernbereich'''

def number(dir): #Nummer Eingabe überpüfung
    if len(dir) != 3 and len(dir) != 4:
        lendir = input('Bitte geben sie eine 3 oder 4 stellige Internnummer ein!: ')
        dir = lendir
    for i in dir:
        if not str(dir).isdecimal():
            decdir = input('Bitte geben sie eine ZAHL ein!: ')
            dir = decdir
    print(dir)
    return dir



'''IPEI-Eingabe'''

def ipei(ipdi): #IPEI Eingabe überprüfen
    if len(ipdi) != 13:
        ipdi = input('Die IPEI muss 13 stellen lang sein: ')
    for i in range(0,12):
        if not ipdi[i].isdecimal():
            ipdi = input('Der Inhalt der IPEI müssen zahlen sein: ')
    for i in ipdi[12]:
        if not ipdi[12].isdecimal and ipdi[12] != '*':
            ipdi = input('Der letzte Chrakter der IPEI muss eine Zahl oder ein * sein: ')



'''Verknüpfungen'''

filetitle = input('Bitte geben sie ein wie das File heissen sollte: ')
fileobj = TextFile(filetitle) #Erstellen des Files mit dem Titel

firstnum = input('Bitte geben sie die Erste Nummer des Berreiches an: ') #1. Nummereingabe
number(firstnum)
lastnum = input('Bitte geben sie die letzte Nummer des Berreiches an: ') #2. Nummereingabe
number(lastnum)

print('Sie können jederzeit mit der eingabe von "quit" die IPEI eingabe stoppen.')
startipei = None
start = input('Wollen sie IPEIs eingeben? Ja[y] oder Nein[n]: ')
if start == 'n' or start == 'Nein':
    startipei = False
elif start == 'y' or start == 'Ja':
    startipei = True
else:
    print('Ungültige Eingabe!')

fileobj.createfile(int(firstnum),int(lastnum),bool(startipei)) #Den Nummernbereich am File weitergeben
