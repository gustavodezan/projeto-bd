# Frontend
from tkinter import *
import tkinter.messagebox

State = 0; #controle de estados das telas

def MainScr():
    def Logged():
        global State
        State = 1
        MainScr.update()
        MainScr.destroy()

    def GetInput():
        UsrBox= Usr.get()
        PwdBox= Pwd.get()
        #UsrOK = False #Buscar se user existe na database
        #PwdOK = False#Buscar se senha do user está correta
        if UsrBox == '123' :
            if PwdBox == '123':
                Logged()
            else:
                tkinter.messagebox.showinfo('Erro!', 'Senha inválida.')
        else:
            tkinter.messagebox.showinfo('Erro!', 'Usuário não encontrado.')
    
    def Quit():
        global State
        State = -1
        MainScr.quit()

    MainScr = Tk()
    MainScr.geometry("640x480")#Resolução
    MainScr.title("Login")
    #TODO Centralizar janelas!

    #Título
    Label(text="MuseuBD", bg="grey", width="300", height="2", font=("Arial", 15)).pack(pady=30) 

    #Campo de usuário
    Label(text="Usuário (Código de identificação)", height="2", font=("Arial", 10)).pack()
    Usr = Entry(MainScr, width=40)
    Usr.focus_set()
    Usr.pack()

    #campo de senha
    Label(text="Senha", height="2", font=("Arial", 10)).pack()
    Pwd = Entry(MainScr, show="*", width=40)
    Pwd.pack()

    #login
    Button(text="Login", height="2", width="20", command=GetInput).pack(pady=30) 

    #Saída
    Button(text="Sair", height="2", width="10", command=Quit).pack(pady=40)

    MainScr.mainloop()

def MainUsr():
    def PrevPage():
        global State
        State = 0
        UsrScr.update()
        UsrScr.destroy()
    
    UsrScr = Tk()
    UsrScr.geometry("640x480")
    UsrScr.title("Opções do Usuário")

    #TODO fazer opções específicas de todos os users, desabilitar botões de acordo com privilégio de acesso
    Button(text="Opção 1", height="2", width="10", command=lambda: PrevPage()).grid(row=0, column=0)
    Button(text="Opção 2", height="2", width="10", command=lambda: PrevPage()).grid(row=0, column = 1)
    Button(text="Opção 3", height="2", width="10", command=lambda: PrevPage()).grid(row=0, column = 2)
    Button(text="Opção 4", height="2", width="10", command=lambda: PrevPage()).grid(row = 1, column=0)
    Button(text="Opção 5", height="2", width="10", command=lambda: PrevPage()).grid(row = 1, column = 1)
    Button(text="Sair", height="2", width="10", command=lambda: PrevPage()).grid(row = 5, column= 0)

    UsrScr.mainloop()

def Core():
    global State
    while(State >= 0):
        if State == 0:
            MainScr()
        elif State == 1:
            MainUsr()
    #TODO estados adicionais para inserção de dados

Core()