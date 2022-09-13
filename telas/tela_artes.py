from dataclasses import fields
from datetime import datetime
import io
from tkinter import Entry, Image, messagebox
from tkinter.filedialog import askopenfiles
import tkinter.ttk as ttk
import tkinter as tk
import crud
from telas.tela_dono import VisualizeDonoScr
from telas.tela_autor import VisualizeAutorScr
import PIL.Image, PIL.ImageTk

class ArtesScr(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.initUI()
        self.master.iconify()
    
    def initUI(self):
        self.geometry("1000x800")
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
        arts = crud.select_all("ObraDeArte")

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

        btn_create = ttk.Button(self, text="Criar", command=lambda:CreateArtScr(self))
        btn_create.pack(fill=tk.X, padx=15, pady=5)

        btn_update = ttk.Button(self, text="Atualizar", command=lambda:self.update())
        btn_update.pack(fill=tk.X, padx=15, pady=5)

        btn_delete = ttk.Button(self, text="Deletar", command=lambda:self.delete())
        btn_delete.pack(fill=tk.X, padx=15, pady=5)

        btn_back = ttk.Button(self, text="Voltar", command=self.destroy)
        btn_back.pack(fill=tk.X, padx=15, pady=5)
        
    def cancel(self):
        self.create_window.destroy()

    def read(self, codigo_arte=None):
        # abrir tela de leitura
        print("Abrir tela de leitura")
        VisualizeArtScr(self, codigo_arte)
        pass

    def update(self):
        # abrir tela de atualização
        UpdateArtScr(self.arts.get(self.arts.curselection())[0], self)
        pass

    def delete(self):
        # abrir tela de deleção
        crud.delete_record("ObraDeArte", "Codigo", str(self.arts.get(self.arts.curselection())[0]))
        pass

    def destroy(self):
        self.master.deiconify()
        super().destroy()
    
    def refresh(self):
        self.destroy()
        self.__init__()


class VisualizeArtScr(tk.Toplevel):
    def __init__(self, master=None, codigo=None):
        super().__init__(master=master)
        self.codigo = codigo
        self.initUI()
        self.master.iconify()
    
    def initUI(self):
        self.geometry("1200x600")
        style = ttk.Style(self)
        style.theme_use("clam")
        self.title("Visualizar Obra de Arte")

        # Frames 1 e 2
        self.frame = tk.Frame(self)
        self.frame.pack(fill=tk.BOTH, expand=True)

        # frame2 -> right side of frame
        self.frame2 = tk.Frame(self.frame)
        self.frame2.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Selecionar obra de arte no banco
        art = crud.select_record("ObraDeArte", "Codigo", str(self.codigo))

        # Listar informações da obra de arte uma por linha
        lbl_arts = ttk.Label(self.frame, text="Informações da Obra de Arte")
        lbl_arts.pack(fill=tk.X, padx=15, pady=5)

        # read events from database
        img = art[-1]
        art = art[:-1]
        
        labels = ["Codigo", "Autor", "Dono", "Ala", "Local de Criacao", "Data de Inicio", "Data de Conclusao", "Material", "Nome", "Movimento Artistico"]

        # Carregar nome do Dono
        nome_dono = crud.select_record("DonoArte", "Codigo", str(art[0]))[2]
        
        # Carregar nome da Ala
        nome_ala = crud.select_record("Ala", "Codigo", str(art[1]))[1]

        # Carregar autor
        codigo_autor = crud.select_record("Autoria", "CodigoObra", str(art[0]))[1]
        nome_autor = crud.select_record("Autor", "Codigo", str(codigo_autor))[1]

        art = list(art)
        art.insert(1, codigo_autor)

        # self.frame = tk.Frame(self)
        # self.frame.pack(fill=tk.X, padx=15, pady=5)
        i = 0
        for item in art:
            if i == 5 or i == 6:
                # Exibir data no formato dd/mm/aaaa
                item = item.strftime("%d/%m/%Y")
                item = labels[i] + ": " + str(item)
            elif i == 2:
                item = labels[i] + ": " + nome_dono
            elif i == 3:
                item = labels[i] + ": " + nome_ala
            elif i == 1:
                item = labels[i] + ": " + nome_autor
            else:
                item = labels[i] + ": " + str(item)
            lbl = ttk.Label(self.frame, text=item)
            lbl.pack(fill=tk.X, padx=15, pady=5)
            i += 1

        # Salvar a imagem do banco
        with open("./img/temp/temp.jpg", "wb") as f:
            f.write(img)

        # reescalar imagem e exibir
        img = PIL.Image.open("./img/temp/temp.jpg")
        img = img.resize((img.width//3, img.height//3), PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(img)

        # Exibir imagem
        lbl_img = ttk.Label(self.frame2, image=img, anchor=tk.CENTER)
        lbl_img.image = img
        lbl_img.pack(fill=tk.X, padx=15, pady=5)

        # Botao para abrir a tela do autor
        btn_autor = ttk.Button(self.frame, text="Autor", command=lambda:VisualizeAutorScr(self, art[1]))
        btn_autor.pack(fill=tk.X, padx=15, pady=5)

        # Botao para abrir tela de dono
        btn_dono = ttk.Button(self.frame, text="Dono", command=lambda:VisualizeDonoScr(self, art[1]))
        btn_dono.pack(fill=tk.X, padx=15, pady=5)

        # Botão de voltar
        btn_back = ttk.Button(self.frame, text="Voltar", command=self.voltar)
        btn_back.pack(fill=tk.X, padx=15, pady=5)

    def voltar(self):
        self.master.deiconify()
        self.destroy()

class CreateArtScr(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.img = "Nenhuma imagem selecionada"
        self.initUI()
        self.master.iconify()

    def initUI(self):
        self.geometry("800x600")
        style = ttk.Style(self)
        style.theme_use("clam")
        self.title("Criar")

        # Create inputs:
        lbl_codigo = ttk.Label(self, text="Codigo")
        lbl_codigo.pack(fill=tk.X, padx=15, pady=5)
        self.codigo = ttk.Entry(self)
        self.codigo.pack(fill=tk.X, padx=15, pady=5)

        lbl_dono = ttk.Label(self, text="Codigo Dono")
        lbl_dono.pack(fill=tk.X, padx=15, pady=5)
        self.dono = ttk.Entry(self)
        self.dono.pack(fill=tk.X, padx=15, pady=5)

        lbl_ala = ttk.Label(self, text="Codigo Ala")
        lbl_ala.pack(fill=tk.X, padx=15, pady=5)
        self.ala = ttk.Entry(self)
        self.ala.pack(fill=tk.X, padx=15, pady=5)

        lbl_local = ttk.Label(self, text="Local de Criacao")
        lbl_local.pack(fill=tk.X, padx=15, pady=5)
        self.local = ttk.Entry(self)
        self.local.pack(fill=tk.X, padx=15, pady=5)

        lbl_data_inicio = ttk.Label(self, text="Data de Inicio")
        lbl_data_inicio.pack(fill=tk.X, padx=15, pady=5)
        self.data_inicio = ttk.Entry(self)
        self.data_inicio.pack(fill=tk.X, padx=15, pady=5)

        lbl_data_conclusao = ttk.Label(self, text="Data de Conclusao")
        lbl_data_conclusao.pack(fill=tk.X, padx=15, pady=5)
        self.data_conclusao = ttk.Entry(self)
        self.data_conclusao.pack(fill=tk.X, padx=15, pady=5)

        lbl_material = ttk.Label(self, text="Material")
        lbl_material.pack(fill=tk.X, padx=15, pady=5)
        self.material = ttk.Entry(self)
        self.material.pack(fill=tk.X, padx=15, pady=5)

        lbl_nome = ttk.Label(self, text="Nome")
        lbl_nome.pack(fill=tk.X, padx=15, pady=5)
        self.nome = ttk.Entry(self)
        self.nome.pack(fill=tk.X, padx=15, pady=5)

        lbl_movimento = ttk.Label(self, text="Movimento Artistico")
        lbl_movimento.pack(fill=tk.X, padx=15, pady=5)
        self.movimento = ttk.Entry(self)
        self.movimento.pack(fill=tk.X, padx=15, pady=5)

        # Image input
        lbl_img = ttk.Label(self, text="Imagem")
        lbl_img.pack(fill=tk.X, padx=15, pady=5)

        btn_add_file = ttk.Button(
            self,
            text="Adicionar arquivo",
            command=lambda: self.add_file(),
        )
        btn_add_file.pack(padx=15, pady=5)
        # show self.img
        self.lbl_img = ttk.Label(self, text=self.img)
        self.lbl_img.pack(fill=tk.X, padx=15, pady=5)


        # create a button to confirm the creation
        btn_confirm = ttk.Button(self, text="Confirmar", command=lambda:self.confirm())
        btn_confirm.pack(fill=tk.X, padx=15, pady=5)

        # create a button to cancel the creation
        btn_cancel = ttk.Button(self, text="Cancelar", command=lambda:self.cancel())
        btn_cancel.pack(fill=tk.X, padx=15, pady=5)

    def add_file(self):
        file_path = askopenfiles(
            mode="r",
            filetypes=[
                ("PNG Files", "*png"),
                ("JPEG Files", "*jpg"),
            ],
        )
        if file_path is not None:
            for file in file_path:
                self.img = file.name
                print(self.img)

    def confirm(self):
        try:
            codigo = self.codigo.get()
            dono = self.dono.get()
            ala = self.ala.get()
            local = self.local.get()
            data_inicio = self.data_inicio.get()
            data_inicio = datetime.strptime(data_inicio, "%d/%m/%Y")
            data_conclusao = self.data_conclusao.get()
            data_conclusao = datetime.strptime(data_conclusao, "%d/%m/%Y")
            material = self.material.get()
            nome = self.nome.get()
            movimento = self.movimento.get()
            if self.img == "Nenhuma imagem selecionada":
                raise Exception("Nenhuma imagem selecionada")
            img = self.img
            img = open(img, "rb")
            img_bytes = img.read()
            img.close()
            crud.insert("ObraDeArte", codigo, dono, ala, local, data_inicio, data_conclusao, material, nome, movimento, img_bytes)
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

class UpdateArtScr(tk.Toplevel):
    def __init__(self, codigo_arte=None, master=None):
        super().__init__(master=master)
        self.img = "Nenhuma imagem selecionada"
        self.codigo_art = codigo_arte
        self.initUI()
        self.master.iconify()

    def initUI(self):
        self.geometry("800x600")
        style = ttk.Style(self)
        style.theme_use("clam")
        self.title("Criar")

        # Create inputs:
        lbl_table = ttk.Label(self, text="Insira o dado que quer alterar")
        lbl_table.pack(fill=tk.X, padx=15, pady=5)
        self.table = ttk.Entry(self)
        self.table.pack(fill=tk.X, padx=15, pady=5)

        lbl_data = ttk.Label(self, text="Insira o novo valor")
        lbl_data.pack(fill=tk.X, padx=15, pady=5)
        self.data = ttk.Entry(self)
        self.data.pack(fill=tk.X, padx=15, pady=5)

        btn_confirm = ttk.Button(self, text="Confirmar", command=lambda:self.confirm())
        btn_confirm.pack(fill=tk.X, padx=15, pady=5)

        btn_cancel = ttk.Button(self, text="Cancelar", command=lambda:self.cancel())
        btn_cancel.pack(fill=tk.X, padx=15, pady=5)

    def confirm(self):
        try:
            table = self.table.get()
            table.lower().capitalize()
            data = self.data.get()

            crud.update_record("ObraDeArte", table, data, "Codigo", self.codigo_art)
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