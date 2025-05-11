import base64
import sys
from email.message import EmailMessage

from DriveAPI import api
from File import *
from DB import Database


# Função responsável por enviar um email para o dono do arquivo, informando que a visibilidade foi alterada
def send_email(file):
    try:
        # Conecta na API do Gmail (a função api('gmail') retorna o serviço da API Gmail)
        gmail = api('gmail')

        # Cria a mensagem de email
        message = EmailMessage()

        # Corpo do email explicando que a visibilidade do arquivo foi alterada
        msg = f'Prezado(a), por motivo de segurança, a visibilidade do arquivo "{file.name}" foi modificada para restrito.'
        message.set_content(msg)

        # Define o destinatário, remetente e assunto do email
        message['To'] = file.owners
        message['From'] = 'rafaelmonteirosouza123@gmail.com'
        message['Subject'] = f'Documento Drive - {file.name}'

        # Codifica a mensagem em base64 (formato exigido pela API do Gmail)
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

        # Prepara o corpo da requisição para a API do Gmail
        create_message = {'raw': encoded_message}
        user = 'rafaelmonteirosouza123@gmail.com'

        # Envia o email usando a API do Gmail
        gmail.users().messages().send(userId=user, body=create_message).execute()
        print(f'📧 Email enviado para: {file.owners}')

    except Exception as e:
        print(f'❌ Erro ao enviar o email para "{file.owners}": {e}')


# Função principal da aplicação — responsável por executar todo o fluxo
def main():
    print('\n🚀 Iniciando aplicação...\n')

    try:
        # Conecta na API do Google Drive (a função api('drive') retorna o serviço da API Drive)
        service = api('drive')
    except Exception as e:
        print(f'❌ Erro ao conectar à API do Google Drive: {e}')
        sys.exit(1)

    # Cria o banco de dados e as tabelas (se ainda não existirem)
    try:
        Database.createDatabase()
        Database.createTableFiles()
        Database.createTableFileLogs()
        print('✅ Banco de dados e tabelas criados (ou já existentes).')
    except Exception as error:
        print(f'❌ Erro ao criar banco de dados ou tabelas: {error}')
        sys.exit(1)

    # Tenta listar os arquivos do Google Drive
    try:
        results = service.files().list(pageSize=1000, fields="nextPageToken, files(*)").execute()
        items = results.get('files', [])

        # Se não houver arquivos
        if not items:
            print('⚠️ Nenhum arquivo encontrado no Drive.')
            return

        print('\n📂 Lista de arquivos encontrados no Drive:')

        # Para cada arquivo encontrado, cria um objeto File e insere na base de dados
        for item in items:
            try:
                file = File(
                    item['id'],
                    item['name'],
                    item['owners'][0]['emailAddress'],  # Pega o e-mail do proprietário
                    item['shared'],  # Se está compartilhado
                    item['modifiedTime'],  # Data de modificação
                    item['mimeType']  # Tipo MIME
                )
                Database.insertData(file)
            except KeyError as e:
                print(f'⚠️ Dados incompletos no arquivo {item.get("name", "desconhecido")}: campo ausente {e}')
            except Exception as e:
                print(f'❌ Erro ao processar o arquivo {item.get("name", "desconhecido")}: {e}')

        print('\n✅ Todos os arquivos foram processados e inseridos na base de dados.')

        # Verifica arquivos que estão compartilhados publicamente
        print('\n🔍 Verificando arquivos compartilhados...\n')
        for item in items:
            try:
                # Cria um objeto File apenas com os campos necessários para o log
                fileHist = File(
                    item['id'],
                    item['name'],
                    item['owners'][0]['emailAddress'],
                    item['shared'],
                    None,  # Não precisa da data de modificação nesse contexto
                    None  # Nem do mimeType
                )

                # Se o arquivo estiver compartilhado
                if fileHist.shared is True:
                    print(f'\n🔗 Arquivo compartilhado: {fileHist.name}')
                    print(f'{(fileHist.id, fileHist.name, str(fileHist.shared), fileHist.owners)}')

                    try:
                        # Insere o log do arquivo na tabela logFiles
                        print(f'\n📝 Inserindo log do arquivo: {fileHist.name}')
                        Database.insertDataLog(fileHist)

                        # Remove a permissão de "qualquer pessoa com o link"
                        service.permissions().delete(
                            fileId=fileHist.id,
                            permissionId='anyoneWithLink'
                        ).execute()

                        # Envia o email notificando o dono
                        send_email(fileHist)

                        # Atualiza a visibilidade do arquivo na base de dados para 'False'
                        Database.fileUpdate(fileHist.id)

                        print(f'🔒 Visibilidade do arquivo com ID {fileHist.id} atualizada para restrito.\n')

                    except Exception as e:
                        # Se a permissão já não existir, ignora o erro
                        if 'Permission not found' in str(e):
                            print(f'⚠️ O arquivo "{fileHist.name}" já está restrito.\n')
                        else:
                            print(f'❌ Erro ao processar o arquivo "{fileHist.name}": {e}\n')

                else:
                    # Caso o arquivo já esteja restrito
                    print(f'ℹ️ O arquivo "{fileHist.name}" já está restrito e não requer mais ação.\n')

            except KeyError as e:
                print(f'⚠️ Dados incompletos no arquivo {item.get("name", "desconhecido")}: campo ausente {e}')
            except Exception as e:
                print(f'❌ Erro ao verificar o arquivo {item.get("name", "desconhecido")}: {e}')

    except Exception as error:
        print(f'❌ Erro ao listar ou processar arquivos do Drive: {error}')
        sys.exit(1)


# Chama a função main()
if __name__ == '__main__':
    main()
