#import openpyxl

#book = openpyxl.load_workbook('relação_de_alunos.xlsx')

#sheet = book.active

#cells = sheet['E2': 'E6']

#print(cells.)

'''from openpyxl import load_workbook
wb = load_workbook(filename='relação_de_alunos.xlsx', read_only=True)
ws = wb['Registros'] # ws agora é uma IterableWorksheet


for a in ws.rows:
    print(a[4].value)
'''
'''
import sys
 
x='si'
 
while x=='si':
    tecla = sys.stdin.read(1)
    if tecla != 's':
        print ('Has presionado '+ tecla)
    else:
        x='no'
        print ('Se rompe el bucle')

from tkinter import *
root=Tk()

class novo:

        def __init__(self, janela):
            self.caixa=Frame(janela)
            self.caixa.grid()
            self.b=Button(janela, text='Abrir', command=self.new_jan)
            self.b.grid()
            self.l1=Label(janela, text='raiz!')
            self.l1.grid()

        def new_jan(self):
            self.jan=Toplevel()
            self.l=Label(self.jan, text='Feche esta para poder voltar a raiz!')
            self.l.grid()
            b=Button(self.jan, text='Fechar', command=self.fecha_jan)
            b.grid()
            self.jan.geometry('300x200')
            self.jan.transient(root)#Sempre aberta
            self.jan.focus_force()#Quando abrir foco nela
            self.jan.grab_set()#Não usar botoes da outra

        def fecha_jan(self):
            self.jan.destroy()


novo(root)

root.geometry('300x200')

root.mainloop()
'''
from pygame import mixer
mixer.init()
mixer.music.load('fim.mp3')
mixer.music.play()
