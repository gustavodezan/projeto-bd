from dataclasses import fields
from datetime import datetime
from tkinter import Entry, messagebox
import tkinter.ttk as ttk
import tkinter as tk
import crud

class AutorScr(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.initUI()
        self.master.iconify()
    
    def initUI(self):
        self.geometry("800x600")
        style = ttk.Style(self)
        style.theme_use("clam")
        self.title("Registros")

        # Listar obras de arte
        lbl_arts = ttk.Label(self, text="Obras de Arte")
        lbl_arts.pack(fill=tk.X, padx=15, pady=5)
        # read events with and show them in a listbox
        self.arts = tk.Listbox(self)
        self.arts.pack(fill=tk.X, padx=15, pady=5)
        # read events from database
        arts = crud.select_all("Autor")

        labels = ["Codigo", "Nome", "Dono", "Ala"]
        arts.insert(0, labels)
        i = 0
        for art in arts:
            if i != 0:
                nome_obra = art[7]
                nome_dono = crud.select_record("DonoArte", "Codigo", str(art[1]))[2]
                nome_ala = crud.select_record("Ala", "Codigo", str(art[2]))[1]
                art = list(art[:1]) + [nome_obra] + [nome_dono] + [nome_ala]
            self.arts.insert(tk.END, art)
            i += 1
        # create CRUD buttons
        btn_selecionar = ttk.Button(self, text="Selecionar", command=lambda:self.read(self.arts.get(self.arts.curselection())[0]))
        btn_selecionar.pack(fill=tk.X, padx=15, pady=5)

        btn_create = ttk.Button(self, text="Criar", command=lambda:CreateAutorScr(self))
        btn_create.pack(fill=tk.X, padx=15, pady=5)

        btn_update = ttk.Button(self, text="Atualizar", command=lambda:self.update())
        btn_update.pack(fill=tk.X, padx=15, pady=5)

        btn_delete = ttk.Button(self, text="Deletar", command=lambda:self.delete())
        btn_delete.pack(fill=tk.X, padx=15, pady=5)

        btn_back = ttk.Button(self, text="Voltar", command=self.destroy)
        btn_back.pack(fill=tk.X, padx=15, pady=5)
        
    def cancel(self):
        self.create_window.destroy()

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


class VisualizeAutorScr(tk.Toplevel):
    def __init__(self, master=None, codigo=None, codigo_arte=None):
        super().__init__(master=master)
        self.codigo = codigo
        self.codigo_arte = codigo_arte
        self.initUI()
        self.master.iconify()
    
    def initUI(self):
        self.geometry("800x600")
        style = ttk.Style(self)
        style.theme_use("clam")
        self.title("Visualizar Obra de Arte")

        # Selecionar obra de arte no banco
        try:
            dono = crud.select_record("Autor", "Codigo", str(self.codigo))
        except:
            dono = ""
        # Listar informações da obra de arte uma por linha
        lbl_dono = ttk.Label(self, text="Informações sobre o Aurtista")
        lbl_dono.pack(fill=tk.X, padx=15, pady=5)
        
        labels = ["Codigo", "Nome", "Data de Nascimento", "Data de Falescimento", "País de Origem"]

        self.frame = tk.Frame(self)
        self.frame.pack(fill=tk.X, padx=15, pady=5)
        i = 0
        for item in dono:
            item = labels[i] + ": " + str(item)
            lbl = ttk.Label(self.frame, text=item)
            lbl.pack(fill=tk.X, padx=15, pady=5)
            i += 1
        
        # Botão de voltar
        btn_back = ttk.Button(self, text="Voltar", command=self.voltar)
        btn_back.pack(fill=tk.X, padx=15, pady=5)

    def voltar(self):
        self.master.deiconify()
        self.destroy()

class CreateAutorScr(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.initUI()
        self.master.iconify()

    def initUI(self):
        self.geometry("800x600")
        style = ttk.Style(self)
        style.theme_use("clam")
        self.title("Criar")

        # Create inputs:
        lbl_nome = ttk.Label(self, text="Nome")
        lbl_nome.pack(fill=tk.X, padx=15, pady=5)
        self.nome = tk.StringVar()
        txt_nome = ttk.Entry(self, textvariable=self.nome)
        txt_nome.pack(fill=tk.X, padx=15, pady=5)

        lbl_codigo_ala = ttk.Label(self, text="CodigoAla")
        lbl_codigo_ala.pack(fill=tk.X, padx=15, pady=5)
        self.codigo_ala = tk.StringVar()
        txt_codigo_ala = ttk.Entry(self, textvariable=self.codigo_ala)
        txt_codigo_ala.pack(fill=tk.X, padx=15, pady=5)

        lbl_data_inicio = ttk.Label(self, text="DataInicio")
        lbl_data_inicio.pack(fill=tk.X, padx=15, pady=5)
        self.data_inicio = tk.StringVar()
        txt_data_inicio = ttk.Entry(self, textvariable=self.data_inicio)
        txt_data_inicio.pack(fill=tk.X, padx=15, pady=5)

        lbl_data_fim = ttk.Label(self, text="DataFim")
        lbl_data_fim.pack(fill=tk.X, padx=15, pady=5)
        self.data_fim = tk.StringVar()
        txt_data_fim = ttk.Entry(self, textvariable=self.data_fim)
        txt_data_fim.pack(fill=tk.X, padx=15, pady=5)

        lbl_descricao = ttk.Label(self, text="Descricao")
        lbl_descricao.pack(fill=tk.X, padx=15, pady=5)
        self.descricao = tk.StringVar()
        txt_descricao = ttk.Entry(self, textvariable=self.descricao)
        txt_descricao.pack(fill=tk.X, padx=15, pady=5)

        lbl_instituicao = ttk.Label(self, text="Instituicao")
        lbl_instituicao.pack(fill=tk.X, padx=15, pady=5)
        self.instituicao = tk.StringVar()
        txt_instituicao = ttk.Entry(self, textvariable=self.instituicao)
        txt_instituicao.pack(fill=tk.X, padx=15, pady=5)


        # create a button to confirm the creation
        btn_confirm = ttk.Button(self, text="Confirmar", command=lambda:self.confirm())
        btn_confirm.pack(fill=tk.X, padx=15, pady=5)

        # create a button to cancel the creation
        btn_cancel = ttk.Button(self, text="Cancelar", command=lambda:self.cancel())
        btn_cancel.pack(fill=tk.X, padx=15, pady=5)

    def confirm(self):
        try:
            nome = self.nome.get()
            codigo_ala = self.codigo_ala.get()
            data_inicio = self.data_inicio.get()
            data_inicio = datetime.strptime(data_inicio, "%d/%m/%Y")
            data_fim = self.data_fim.get()
            data_fim = datetime.strptime(data_fim, "%d/%m/%Y")
            descricao = self.descricao.get()
            instituicao = self.instituicao.get()
            crud.insert("Evento", nome, codigo_ala, data_inicio, data_fim, descricao, instituicao)
            self.master.refresh()
            self.destroy()
        except Exception as e:
            # show messagebox with error
            messagebox.showerror("Erro", e)

    def cancel(self):
        self.master.deiconify()
        self.destroy()
    
    def refresh(self):
        self.destroy()
        self.__init__()
        

if __name__ == "__main__":
    root = tk.Tk()
    DonoScr(root)
    root.mainloop()