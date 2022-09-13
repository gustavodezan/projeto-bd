from dataclasses import fields
from datetime import datetime
from tkinter import ttk
import tkinter as tk
import crud

class RegisterScr(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.initUI()
        self.master.iconify()
    
    def initUI(self):
        self.geometry("800x600")
        style = ttk.Style(self)
        style.theme_use("clam")
        self.title("Registros")

        # White label to show all users
        lbl_users = ttk.Label(self, text="Usuários")
        lbl_users.pack(fill=tk.X, padx=15, pady=5)
        # read users with and show them in a listbox
        self.users = tk.Listbox(self)
        self.users.pack(fill=tk.X, padx=15, pady=5)
        # read users from database
        users = crud.select_all("Funcionario")
        for user in users:
            self.users.insert(tk.END, user)

        # create CRUD buttons
        btn_create = ttk.Button(self, text="Criar", command=lambda:self.create())
        btn_create.pack(fill=tk.X, padx=15, pady=5)

        btn_update = ttk.Button(self, text="Atualizar", command=lambda:self.update())
        btn_update.pack(fill=tk.X, padx=15, pady=5)

        btn_delete = ttk.Button(self, text="Deletar", command=lambda:self.delete())
        btn_delete.pack(fill=tk.X, padx=15, pady=5)

        btn_back = ttk.Button(self, text="Voltar", command=self.destroy)
        btn_back.pack(fill=tk.X, padx=15, pady=5)

    def create(self):
        # abrir tela de criação
        print("Abrir tela de criação")
        # select if want to create a employee, a client or a item
        # create a new window
        self.create_window = tk.Toplevel(self)
        self.create_window.geometry("800x600")
        style = ttk.Style(self.create_window)
        style.theme_use("clam")
        self.create_window.title("Criar")

        # create a label to show the options
        lbl_options = ttk.Label(self.create_window, text="Criar")
        lbl_options.pack(fill=tk.X, padx=15, pady=5)

        # create a listbox to show the options
        self.options = tk.Listbox(self.create_window)
        self.options.pack(fill=tk.X, padx=15, pady=5)
        self.options.insert(tk.END, "Funcionário")
        self.options.insert(tk.END, "Cliente")
        self.options.insert(tk.END, "Item")

        # create a button to confirm the option
        btn_confirm = ttk.Button(self.create_window, text="Confirmar", command=lambda:self.confirm())
        btn_confirm.pack(fill=tk.X, padx=15, pady=5)

        # create a button to cancel the option
        btn_cancel = ttk.Button(self.create_window, text="Cancelar", command=lambda:self.cancel())
        btn_cancel.pack(fill=tk.X, padx=15, pady=5)
        
    def confirm(self):
        # open the window according to the option
        option = self.options.get(self.options.curselection())
        if option == "Funcionário":
            CreateEmployeeScr(self.create_window)
        elif option == "Cliente":
            pass
        elif option == "Item":
            pass
        else:
            print("Erro")
    def cancel(self):
        self.create_window.destroy()

    def read(self):
        # abrir tela de leitura
        print("Abrir tela de leitura")
        pass

    def update(self):
        # abrir tela de atualização
        print("Abrir tela de atualização")
        pass

    def delete(self):
        # abrir tela de deleção
        print("Abrir tela de deleção")
        pass

    def destroy(self):
        self.master.deiconify()
        super().destroy()
    
    def refresh(self):
        self.destroy()
        self.__init__()


class CreateEmployeeScr(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.type = type
        self.fields = fields
        self.initUI()
        self.master.iconify()

    def initUI(self):
        self.geometry("800x600")
        style = ttk.Style(self)
        style.theme_use("clam")
        self.title("Criar")

        # Create inputs for: Matricula, CPF, Nome, DataNascimento, DataContratacao, Funcao, Endereco):
        lbl_matricula = ttk.Label(self, text="Matricula")
        lbl_matricula.pack(fill=tk.X, padx=15, pady=5)
        self.matricula = ttk.Entry(self)
        self.matricula.pack(fill=tk.X, padx=15, pady=5)

        lbl_cpf = ttk.Label(self, text="CPF")
        lbl_cpf.pack(fill=tk.X, padx=15, pady=5)
        self.cpf = ttk.Entry(self)
        self.cpf.pack(fill=tk.X, padx=15, pady=5)

        lbl_nome = ttk.Label(self, text="Nome")
        lbl_nome.pack(fill=tk.X, padx=15, pady=5)
        self.nome = ttk.Entry(self)
        self.nome.pack(fill=tk.X, padx=15, pady=5)

        lbl_data_nascimento = ttk.Label(self, text="Data de Nascimento")
        lbl_data_nascimento.pack(fill=tk.X, padx=15, pady=5)
        self.data_nascimento = ttk.Entry(self)
        self.data_nascimento.pack(fill=tk.X, padx=15, pady=5)

        lbl_funcao = ttk.Label(self, text="Função")
        lbl_funcao.pack(fill=tk.X, padx=15, pady=5)
        self.funcao = ttk.Entry(self)
        self.funcao.pack(fill=tk.X, padx=15, pady=5)

        lbl_endereco = ttk.Label(self, text="Endereço")
        lbl_endereco.pack(fill=tk.X, padx=15, pady=5)
        self.endereco = ttk.Entry(self)
        self.endereco.pack(fill=tk.X, padx=15, pady=5)

        # create a button to confirm the creation
        btn_confirm = ttk.Button(self, text="Confirmar", command=lambda:self.confirm(lbl_matricula, lbl_cpf, lbl_nome, lbl_data_nascimento, lbl_funcao, lbl_endereco))
        btn_confirm.pack(fill=tk.X, padx=15, pady=5)

        # create a button to cancel the creation
        btn_cancel = ttk.Button(self, text="Cancelar", command=lambda:self.cancel())
        btn_cancel.pack(fill=tk.X, padx=15, pady=5)

    def confirm(self, lbl_matricula, lbl_cpf, lbl_nome, lbl_data_nascimento, lbl_funcao, lbl_endereco):
        # create a new employee
        matricula = self.matricula.get()
        cpf = self.cpf.get()
        nome = self.nome.get()
        data_nascimento = self.data_nascimento.get()
        funcao = self.funcao.get()
        endereco = self.endereco.get()
        if matricula == "":
            lbl_matricula.config(foreground="red")
        if cpf == "":
            lbl_cpf.config(foreground="red")
        if nome == "":
            lbl_nome.config(foreground="red")
        if data_nascimento == "":
            lbl_data_nascimento.config(foreground="red")
        if funcao == "":
            lbl_funcao.config(foreground="red")
        if endereco == "":
            lbl_endereco.config(foreground="red")
        if matricula != "" and cpf != "" and nome != "" and data_nascimento != "" and funcao != "" and endereco != "":
            # create a new employee
            data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
            crud.create_funcionario(matricula, cpf, nome, data_nascimento, datetime.now(), funcao, endereco)
            # reload the main screen
            self.master.master.refresh()
            self.master.destroy()
            self.destroy()

    
        

if __name__ == "__main__":
    root = tk.Tk()
    RegisterScr(root)
    root.mainloop()