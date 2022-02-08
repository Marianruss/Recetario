from os import read
import random
from tkinter import Event
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import T, WIN_CLOSED

sg.theme("DarkBlue1")

def win1():
    layout = [
    [ sg.Text('Recetas al Azar para tu progresión')],
    [sg.Text("Progresión: 1")],
    [sg.Text("¿Que receta necesitás?")],
    [sg.Button("Desayunos/Meriendas"), sg.Button("Almuerzos/Cenas")],
    [sg.Button("Cerrar" )]]   

    window = sg.Window("Recetas",layout)
    return window

def win2(receta,comida):
    layout2 = [[sg.Text(receta)],
                    [sg.Button("Listo")]]

    w2= sg.Window(f"Receta {comida}", layout2)
    readed = False
    while not readed:
            event2,values2 = w2.read()
            if event2 == sg.WIN_CLOSED or event2 == "Listo":
                w2.close()
                readed = True

def desayunos():
    file = open('Progresión 1-Desayunos.txt','r' , encoding="utf-8")
    content = file.read()
    s = content.split("###")
    receta = random.choice(s)
    return receta

def almuerzos():
    file = open('Progresión-1-Almuerzos-Cenas.txt','r' , encoding="utf-8")
    content = file.read()
    s = content.split("###")
    receta = random.choice(s)
    return receta

def main():

    close = False
    win = win1()
    while not close:
        
        event,values = win.read()
        #Cierra la ventana
        if event == sg.WIN_CLOSED or event == "Cerrar":
            close = True
        #Muestra una receta random de desayunos/meriendas en una nueva ventana
        elif event == "Desayunos/Meriendas":
            desayuno = desayunos()
            win2(desayuno,"desayuno")
            
        elif event == "Almuerzos/Cenas":
            almuerzo = almuerzos()
            win2(almuerzo,"almuerzo")



            

main()
