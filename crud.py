from database import mycursor, mydb
from datetime import datetime

# CREATE:

# add a new artist to the database -> Codigo, Pais, Nome, TipoDono:boolean
# TipoDono = 0 -> Pessoa Fisica
# TipoDono = 1 -> Pessoa Juridica
def create_dono_arte(codigo, pais, nome, tipoDono):
    sql = "INSERT INTO DonoArte(Codigo, Pais, Nome, TipoDono) VALUES (%s, %s, %s, %s)"
    val = (codigo, pais, nome, tipoDono)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Owner record inserted.")

# add a new section to the database -> Codigo, Nome, Andar, Tema
def create_ala(Codigo, Nome, Andar, Tema):
    sql = "INSERT INTO Ala(Codigo, Nome, Andar, Tema) VALUES (%s, %s, %s, %s)"
    val = (Codigo, Nome, Andar, Tema)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Section record inserted.")

# add a new art piece to the database -> Codigo, CodigoDono, CodigoAla, LocalCriacao, DataInicio, DataConclusao, Material, Nome, MovArtistico, Imagem
def create_arte(Codigo, CodigoDono, CodigoAla, LocalCriacao, DataInicio, DataConclusao, Material, Nome, MovArtistico, Imagem):
    sql = "INSERT INTO ObraDeArte(Codigo, CodigoDono, CodigoAla, LocalCriacao, DataInicio, DataConclusao, Material, Nome, MovArtistico, Imagem) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (Codigo, CodigoDono, CodigoAla, LocalCriacao, DataInicio, DataConclusao, Material, Nome, MovArtistico, Imagem)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Art record inserted.")

# add a new artist to the database -> Codigo, Nome, DataNascimento, DataMorte, PaisOrigem
def create_autor(Codigo, Nome, DataNascimento, DataMorte, PaisOrigem):
    sql = "INSERT INTO Autor(Codigo, Nome, DataNascimento, DataMorte, PaisOrigem) VALUES (%s, %s, %s, %s, %s)"
    val = (Codigo, Nome, DataNascimento, DataMorte, PaisOrigem)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Author record inserted.")

# add a new event to the database -> Nome, CodigoAla, DataInicio, DataFim, Descricao, Instituicao
def create_evento(Nome, CodigoAla, DataInicio, DataFim, Descricao, Instituicao):
    sql = "INSERT INTO Evento(Nome, CodigoAla, DataInicio, DataFim, Descricao, Instituicao) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (Nome, CodigoAla, DataInicio, DataFim, Descricao, Instituicao)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Event record inserted.")

# add a new Integrante to the database -> Codigo, Nome, DataNascimento, Funcao
def create_integrante_evento(Codigo, Nome, DataNascimento, Funcao):
    sql = "INSERT INTO IntegranteEvento(Codigo, Nome, DataNascimento, Funcao) VALUES (%s, %s, %s, %s)"
    val = (Codigo, Nome, DataNascimento, Funcao)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Event member record inserted.")

# add a new visitor to the database -> CPF, Nome, Nacionalidade, TipoEntrada
def create_visitante(CPF, Nome, Nacionalidade, TipoEntrada):
    sql = "INSERT INTO Visitante(CPF, Nome, Nacionalidade, TipoEntrada) VALUES (%s, %s, %s, %s)"
    val = (CPF, Nome, Nacionalidade, TipoEntrada)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Visitor record inserted.")

# add a new employee to the database -> Matricula, CPF, Nome, DataNascimento, DataContratacao, Funcao, Endereco
def create_funcionario(Matricula, CPF, Nome, DataNascimento, DataContratacao, Funcao, Endereco):
    sql = "INSERT INTO Funcionario(Matricula, CPF, Nome, DataNascimento, DataContratacao, Funcao, Endereco) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (Matricula, CPF, Nome, DataNascimento, DataContratacao, Funcao, Endereco)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Employee record inserted.")

# add a new lost_item to the database -> Nome, Descricao, DataEncontrado, DataDevolucao, StatusItem, CodigoVisitante, CodigoFuncionario, CodigoAla
def create_item_perdido(Nome, Descricao, DataEncontrado, DataDevolucao, StatusItem, CodigoVisitante, CodigoFuncionario, CodigoAla):
    sql = "INSERT INTO ItemPerdido(Nome, Descricao, DataEncontrado, DataDevolucao, StatusItem, CodigoVisitante, CodigoFuncionario, CodigoAla) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (Nome, Descricao, DataEncontrado, DataDevolucao, StatusItem, CodigoVisitante, CodigoFuncionario, CodigoAla)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Lost item record inserted.")

# add a new DataVisita to the database -> Codigo, DataVisita, CodigoVisitante
def create_data_visita(Codigo, DataVisita, CodigoVisitante):
    sql = "INSERT INTO DataVisita(Codigo, DataVisita, CodigoVisitante) VALUES (%s, %s, %s)"
    val = (Codigo, DataVisita, CodigoVisitante)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Visit date record inserted.")

# add a new Trabalha to the database -> CodigoFuncionario, CodigoAla
def create_trabalha(CodigoFuncionario, CodigoAla):
    sql = "INSERT INTO Trabalha(CodigoFuncionario, CodigoAla) VALUES (%s, %s)"
    val = (CodigoFuncionario, CodigoAla)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Works record inserted.")

# add a new Participa to the database -> CodigoIntegrante, NomeEvento
def create_participa(CodigoIntegrante, NomeEvento):
    sql = "INSERT INTO Participa(CodigoIntegrante, NomeEvento) VALUES (%s, %s)"
    val = (CodigoIntegrante, NomeEvento)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Participates record inserted.")

# add a new Autoria to the database -> CodigoObra, CodigoAutor
def create_autoria(CodigoObra, CodigoAutor):
    sql = "INSERT INTO Autoria(CodigoObra, CodigoAutor) VALUES (%s, %s)"
    val = (CodigoObra, CodigoAutor)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Authorship record inserted.")

# add a record to the database -> multiple args
def create_record(table, *args):
    if table == "Dono":
        create_dono_arte(*args)
    elif table == "Ala":
        create_ala(*args)
    elif table == "Obra":
        create_arte(*args)
    elif table == "Autor":
        create_autor(*args)
    elif table == "Evento":
        create_evento(*args)
    elif table == "IntegranteEvento":
        create_integrante_evento(*args)
    elif table == "Visitante":
        create_visitante(*args)
    elif table == "Funcionario":
        create_funcionario(*args)
    elif table == "ItemPerdido":
        create_item_perdido(*args)
    elif table == "DataVisita":
        create_data_visita(*args)
    elif table == "Trabalha":
        create_trabalha(*args)
    elif table == "Participa":
        create_participa(*args)
    elif table == "Autoria":
        create_autoria(*args)
    else:
        print("Invalid table name.")

# Delete a record from the database
def delete_record(table, column, value):
    sql = "DELETE FROM " + table + " WHERE " + column + " = " + value
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")

# Update a record from the database
def update_record(table, column, value, column2, value2):
    sql = "UPDATE " + table + " SET " + column + " = " + value + " WHERE " + column2 + " = " + value2
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")

# Select a record from the database
def select_record(table, column, value):
    sql = "SELECT * FROM " + table + " WHERE " + column + " = " + value
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

# Select all records from the database
def select_all(table):
    sql = "SELECT * FROM " + table
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

if __name__ == "__main__":
    create_dono_arte(1, "Brasil", "João", False)
    create_ala(1, "Arte", 1, "Arte")
    create_arte(1, 1, 1, "Portugal", "2019-01-01", "2019-01-01", "Madeira", "Madeira", "Madeira", "Madeira")
    create_arte(2, 1, 1, "Portugal", "2019-01-01", "2019-01-01", "Madeira", "Madeira", "Madeira", "Madeira")

    create_autor(1, "João", "2019-01-01", "2019-01-01", "Brasil")

    create_evento("Evento", 1, "2019-01-01", "2019-01-01", "Evento", "Evento")
    create_integrante_evento(1, "João", "2019-01-01", "Evento")

    create_visitante(1, "João", "Brasil", 1)
    create_funcionario(1, 1, "João", "2019-01-01", "2019-01-01", "Evento", "Evento")
    create_item_perdido("Evento", "Evento", datetime(2019,1,1), "2019-01-01", "Evento", 1, 1, 1)

    create_data_visita(1, datetime(2019,1,1), 1)
    create_trabalha(1, 1)
    create_participa(1, "Evento")
    create_autoria(1, 1)

    # select_all("Autor")
    select_record("Autor", "Nome", "'João'")