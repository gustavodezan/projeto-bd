from database import mycursor, mydb
from datetime import datetime

# CREATE:

# add a new artist to the database
# TipoDono = 0 -> Pessoa Fisica
# TipoDono = 1 -> Pessoa Juridica
def create_dono_arte(codigo, pais, nome, tipoDono):
    sql = "INSERT INTO DonoArte(Codigo, Pais, Nome, TipoDono) VALUES (%s, %s, %s, %s)"
    val = (codigo, pais, nome, tipoDono)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Owner record inserted.")

# add a new section to the database
def create_ala(Codigo, Nome, Andar, Tema):
    sql = "INSERT INTO Ala(Codigo, Nome, Andar, Tema) VALUES (%s, %s, %s, %s)"
    val = (Codigo, Nome, Andar, Tema)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Section record inserted.")

# add a new art piece to the database
def create_arte(Codigo, CodigoDono, CodigoAla, LocalCriacao, DataInicio, DataConclusao, Material, Nome, MovArtistico, Imagem):
    sql = "INSERT INTO ObraDeArte(Codigo, CodigoDono, CodigoAla, LocalCriacao, DataInicio, DataConclusao, Material, Nome, MovArtistico, Imagem) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (Codigo, CodigoDono, CodigoAla, LocalCriacao, DataInicio, DataConclusao, Material, Nome, MovArtistico, Imagem)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Art record inserted.")

# add a new artist to the database
def create_autor(Codigo, Nome, DataNascimento, DataMorte, PaisOrigem):
    sql = "INSERT INTO Autor(Codigo, Nome, DataNascimento, DataMorte, PaisOrigem) VALUES (%s, %s, %s, %s, %s)"
    val = (Codigo, Nome, DataNascimento, DataMorte, PaisOrigem)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Author record inserted.")

# add a new event to the database
def create_evento(Nome, CodigoAla, DataInicio, DataFim, Descricao, Instituicao):
    sql = "INSERT INTO Evento(Nome, CodigoAla, DataInicio, DataFim, Descricao, Instituicao) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (Nome, CodigoAla, DataInicio, DataFim, Descricao, Instituicao)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Event record inserted.")

# add a new Integrante to the database
def create_integrante_evento(Codigo, Nome, DataNascimento, Funcao):
    sql = "INSERT INTO IntegranteEvento(Codigo, Nome, DataNascimento, Funcao) VALUES (%s, %s, %s, %s)"
    val = (Codigo, Nome, DataNascimento, Funcao)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Event member record inserted.")

# add a new visitor to the database
def create_visitante(CPF, Nome, Nacionalidade, TipoEntrada):
    sql = "INSERT INTO Visitante(CPF, Nome, Nacionalidade, TipoEntrada) VALUES (%s, %s, %s, %s)"
    val = (CPF, Nome, Nacionalidade, TipoEntrada)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Visitor record inserted.")

# add a new employee to the database
def create_funcionario(Matricula, CPF, Nome, DataNascimento, DataContratacao, Funcao, Endereco):
    sql = "INSERT INTO Funcionario(Matricula, CPF, Nome, DataNascimento, DataContratacao, Funcao, Endereco) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (Matricula, CPF, Nome, DataNascimento, DataContratacao, Funcao, Endereco)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Employee record inserted.")

# add a new lost_item to the database
def create_item_perdido(Nome, Descricao, DataEncontrado, DataDevolucao, StatusItem, CodigoVisitante, CodigoFuncionario, CodigoAla):
    sql = "INSERT INTO ItemPerdido(Nome, Descricao, DataEncontrado, DataDevolucao, StatusItem, CodigoVisitante, CodigoFuncionario, CodigoAla) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (Nome, Descricao, DataEncontrado, DataDevolucao, StatusItem, CodigoVisitante, CodigoFuncionario, CodigoAla)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Lost item record inserted.")

# add a new DataVisita to the database
def create_data_visita(Codigo:int, DataVisita:datetime, CodigoVisitante:str):
    sql = "INSERT INTO DataVisita(Codigo, DataVisita, CodigoVisitante) VALUES (%s, %s, %s)"
    val = (Codigo, DataVisita, CodigoVisitante)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Visit date record inserted.")

# add a new Trabalha to the database
def create_trabalha(CodigoFuncionario:int, CodigoAla:int):
    sql = "INSERT INTO Trabalha(CodigoFuncionario, CodigoAla) VALUES (%s, %s)"
    val = (CodigoFuncionario, CodigoAla)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Works record inserted.")

# add a new Participa to the database
def create_participa(CodigoIntegrante:int, NomeEvento:str):
    sql = "INSERT INTO Participa(CodigoIntegrante, NomeEvento) VALUES (%s, %s)"
    val = (CodigoIntegrante, NomeEvento)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Participates record inserted.")

# add a new Autoria to the database
def create_autoria(CodigoObra:int, CodigoAutor:int):
    sql = "INSERT INTO Autoria(CodigoObra, CodigoAutor) VALUES (%s, %s)"
    val = (CodigoObra, CodigoAutor)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Authorship record inserted.")

# add a record to the database
def insert(table, *args):
    sql = "INSERT INTO " + table + " VALUES ("	
    for i in range(len(args)):
        sql += "%s"
        if i != len(args) - 1:
            sql += ", "
    sql += ")"
    val = args
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

# Delete a record from the database
def delete_record(table:str, column:str, value:str):
    sql = "DELETE FROM " + table + " WHERE " + column + " = " + value
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")

# Update a record from the database
def update_record(table:str, column:str, value:str, column2:str, value2:str):
    sql = "UPDATE " + table + " SET " + column + " = " + value + " WHERE " + column2 + " = " + value2
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")

# Select a record from the database
def select_record(table:str, column:str, value:str):
    sql = "SELECT * FROM " + table + " WHERE " + column + " = " + value
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult[0]

# Select all records from the database
def select_all(table:str):
    sql = "SELECT * FROM " + table
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult

def select_all_where(table:str, column:str, value:str):
    sql = "SELECT * FROM " + table + " WHERE " + column + " = " + value
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult

# Login
def verifica_login(user:int, password:str) -> list:
    sql = "SELECT * FROM Funcionario WHERE Matricula = " + user
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    if myresult[0][1] == password:
        return myresult
    return []

if __name__ == "__main__":
    create_dono_arte(1, "Brasil", "João", False)
    create_ala(1, "Arte", 1, "Arte")
    img = open("./img/pic1.jpg", "rb")
    create_arte(1, 1, 1, "Portugal", "2019-01-01", "2019-01-01", "Madeira", "Madeira", "Madeira", img.read())
    create_arte(2, 1, 1, "Portugal", "2019-01-01", "2019-01-01", "Madeira", "Madeira", "Madeira", img.read())

    create_autor(1, "João", "2019-01-01", "2019-01-01", "Brasil")

    create_evento("Evento", 1, "2019-01-01", "2019-01-01", "Evento", "Evento")
    create_integrante_evento(1, "João", "2019-01-01", "Evento")

    create_visitante(1, "João", "Brasil", 1)
    create_funcionario(1, 1, "admin", datetime(2000,1,1), datetime.now(), "Evento", "Evento")
    create_item_perdido("Evento", "Evento", datetime(2019,1,1), "2019-01-01", "Evento", 1, 1, 1)

    create_data_visita(1, datetime(2019,1,1), 1)
    create_trabalha(1, 1)
    create_participa(1, "Evento")
    create_autoria(1, 1)

    # select_all("Autor")
    select_record("Autor", "Nome", "'João'")

    # select_all("Obra")
    arte = select_record("ObraDeArte", "Nome", "'Madeira'")