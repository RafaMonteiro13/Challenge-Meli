import os.path

# Bibliotecas do Google para autenticação e API
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Escopos de acesso — permissões que a aplicação vai solicitar ao Google
SCOPES = [
    'https://www.googleapis.com/auth/drive',     # Permissão total para acessar o Google Drive
    'https://www.googleapis.com/auth/gmail.send' # Permissão para enviar e-mails pelo Gmail
]

# Função que autentica e retorna um serviço da API do Google (Drive ou Gmail)
def api(api):
    creds = None  # Inicializa o objeto de credenciais

    # Verifica se já existe um token salvo (credenciais já autorizadas anteriormente)
    if os.path.exists('token.json'):
        # Carrega as credenciais salvas do arquivo 'token.json'
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # Se não há credenciais ou as credenciais são inválidas (expiradas ou ausentes)
    if not creds or not creds.valid:
        # Se a credencial está expirada mas tem um token de atualização, faz refresh (renova a sessão)
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # Se não tem refresh token ou nenhuma credencial, inicia um fluxo de autenticação (OAuth2)
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES
            )
            # Abre um servidor local temporário para o usuário se autenticar no navegador
            creds = flow.run_local_server(port=0)

        # Salva as novas credenciais no arquivo 'token.json' para usos futuros (evita reautenticar sempre)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    # Constrói e retorna o serviço da API de acordo com o parâmetro 'api'
    if api == 'gmail':
        # Constrói o serviço Gmail API v1
        service = build('gmail', 'v1', credentials=creds)
        return service

    # Se não for 'gmail', por padrão retorna o serviço Google Drive API v3
    service = build('drive', 'v3', credentials=creds)
    return service