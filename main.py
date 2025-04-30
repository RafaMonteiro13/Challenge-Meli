import base64
from email.message import EmailMessage

from DriveAPI import api
from File import *
from DB import Database


# Press the green button in the gutter to run the script.
def send_email(file):
    # create gmail api client
    gmail = api('gmail')
    message = EmailMessage()

    msg = f'Prezado(a), por motivo de segurança, a visibilidade do arquivo "{file.name}" foi modificado para restrito.'
    message.set_content(msg)

    # headers
    message['To'] = file.owners
    message['From'] = 'rafaelmonteirosouza123@gmail.com'
    message['Subject'] = f'Documento Drive - {file.name}'

    # encoded message
    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    create_message = {
        'raw': encoded_message
    }
    user = 'rafaelmonteirosouza123@gmail.com'
    gmail.users().messages().send(userId=user, body=create_message).execute()
    print(f'Email enviado para: {file.owners}')


def main():
    print('------------ Start Application ------------')
    service = api('drive')

    try:
        Database.createDatabase()
        Database.createTableFiles()
        Database.createTableFileLogs()
    except Exception as error:
        print(f'Database error: {error}')

    try:
        results = service.files().list(
            pageSize=1000, fields="nextPageToken, files(*)").execute()
        items = results.get('files', [])

        if not items:
            print('No files found.')
            return
        print('File:')
        for item in items:
            file = File(item['id'], item['name'], item['owners'][0]['emailAddress'], item['shared'],
                        item['modifiedTime'],
                        item['mimeType'])
            Database.insertData(file)
        print('Arquivos inseridos na base de dados!')

        print('-=-=' * 100)
        for item in items:
            # id, name, owners, shared, modifiedTime, mimeType
            fileHist = File(item['id'], item['name'], item['owners'][0]['emailAddress'], item['shared'], None, None)
            if fileHist.shared is True:
                print(f'{fileHist.name} - shared: {fileHist.shared}')
                try:
                    print('-=-=' * 100)
                    Database.insertDataLog(fileHist)
                    # Tenta deletar a permissão de compartilhamento
                    service.permissions().delete(fileId=fileHist.id, permissionId='anyoneWithLink').execute()
                    send_email(fileHist)
                    Database.fileUpdate(fileHist.id)
                except Exception as e:
                    # Caso o erro seja "Permission not found" ou algo que indique que o arquivo já está restrito
                    if 'Permission not found' in str(e):
                        print(f'O arquivo "{fileHist.name}" já está restrito.')
                    else:
                        print(f'Erro ao tentar remover a permissão ou enviar e-mail para o arquivo "{fileHist.name}": {e}')
                print('-=-=' * 100)
            else:
                print(f'O arquivo "{fileHist.name}" já está restrito e não requer mais ação.')
    except Exception as error:
        print(f'Error {error}')



if __name__ == '__main__':
    main()
