import json
import mysql.connector

class Database:
    # Estabelece uma conexão com o banco de dados "DriveDocuments"
    @staticmethod
    def connection():
        # Lê credenciais do arquivo 'properties.json'
        with open('properties.json', 'r') as f:
            credentials = json.load(f)
            db_user = credentials["db_user"]
            db_pwd = credentials["db_pwd"]

        # Conecta no banco "DriveDocuments"
        mydb = mysql.connector.connect(
            host="localhost",
            user=db_user,
            password=db_pwd,
            database="DriveDocuments"
        )
        return mydb

    # Cria o banco de dados "DriveDocuments" caso não exista
    @staticmethod
    def createDatabase():
        # Lê credenciais do arquivo 'properties.json'
        with open('properties.json', 'r') as f:
            credentials = json.load(f)
            db_user = credentials["db_user"]
            db_pwd = credentials["db_pwd"]

        # Conecta no MySQL (sem especificar banco) para criar o banco
        mydb = mysql.connector.connect(
            host="localhost",
            user=db_user,
            password=db_pwd
        )
        mycursor = mydb.cursor()

        # Cria o banco "DriveDocuments" se ainda não existir
        mycursor.execute("CREATE DATABASE IF NOT EXISTS DriveDocuments")

    # Cria a tabela 'files' para armazenar arquivos, se não existir
    @staticmethod
    def createTableFiles():
        mydb = Database.connection()
        mycursor = mydb.cursor()

        # Comando SQL para criar tabela 'files'
        sql = """
        CREATE TABLE IF NOT EXISTS files (
            id VARCHAR(150) NOT NULL,
            name VARCHAR(260) NOT NULL,
            extension VARCHAR(200) NOT NULL,
            owner VARCHAR(300) NOT NULL,
            lastModify VARCHAR(200) NOT NULL,
            visibility ENUM('True', 'False'),
            PRIMARY KEY(id)
        );
        """
        mycursor.execute(sql)

    # Cria a tabela 'logFiles' para armazenar logs de arquivos, se não existir
    @staticmethod
    def createTableFileLogs():
        mydb = Database.connection()
        mycursor = mydb.cursor()

        # Comando SQL para criar tabela 'logFiles'
        sql = """
        CREATE TABLE IF NOT EXISTS logFiles (
            id VARCHAR(100) NOT NULL,
            name VARCHAR(255) NOT NULL,
            visibility ENUM('True', 'False'),
            owner VARCHAR(200) NOT NULL,
            PRIMARY KEY(id)
        );
        """
        mycursor.execute(sql)

    # Insere um novo arquivo na tabela 'files' (se não existir ainda)
    @staticmethod
    def insertData(file):
        # Mostra informações do arquivo no console
        print(f'\n📄 Arquivo encontrado: {file.name}')
        print(f'{(file.id, file.name, file.mimeType, file.owners, file.modifiedTime, str(file.shared))}')

        # Verifica se o arquivo já existe na tabela 'files'
        if Database.selectById(file.id, 'files') is False:
            mydb = Database.connection()
            mycursor = mydb.cursor()

            # Comando SQL para inserir dados na tabela 'files'
            sql = "INSERT INTO files (id, name, extension, owner, lastModify, visibility) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (file.id, file.name, file.mimeType, file.owners, file.modifiedTime, str(file.shared))
            mycursor.execute(sql, val)
            mydb.commit()

            # Caso o registro já existe ele informa que já esta salvo na base de dados
            # Caso não, ele grava na base de dados

            print(f'✅ O arquivo "{file.name}" foi gravado na base de dados.\n')
        else:
            print(f'ℹ️ O arquivo "{file.name}" já está salvo na base de dados.\n')

    # Busca e imprime todos os registros da tabela 'files'
    @staticmethod
    def selectAll():
        mydb = Database.connection()
        mycursor = mydb.cursor()

        # Executa a consulta para selecionar tudo
        mycursor.execute("SELECT * FROM files")
        myresult = mycursor.fetchall()

        # Imprime cada registro encontrado
        for result in myresult:
            print(result)

    # Verifica se existe um registro pelo ID em uma tabela especificada
    @staticmethod
    def selectById(fileId, table):
        mydb = Database.connection()
        mycursor = mydb.cursor()

        # Executa a consulta filtrando pelo ID
        mycursor.execute(f"SELECT * FROM {table} WHERE id = '{fileId}'")
        result = mycursor.fetchone()

        # Retorna True se encontrou, False se não encontrou
        if result is None:
            return False
        else:
            return True

    # Insere um novo log na tabela 'logFiles' (se ainda não existir)
    @staticmethod
    def insertDataLog(file):
        mydb = Database.connection()
        mycursor = mydb.cursor()

        # Verifica se o log do arquivo já existe
        if Database.selectById(file.id, 'logFiles') is False:
            # Comando SQL para inserir no logFiles
            sql = "INSERT INTO logFiles (id, name, visibility, owner) VALUES (%s, %s, %s, %s)"
            val = (file.id, file.name, file.shared, file.owners)
            mycursor.execute(sql, val)
            mydb.commit()
            print(f'✅ Log do arquivo {file.name} inserido na base de dados logFiles.')
        else:
            print(f'⚠️  O log do arquivo {file.name} já existe na base de dados.')

    # Atualiza a visibilidade de um arquivo para 'False' na tabela 'files'
    @staticmethod
    def fileUpdate(fileId):
        mydb = Database.connection()
        mycursor = mydb.cursor()

        # Comando SQL para atualizar visibilidade do arquivo
        sql = f"UPDATE files SET visibility='False' WHERE id='{fileId}'"
        mycursor.execute(sql)
        mydb.commit()
