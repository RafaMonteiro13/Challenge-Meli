import base64
from email.message import EmailMessage

from DriveAPI import api
from File import *
from DB import Database


def send_email(file):
    gmail = api('gmail')
    message = EmailMessage()

    msg = f'Prezado(a), por motivo de segurança, a visibilidade do arquivo "{file.name}" foi modificada para restrito.'
    message.set_content(msg)

    message['To'] = file.owners
    message['From'] = 'rafaelmonteirosouza123@gmail.com'
    message['Subject'] = f'Documento Drive - {file.name}'

    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    create_message = {'raw': encoded_message}
    user = 'rafaelmonteirosouza123@gmail.com'
    gmail.users().messages().send(userId=user, body=create_message).execute()
    print(f'📧 Email enviado para: {file.owners}')


def main():
    print('\n🚀 Iniciando aplicação...\n')
    service = api('drive')

    try:
        Database.createDatabase()
        Database.createTableFiles()
        Database.createTableFileLogs()
        print('✅ Banco de dados e tabelas criados (ou já existentes).')
    except Exception as error:
        print(f'❌ Erro no banco de dados: {error}')

    try:
        results = service.files().list(pageSize=1000, fields="nextPageToken, files(*)").execute()
        items = results.get('files', [])

        if not items:
            print('⚠️  Nenhum arquivo encontrado no Drive.')
            return

        print('\n📂 Lista de arquivos encontrados no Drive:')
        for item in items:
            file = File(
                item['id'],
                item['name'],
                item['owners'][0]['emailAddress'],
                item['shared'],
                item['modifiedTime'],
                item['mimeType']
            )
            Database.insertData(file)

        print('\n✅ Todos os arquivos foram processados e inseridos na base de dados.')

        print('\n🔍 Verificando arquivos compartilhados...\n')
        try:
            for item in items:
                fileHist = File(
                    item['id'],
                    item['name'],
                    item['owners'][0]['emailAddress'],
                    item['shared'],
                    None,
                    None
                )

                if fileHist.shared is True:
                    print(f'\n🔗 Arquivo compartilhado: {fileHist.name}')
                    print(f'{(fileHist.id, fileHist.name, str(fileHist.shared), fileHist.owners)}')

                    try:
                        print(f'\n📝 Inserindo log do arquivo: {fileHist.name}')
                        Database.insertDataLog(fileHist)

                        # Tenta deletar a permissão de compartilhamento
                        service.permissions().delete(
                            fileId=fileHist.id,
                            permissionId='anyoneWithLink'
                        ).execute()

                        send_email(fileHist)
                        Database.fileUpdate(fileHist.id)

                        print(f'🔒 Visibilidade do arquivo com ID {fileHist.id} atualizada para restrito.\n')

                    except Exception as e:
                        if 'Permission not found' in str(e):
                            print(f'⚠️ O arquivo "{fileHist.name}" já está restrito.\n')
                        else:
                            print(f'❌ Erro ao processar o arquivo "{fileHist.name}": {e}\n')

                else:
                    print(f'ℹ️ O arquivo "{fileHist.name}" já está restrito e não requer mais ação.\n')

        except Exception as error:
            print(f'❌ Erro ao buscar ou processar arquivos: {error}')

    except Exception as error:
        print(f'❌ Erro ao listar arquivos do Drive: {error}')


if __name__ == '__main__':
    main()
