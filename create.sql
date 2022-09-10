CREATE DATABASE museu
USE museu;

CREATE TABLE DonoArte(Cogido INT NOT NULL, Pais VARCHAR(25), Nome VARCHAR(25), TipoDono BOOLEAN, PRIMARY KEY(Cogido));
CREATE TABLE Ala(Codigo INT NOT NULL, Nome CHAR(5), Andar INT, Tema VARCHAR(50), PRIMARY KEY(Codigo));
CREATE TABLE ObraDeArte(Codigo INT NOT NULL, CodigoDono INT, CodigoAla INT, LocalCriacao VARCHAR(25), DataInicio DATE, DataConclusao DATE, Material VARCHAR(30), Nome VARCHAR(80), MovArtistico VARCHAR(50), Imagem LONGBLOB, PRIMARY KEY(Codigo), FOREIGN KEY(CodigoDono) REFERENCES DonoArte(Codigo) ON DELETE CASCADE, FOREIGN KEY(CodigoAla) REFERENCES Ala(Codigo) ON DELETE CASCADE);

CREATE TABLE Autor(Codigo INT NOT NULL, Nome VARCHAR(80), DataNascimento DATE, DataMorte DATE, PaisOrigem VARCHAR(25), PRIMARY KEY(Codigo));

CREATE TABLE Evento(Nome VARCHAR(50) NOT NULL, CodigoAla INT NOT NULL, DataInicio DATE, DataFim DATE, Descricao VARCHAR(200), Instituicao VARCHAR(50), PRIMARY KEY(Nome), FOREIGN KEY(CodigoAla) REFERENCES Ala(Codigo));
CREATE TABLE IntegranteEvento(Codigo INT NOT NULL, Nome VARCHAR(50), DataNascimento DATE, Funcao VARCHAR(50), PRIMARY KEY(Codigo));

CREATE TABLE Visitante(CPF CHAR(11) NOT NULL, Nome VARCHAR(80), Nacionalidade VARCHAR(50), TipoEntrada INT, PRIMARY KEY(CPF));
CREATE TABLE Funcionario(Matricula INT NOT NULL, CPF CHAR(11), Nome VARCHAR(80), DataNascimento DATE, DataContratacao DATE, Funcao VARCHAR(20), Endereco VARCHAR(50), PRIMARY KEY(CPF));
CREATE TABLE ItemPerdido(Nome VARCHAR(30) NOT NULL, Descricao VARCHAR(200), DataEncontrado DATE, DataDevolucao DATE, StatusItem VARCHAR(50), CodigoVisitante INT, CodigoFuncionario INT, CodigoAla INT, PRIMARY KEY(Nome), FOREIGN KEY(CodigoAla) REFERENCES Ala(Codigo), FOREIGN KEY(CodigoVisitante) REFERENCES Visitante(Codigo), FOREIGN KEY(CodigoFuncionario) REFERENCES Funcionario(Codigo));

CREATE TABLE DataVisita(Codigo INT NOT NULL, DataVisita DATE, CodigoVisitante CHAR(11) NOT NULL, FOREIGN KEY(CodigoVisitante) REFERENCES Visitante(Codigo));
CREATE TABLE Trabalha(MatriculaFuncionario INT NOT NULL, CodigoAla INT NOT NULL, PRIMARY KEY(FOREIGN KEY(MatriculaFuncionario) REFERENCES Funcionario(Matricula), FOREIGN KEY(CodigoAla) REFERENCES Ala(Codigo)));
CREATE TABLE Participa(CodigoIntegrante INT NOT NULL, NomeEvento VARCHAR(50) NOT NULL, PRIMARY KEY(FOREIGN KEY(CodigoIntegrante) REFERENCES IntegranteEvento(Codigo), FOREIGN KEY(NomeEvento) REFERENCES Evento(Nome)));
CREATE TABLE Autoria(CodigoObra INT NOT NULL, CodigoAutor INT NOT NULL, PRIMARY KEY(FOREIGN KEY(CodigoObra) REFERENCES ObraDeArte(Codigo), FOREIGN KEY(CodigoAutor) REFERENCES Autor(Codigo)));
