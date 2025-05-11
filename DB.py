import json
import mysql.connector
import logging

# Configura log apenas para arquivo (erros e exceções)
logging.basicConfig(
    filename='Logs.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class Database:
    # Estabelece uma conexão com o banco de dados "DriveDocuments"
    @staticmethod
    def connection():
        try:
            with open('properties.json', 'r') as f:
                credentials = json.load(f)
                db_user = credentials["db_user"]
                db_pwd = credentials["db_pwd"]

            mydb = mysql.connector.connect(
                host="localhost",
                user=db_user,
                password=db_pwd,
                database="DriveDocuments"
            )
            return mydb

        except FileNotFoundError:
            logging.error('Arquivo properties.json não encontrado.')
            raise
        except KeyError as e:
            logging.error(f'Chave ausente no properties.json: {e}')
            raise
        except mysql.connector.Error as err:
            logging.error(f'Erro de conexão com o banco de dados: {err}')
            raise
        except Exception as e:
            logging.error(f'Erro inesperado: {e}')
            raise

    # Cria o banco de dados "DriveDocuments" caso não exista
    @staticmethod
    def createDatabase():
        try:
            with open('properties.json', 'r') as f:
                credentials = json.load(f)
                db_user = credentials["db_user"]
                db_pwd = credentials["db_pwd"]

            mydb = mysql.connector.connect(
                host="localhost",
                user=db_user,
                password=db_pwd
            )
            mycursor = mydb.cursor()
            mycursor.execute("CREATE DATABASE IF NOT EXISTS DriveDocuments")

        except FileNotFoundError:
            logging.error('Arquivo properties.json não encontrado.')
            raise
        except KeyError as e:
            logging.error(f'Chave ausente no properties.json: {e}')
            raise
        except mysql.connector.Error as err:
            logging.error(f'Erro ao criar o banco de dados: {err}')
            raise
        except Exception as e:
            logging.error(f'Erro inesperado: {e}')
            raise

    # Cria a tabela 'files' para armazenar arquivos, se não existir
    @staticmethod
    def createTableFiles():
        try:
            mydb = Database.connection()
            mycursor = mydb.cursor()

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

        except mysql.connector.Error as err:
            logging.error(f'Erro ao criar a tabela files: {err}')
            raise
        except Exception as e:
            logging.error(f'Erro inesperado: {e}')
            raise

    # Cria a tabela 'logFiles' para armazenar logs de arquivos, se não existir
    @staticmethod
    def createTableFileLogs():
        try:
            mydb = Database.connection()
            mycursor = mydb.cursor()

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

        except mysql.connector.Error as err:
            logging.error(f'Erro ao criar a tabela logFiles: {err}')
            raise
        except Exception as e:
            logging.error(f'Erro inesperado: {e}')
            raise

    # Insere um novo arquivo na tabela 'files' (se não existir ainda)
    @staticmethod
    def insertData(file):
        try:
            print(f'\n📄 Arquivo encontrado: {file.name}')
            print(f'{(file.id, file.name, file.mimeType, file.owners, file.modifiedTime, str(file.shared))}')

            if Database.selectById(file.id, 'files') is False:
                mydb = Database.connection()
                mycursor = mydb.cursor()

                sql = "INSERT INTO files (id, name, extension, owner, lastModify, visibility) VALUES (%s, %s, %s, %s, %s, %s)"
                val = (file.id, file.name, file.mimeType, file.owners, file.modifiedTime, str(file.shared))
                mycursor.execute(sql, val)
                mydb.commit()

                print(f'✅ O arquivo "{file.name}" foi gravado na base de dados.\n')
            else:
                print(f'ℹ️ O arquivo "{file.name}" já está salvo na base de dados.\n')

        except mysql.connector.Error as err:
            logging.error(f'Erro ao inserir o arquivo "{file.name}": {err}')
            raise
        except Exception as e:
            logging.error(f'Erro inesperado ao inserir o arquivo "{file.name}": {e}')
            raise

    # Busca e imprime todos os registros da tabela 'files'
    @staticmethod
    def selectAll():
        try:
            mydb = Database.connection()
            mycursor = mydb.cursor()

            mycursor.execute("SELECT * FROM files")
            myresult = mycursor.fetchall()

            for result in myresult:
                print(result)

        except mysql.connector.Error as err:
            logging.error(f'Erro ao selecionar todos os registros: {err}')
            raise
        except Exception as e:
            logging.error(f'Erro inesperado: {e}')
            raise

    # Verifica se existe um registro pelo ID em uma tabela especificada
    @staticmethod
    def selectById(fileId, table):
        try:
            mydb = Database.connection()
            mycursor = mydb.cursor()

            query = f"SELECT * FROM {table} WHERE id = %s"
            mycursor.execute(query, (fileId,))
            result = mycursor.fetchone()

            return result is not None

        except mysql.connector.Error as err:
            logging.error(f'Erro ao buscar ID "{fileId}" na tabela "{table}": {err}')
            raise
        except Exception as e:
            logging.error(f'Erro inesperado ao buscar ID "{fileId}": {e}')
            raise

    # Insere um novo log na tabela 'logFiles' (se ainda não existir)
    @staticmethod
    def insertDataLog(file):
        try:
            mydb = Database.connection()
            mycursor = mydb.cursor()

            if Database.selectById(file.id, 'logFiles') is False:
                sql = "INSERT INTO logFiles (id, name, visibility, owner) VALUES (%s, %s, %s, %s)"
                val = (file.id, file.name, file.shared, file.owners)
                mycursor.execute(sql, val)
                mydb.commit()

                print(f'✅ Log do arquivo {file.name} inserido na base de dados logFiles.')
            else:
                print(f'⚠️  O log do arquivo {file.name} já existe na base de dados.')

        except mysql.connector.Error as err:
            logging.error(f'Erro ao inserir log do arquivo "{file.name}": {err}')
            raise
        except Exception as e:
            logging.error(f'Erro inesperado ao inserir log do arquivo "{file.name}": {e}')
            raise

    # Atualiza a visibilidade de um arquivo para 'False' na tabela 'files'
    @staticmethod
    def fileUpdate(fileId):
        try:
            mydb = Database.connection()
            mycursor = mydb.cursor()

            sql = f"UPDATE files SET visibility='False' WHERE id='{fileId}'"
            mycursor.execute(sql)
            mydb.commit()

        except mysql.connector.Error as err:
            logging.error(f'Erro ao atualizar visibilidade do arquivo ID "{fileId}": {err}')
            raise
        except Exception as e:
            logging.error(f'Erro inesperado ao atualizar visibilidade do arquivo ID "{fileId}": {e}')
            raise
