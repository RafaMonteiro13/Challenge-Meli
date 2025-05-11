import os.path
import sys
import logging

# Configura log apenas para arquivo (erros e exceções)
logging.basicConfig(
    filename='Logs.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Bibliotecas do Google para autenticação e API
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.exceptions import GoogleAuthError

# Escopos de acesso — permissões que a aplicação vai solicitar ao Google
SCOPES = [
    'https://www.googleapis.com/auth/drive',     # Permissão total para acessar o Google Drive
    'https://www.googleapis.com/auth/gmail.send' # Permissão para enviar e-mails pelo Gmail
]

# Função que autentica e retorna um serviço da API do Google (Drive ou Gmail)
def api(api):
    creds = None  # Inicializa o objeto de credenciais

    try:
        # Verifica se já existe um token salvo (credenciais já autorizadas anteriormente)
        if os.path.exists('token.json'):
            try:
                # Carrega as credenciais salvas do arquivo 'token.json'
                creds = Credentials.from_authorized_user_file('token.json', SCOPES)
            except Exception as e:
                print(f"⚠️ Erro ao carregar o arquivo 'token.json': {e}")
                logging.error(f"Erro ao carregar o arquivo 'token.json': {e}")
                creds = None

        # Se não há credenciais ou as credenciais são inválidas (expiradas ou ausentes)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                try:
                    # Tenta renovar o token
                    creds.refresh(Request())
                except GoogleAuthError as e:
                    print(f"⚠️ Erro ao renovar o token de acesso: {e}")
                    logging.error(f"Erro ao renovar o token de acesso: {e}")
                    creds = None
            else:
                try:
                    # Se não tem refresh token ou nenhuma credencial, inicia um fluxo de autenticação (OAuth2)
                    flow = InstalledAppFlow.from_client_secrets_file(
                        'client_secret.json', SCOPES
                    )
                    # Abre um servidor local temporário para o usuário se autenticar no navegador
                    creds = flow.run_local_server(port=0)
                except FileNotFoundError:
                    print("❌ Arquivo 'client_secret.json' não encontrado. Verifique se o arquivo está no diretório correto.")
                    logging.error("Arquivo 'client_secret.json' não encontrado.")
                    sys.exit(1)
                except Exception as e:
                    print(f"❌ Erro ao realizar o fluxo de autenticação OAuth2: {e}")
                    logging.error(f"Erro ao realizar o fluxo de autenticação OAuth2: {e}")
                    sys.exit(1)

            # Salva as novas credenciais no arquivo 'token.json' para usos futuros (evita reautenticar sempre)
            try:
                with open('token.json', 'w') as token:
                    token.write(creds.to_json())
            except Exception as e:
                print(f"⚠️ Erro ao salvar o token no arquivo 'token.json': {e}")
                logging.error(f"Erro ao salvar o token no arquivo 'token.json': {e}")

        # Constrói e retorna o serviço da API de acordo com o parâmetro 'api'
        try:
            if api == 'gmail':
                # Constrói o serviço Gmail API v1
                service = build('gmail', 'v1', credentials=creds)
                return service
            else:
                # Por padrão retorna o serviço Google Drive API v3
                service = build('drive', 'v3', credentials=creds)
                return service
        except GoogleAuthError as e:
            print(f"❌ Erro ao construir o serviço da API ({api}): {e}")
            logging.error(f"Erro ao construir o serviço da API ({api}): {e}")
            sys.exit(1)

    except Exception as e:
        print(f"❌ Ocorreu um erro inesperado durante o processo de autenticação: {e}")
        logging.error(f"Ocorreu um erro inesperado durante o processo de autenticação: {e}")
        sys.exit(1)
