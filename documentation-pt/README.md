# Challenge MeLi
Desafio Docs no Drive Público

Desenvolver uma aplicação para inventariar em um Banco de Dados todos os arquivos pertencentes à unidade de Drive de um usuário. 
O banco de dados deve ser criado a partir da aplicação, podendo ser utilizado qualquer motor (por exemplo, MySQL ou Redis). Este banco deve armazenar o nome do arquivo, a extensão, o proprietário do arquivo, a visibilidade (público ou privado) e a data da última modificação.
Caso sejam encontrados arquivos configurados como públicos e que possam ser acessados por qualquer pessoa, a configuração deve ser modificada para definir o arquivo como privado e enviar um e-mail ao proprietário notificando a alteração realizada.
A aplicação deve ter a lógica necessária para salvar no banco de dados apenas os arquivos que não foram armazenados em uma execução anterior ou para atualizar a data de modificação ou qualquer outro dado, se necessário. Além disso, deve manter um inventário histórico de todos os arquivos que em algum momento foram públicos.
Esta aplicação deve ser desenvolvida em Python e deve ter testes que verifiquem seu bom funcionamento.

Bônus:
 
* Aplicar boas práticas de programação.
* Documentação e bibliografia consultada.
* Tratamento seguro das credenciais utilizadas.
* Dockerizar a aplicação.

## Pré - Requisitos
Para executar o código, faça o download do código neste repositorio do GitHub: https://github.com/RafaMonteiro13/Challenge-Meli/

## Requisitos para executar o código:
- Python
- MySql
## Instalar as seguintes bibliotecas:
   * pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
   * pip install google-api-python-client
   * pip install mysql-connector-python

## Código fonte
### Base de dados
O arquivo DB.py cria as seguintes tabelas:
* Tabela files que tem as seguintes colunas:
  - id
  - name
  - extension
  - owner
  - lastModify
  - visibility
- Tabela que tem as seguintes colunas:
  - id
  - name
  - visibility
  - owner

O arquivo DB.py faz as seguintes operações:
- Conexão com a base de dados
- Inserir os arquivos na tabela files
- Inserir os arquivos que estão com públicos na tabela logFiles
- Consultar se o arquivo já está gravada na tabela files
- Consultar se o arquivo já está gravado na tabela logFiles
- Atualização dos arquivos que estão publicos na tabela files

### Arquivo DriveAPI
O arquivo DriveAPI.py contém a função "api()", que faz a conexão na API do Google Drive,
e gera um arquivo token.json que armazena os tokens de acesso. O arquivo é criado automaticamente
quando a autorização se completa pela primeira vez.

### Arquivo main
O arquivo main.py é onde acontece a lógica principal da aplicação, logo realiza as conexões nos bancos de dados e a
conexão na API do Google Drive. Lista todos os arquivos do Drive e valida se os arquivos já existem na base de dados, e
também valida se os arquivos são públicos ou privados. Após essas validações o programa modifica a visibilidade dos arquivos
publicos, manda o e-mail para o responsável do arquivo e atualiza as informações na base de dados.

## Bibliografia
- https://docs.python.org/
- https://developers.google.com/drive/api/quickstart/python
- https://developers.google.com/gmail/api/quickstart/python
- https://mailtrap.io/blog/send-emails-with-gmail-api/
- https://stackoverflow.com