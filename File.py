# Classe que representa um arquivo (como um arquivo do Google Drive)
class File():
    # Construtor da classe — cria um objeto File com os atributos do arquivo
    def __init__(self, id, name, owners, shared, modifiedTime, mimeType):
        self.id = id
        self.name = name
        self.owners = owners
        # Visibilidade do arquivo (se está compartilhado ou não — True ou False)
        self.shared = shared
        self.modifiedTime = modifiedTime
        self.mimeType = mimeType
