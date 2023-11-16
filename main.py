import sqlite3 as db
from logs import*
import PySimpleGUI as sg
from saglaba import *
key_ievad  = ( "T-KATEG-", "T-NOSAUK-", "T-RAKSTUR-", "T-CENA-")
key_li = ( "-KATEG-", "-NOSAUK-", "-RAKSTUR-", "-CENA-")
with db.connect("nomat.db") as con:
    cur = con.cursor()
    logs = Logs(cur)
    window = logs.logu_veido()
    event = ""
while event !=sg.WIN_CLOSED and event != "Atcelt":
    event, values= window.read()
    if event in key_li:
        text_event = "T"+event
        values[event] = values[event][0][0]
        window[text_event].update(values[event])
    elif (event == "Ievadīt"):
        flag =1
        saglabat=[]
        for x in key_ievad:
            if values[x] == "":
                flag = 0; break 

            else:
                saglabat.append(values[x])
        if flag:
            sg.popup(saglabat, background_color= "#FF0000")
            prod1 = Saglaba(cur,saglabat[0], "Kategorija")
            prod1.saglaba_jauno(cur,saglabat[0], "Kategorija")
            con.commit()
            prod1.druka_tab(cur,"Kategorija")
        else:
            sg.popup("Kļūda", "Aizpildīt visus laukus", background_color= "#FF0000")
window.close()