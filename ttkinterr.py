from tkinter.ttk import *
from tkinter import *


def enviar_dados():
    button_enviar.configure(state=DISABLED)
    carregar_dados(0)

def carregar_dados(valor:int):
    progress['value']= valor
    if valor < 100:
        valor += 1
        janela.after(10, carregar_dados, valor)
    else:
        button_enviar.configure(state=NORMAL)
        
def comecar_barrinha():
    progress_aba1.start(10)
    button_aba1.configure(state=DISABLED)
    janela.after(4000,parar_barrinha)

def parar_barrinha():
    progress_aba1.stop()
    button_aba1.configure(state= DISABLED)

janela = Tk()
janela.geometry('500x500')
fonte = 'Verdano 12 Bold'

dias_semana = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']


#Label
label_semana = Label(janela, text='Escolha o dia da semana')

#Combobox
combobox_semana = Combobox(janela, values=dias_semana)
combobox_semana.set ('Escolha o dia da semana')

#Notebook
notebook_cadastro = Notebook(janela)
#
aba_1 = Frame(notebook_cadastro)
label_nome = Label (aba_1, text= 'Digite seu nome: ')
entry_nome = Entry(aba_1)
progress_aba1 = Progressbar(aba_1, lenght=100, mode='determinate')
button_aba1 = Button(aba_1, text='Enviar', command=comecar_barrinha)
notebook_cadastro.add(aba_1, text='Cadastro Pessoal')

#2
aba_2 = Frame(notebook_cadastro)
label_matematica = Label (aba_2, text= 'Digite sua nota: ')
entry_matematica = Entry(aba_2)
notebook_cadastro.add(aba_2, text='Notas')
progress = Progressbar(aba_2, length=100, mode='determinate')
button_enviar = Button(aba_2, text='Enviar', command=enviar_dados)
notebook_cadastro.add(aba_2, text='Notas')


#pack
combobox_semana.grid(row =0, column=0, padx=20, pady=20)
notebook_cadastro.grid(row=1, column=0)


label_nome.grid(row=0, column=0)
entry_nome.grid(row=0, column=1)
progress_aba1.grid(row=0, column=2 )
button_aba1.grid(row=0, column=3)

label_matematica.grid(row=0, column=0)
entry_matematica.grid(row=0, column=1)
progress.grid(row=1, column= 0)
button_enviar.grid(row=2, column=0)


janela.mainloop()