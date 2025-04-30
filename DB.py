import json

import mysql.connector

class Database:

    @staticmethod
    def connection():

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

    @staticmethod
    def createDatabase():
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

    @staticmethod
    def createTableFiles():
        mydb = Database.connection()
        mycursor = mydb.cursor()

        sql = "create table if not exists files(id varchar(150) not null,name varchar(260) not null,extension " \
              "varchar(200) not null," \
              "owner varchar(300) not null, lastModify varchar(200) not null,visibility enum('True', 'False')," \
              "primary key(id));"

        mycursor.execute(sql)

    @staticmethod
    def createTableFileLogs():
        mydb = Database.connection()
        mycursor = mydb.cursor()

        sql = "create table if not exists logFiles(id varchar(100) not null,name varchar(255) not null,visibility " \
              "enum('True', " \
              "'False'),owner varchar(200) not null,primary key(id)); "

        mycursor.execute(sql)

        # Função para inserir os dados na base de dados

    @staticmethod
    def insertData(file):
        # print(file)

        print(file.name)
        if Database.selectById(file.id, 'files') is False:

            mydb = Database.connection()
            mycursor = mydb.cursor()

            sql = "INSERT INTO files (id, name, extension, owner, lastModify, visibility) " \
                  "VALUES (%s, %s, %s, %s, %s, %s)"
            val = (file.id, file.name, file.mimeType, file.owners, file.modifiedTime, str(file.shared))
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
            print(f'O arquivo {file.name} foi gravado na base de dados!')
            print('-=' * 100)
        else:
            print('-=' * 50)
            print(f'O item {file.name} já está salvo na base de dados!')
            print('-=' * 50)

    @staticmethod
    def selectAll():
        mydb = Database.connection()
        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM files")
        myresult = mycursor.fetchall()

        for result in myresult:
            print(result)

    @staticmethod
    def selectById(fileId, table):
        mydb = Database.connection()
        mycursor = mydb.cursor()

        mycursor.execute(f"SELECT * FROM {table} WHERE id = '{fileId}'")

        result = mycursor.fetchone()

        print(result)
        if result is None:
            return False
        else:
            return True

    @staticmethod
    def insertDataLog(file):
        print(f'Inserindo na base de dados logFiles')
        mydb = Database.connection()
        mycursor = mydb.cursor()

        if Database.selectById(file.id, 'logFiles') is False:
            sql = "insert into logFiles (id, name, visibility, owner) VALUES (%s, %s, %s, %s)"
            val = (file.id, file.name, file.shared, file.owners)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "Data inserido na base de dados logFiles!")
            print('-=' * 100)
        else:
            print("Arquivo já existe na base!")

    @staticmethod
    def fileUpdate(fileId):
        mydb = Database.connection()
        mycursor = mydb.cursor()

        sql = f"UPDATE files SET visibility='False' WHERE id='{fileId}'"
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")