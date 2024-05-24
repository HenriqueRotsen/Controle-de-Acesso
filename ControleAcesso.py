from dataclasses import dataclass
from Calculadora import calculadora
from Calculadora_Bhaskara import menu as calculadora_bhaskara
from Calculadora_fisica import menu as calculadora_fisica

# Variavel global de número de usuario
CONTADOR_ID = 0

@dataclass
class Usuarios:
    """Dataclass representativa de usuários do sistema. 

    Args:
        id (int): Id do usuário. Definido automaticametne pelo sistema
        nome (str): Nome real de usuário
        username (str): Nome de usuário mostrado no sistema
        email (str): Endereço de e-mail do usuário
        setor (str): Setor do usuário
        cargo (str): Cargo do usuário (comum ou administrador)
        nivel (int): Nível de acesso do usuário
        senha (int, optional): Senha de acesso do usuário ao sistema. Default é 123.
    """
    def __init__(self, id: int, nome: str, username: str, email: str, setor:str, cargo:str, nivel: int, senha=123):
        self.id = id
        self.nome = nome
        self.username = username
        self.email = email
        self.setor = setor
        self.cargo = cargo
        self.nivel = nivel
        self.senha = senha

@dataclass
class Funcionalidades:
    """Definição de funcionalidade do sistema 

    Args:
        id (int): _description_
        nome (str): _description_
        nivel (int): _description_
    """
    def __init__(self, id: int, nome: str, nivel: str):
        self.id = id
        self.nome = nome
        self.nivel = nivel


@dataclass
class FuncionalidadeUsuarios:
    """
    Classe para representar a associação de funcionalidades com usuários.

    Attributes:
        id (int): Identificador único da associação.
        idUsuario (int): Identificador do usuário.
        idFuncionalidade (int): Identificador da funcionalidade.
        liberado (bool): Indica se a funcionalidade está liberada para o usuário.
    """
    id: int
    idUsuario: int
    idFuncionalidade: int
    liberado: bool

    def __init__(self, id: int, idUsuario: int, idFuncionalidade: int, liberado: bool) -> None:
        """
        Inicializa a classe FuncionalidadeUsuarios com os parâmetros fornecidos.

        Args:
            id (int): Identificador único da associação.
            idUsuario (int): Identificador do usuário.
            idFuncionalidade (int): Identificador da funcionalidade.
            liberado (bool): Indica se a funcionalidade está liberada para o usuário.
        """
        self.id = id
        self.idUsuario = idUsuario
        self.idFuncionalidade = idFuncionalidade
        self.liberado = liberado


class SistemaGerenciamentoAcesso:
    """
    Classe para gerenciar o sistema de acesso de usuários e suas funcionalidades.

    Attributes:
        usuarios (list): Lista de usuários cadastrados.
        funcionalidades (list): Lista de funcionalidades disponíveis.
        funcionalidadeUsuarios (list): Lista de associações entre usuários e funcionalidades.
    """

    def __init__(self):
        """
        Inicializa a classe SistemaGerenciamentoAcesso com listas vazias para
        usuários, funcionalidades e associações de funcionalidades com usuários.
        """
        self.usuarios = []
        self.funcionalidades = []
        self.funcionalidadeUsuarios = []

    def verificarSenha(self, userName, senha):
        """
        Verifica se a senha fornecida corresponde ao usuário especificado.

        Args:
            userName (str): Nome de usuário.
            senha (str): Senha do usuário.

        Returns:
            tuple: Um par (bool, int) onde o booleano indica se a senha está correta
            e o inteiro é o ID do usuário, ou -1 se a senha estiver incorreta.
        """
        for user in self.usuarios:
            if user.username == userName and user.senha == int(senha):
                return (True, user.id)
        return (False, -1)

    def cadastrarUsuario(self, usuario):
        """
        Cadastra um novo usuário e associa automaticamente funcionalidades baseadas no nível do usuário.

        Args:
            usuario (Usuario): O objeto usuário a ser cadastrado.
        """
        self.usuarios.append(usuario)
        
        for funcionalidade in self.funcionalidades:
            if usuario.nivel >= funcionalidade.nivel:
                funcUsuario = FuncionalidadeUsuarios(
                    id=len(self.funcionalidadeUsuarios) + 1,
                    idUsuario=usuario.id,
                    idFuncionalidade=funcionalidade.id,
                    liberado=True
                )
            else:
                funcUsuario = FuncionalidadeUsuarios(
                    id=len(self.funcionalidadeUsuarios) + 1,
                    idUsuario=usuario.id,
                    idFuncionalidade=funcionalidade.id,
                    liberado=False
                )
            self.funcionalidadeUsuarios.append(funcUsuario)                

    def associarFuncionalidadeUsuarios(self, funcionalidadeUsuarios):
        """
        Associa uma funcionalidade a um usuário.

        Args:
            funcionalidadeUsuarios (FuncionalidadeUsuarios): A associação a ser adicionada.
        """
        self.funcionalidadeUsuarios.append(funcionalidadeUsuarios)

    def verificarAcesso(self, id_usuario, id_funcionalidade):
        """
        Verifica se um usuário tem acesso a uma determinada funcionalidade.

        Args:
            id_usuario (int): ID do usuário.
            id_funcionalidade (int): ID da funcionalidade.

        Returns:
            bool: True se o usuário tiver acesso, False caso contrário.
        """
        for usuario in self.usuarios:
            if usuario.id == id_usuario:
                for funcionalidadeUsuarios in self.funcionalidadeUsuarios:
                    if (funcionalidadeUsuarios.idUsuario == id_usuario and
                            funcionalidadeUsuarios.idFuncionalidade == id_funcionalidade):
                        for funcionalidade in self.funcionalidades:
                            if funcionalidade.id == id_funcionalidade:
                                if usuario.nivel <= funcionalidade.nivel:
                                    funcionalidadeUsuarios.liberado = True
                                    return True
                                else:
                                    funcionalidadeUsuarios.liberado = False
                                    return False
        return False

    def mostrarFuncionalidadesLiberadas(self, id_usuario):
        """
        Exibe e retorna as funcionalidades liberadas para um usuário.

        Args:
            id_usuario (int): ID do usuário.

        Returns:
            list: Lista de IDs das funcionalidades liberadas.
        """
        liberadas = []
        for funcUsuario in self.funcionalidadeUsuarios:
            if funcUsuario.idUsuario == id_usuario and funcUsuario.liberado:
                funcionalidadeAssociada = next(
                    (funcionalidade for funcionalidade in self.funcionalidades 
                     if funcionalidade.id == funcUsuario.idFuncionalidade), None
                )
                if funcionalidadeAssociada:
                    liberadas.append(funcionalidadeAssociada.id)
                    print(f"{funcionalidadeAssociada.id}- {funcionalidadeAssociada.nome}")
        print("0- Sair")
        return liberadas

    def novoUsuario(self):
        """
        Cria e retorna um novo objeto de usuário baseado na entrada do usuário.

        Returns:
            Usuario: O novo objeto usuário.
        """
        global CONTADOR_ID
        CONTADOR_ID += 1
        idUsuario = CONTADOR_ID
        
        nomeUsuario = input("Digite o nome do usuário: ")
        usernameUsuario = input("Digite o username do usuário: ")
        emailUsuario = input("Digite o email do usuário: ")
        setorUsuario = input("Digite o setor do usuário: ")
        cargoUsuario = input("Digite o cargo do usuário: ")
        nivelUsuario = input("Digite o nível do usuário: ")

        usuario = Usuarios(
            id=idUsuario,
            nome=nomeUsuario,
            username=usernameUsuario,
            email=emailUsuario,
            setor=setorUsuario,
            cargo=cargoUsuario,
            nivel=nivelUsuario
        )

        return usuario
    
    def novaFuncionalidade(self):
        """
        Cria e retorna uma nova funcionalidade baseada na entrada do usuário.

        Returns:
            Funcionalidades: A nova funcionalidade.
        """
        global contadorFunc
        contadorFunc += 1
        idFuncionalidade = contadorFunc
        
        nomeFuncionalidade = input("Digite o nome da funcionalidade: ")
        nivelFuncionalidade = input("Digite o nível da funcionalidade: ")

        funcionalidade = Funcionalidades(
            id=idFuncionalidade,
            nome=nomeFuncionalidade,
            nivel=nivelFuncionalidade
        )

        return funcionalidade

    def atualizarUsuario(self, id_usuario, nome, username, email, setor, cargo, nivel):
        """
        Atualiza as informações de um usuário.

        Args:
            id_usuario (int): ID do usuário a ser atualizado.
            nome (str): Novo nome do usuário.
            username (str): Novo username do usuário.
            email (str): Novo email do usuário.
            setor (str): Novo setor do usuário.
            cargo (str): Novo cargo do usuário.
            nivel (int): Novo nível do usuário.

        Returns:
            bool: True se a atualização for bem-sucedida, False caso contrário.
        """
        if not any(usuario.id == id_usuario for usuario in self.usuarios):
            return False
        if any(usuario.username == username and usuario.id != id_usuario for usuario in self.usuarios):
            return False
        
        for usuario in self.usuarios:
            if usuario.id == id_usuario:
                if nivel < 0:
                    return False
                usuario.nome = nome
                usuario.username = username
                usuario.email = email
                usuario.setor = setor
                usuario.cargo = cargo
                usuario.nivel = nivel
                return True
        return False

    def removerUsuario(self, id_usuario):
        """
        Remove um usuário e suas associações de funcionalidades.

        Args:
            id_usuario (int): ID do usuário a ser removido.
        """
        if any(usuario.id == id_usuario for usuario in self.usuarios):
            self.usuarios = [user for user in self.usuarios if user.id != id_usuario]
            self.funcionalidadeUsuarios = [fu for fu in self.funcionalidadeUsuarios if fu.idUsuario != id_usuario]
            print(f"Usuário {id_usuario} removido com sucesso.")
            return True
        else:
            return False


if __name__ == "__main__":
    sistema = SistemaGerenciamentoAcesso()

    ## Cadastrar funcionalidades TESTE
    funcionalidade1 = Funcionalidades(id=1, nome="Cadastrar Usuário", nivel=5)
    funcionalidade2 = Funcionalidades(id=2, nome="Remover Usuário", nivel=5)
    funcionalidade3 = Funcionalidades(id=3, nome="Editar Usuário", nivel=1)
    funcionalidade4 = Funcionalidades(id=4, nome="Calculadora", nivel=2)
    funcionalidade5 = Funcionalidades(id=5, nome="Calculadora de Equações", nivel=2)
    funcionalidade6 = Funcionalidades(id=6, nome="Calculadora Física", nivel=3)
    sistema.funcionalidades.append(funcionalidade1)
    sistema.funcionalidades.append(funcionalidade2)
    sistema.funcionalidades.append(funcionalidade3)
    sistema.funcionalidades.append(funcionalidade4)
    sistema.funcionalidades.append(funcionalidade5)
    sistema.funcionalidades.append(funcionalidade6)
      
    ## Cadastrar usuários TESTE
    admin = Usuarios(id=0, nome="Admin", username="admin", email="admin@", setor="", cargo="", nivel=5)
    usuario1 = Usuarios(id=1, nome="João", username="joao", email="joao@example.com", setor="RH", cargo="Analista", nivel=1)    
    sistema.cadastrarUsuario(admin)
    sistema.cadastrarUsuario(usuario1)
       
    print("Bem vindo, esse é um sistema para demonstrar o controle de acesso de vários usuários no sistema")
    while True:
        print("\n----- MENU -----\n")
        print("1- Login")
        print("2- Cadastrar Usuário")
        print("0- Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n--- LOGIN ---\n")
            userName = input("Username: ")
            senha = input("Senha: ")
            
            autenticado, userId = sistema.verificarSenha(userName, senha)
        
            if(autenticado):
                print("\n----- TP/TESTES DE SOFTWARE -----\n")
                print("Dado seu nível de acesso, essas são suas opções:")
                liberadas = sistema.mostrarFuncionalidadesLiberadas(userId)
                opcao = input("Escolha uma opção: ")
                
                if (int(opcao) in liberadas):                    
                    for f in liberadas:
                        if(int(opcao) == f):
                            if opcao == '1':
                                user = sistema.novoUsuario()
                                sistema.cadastrarUsuario(user)
                            if opcao == '2':
                                removerId = input("Qual o ID do usuário que deve ser removido? ")
                                sistema.removerUsuario(removerId)
                            if opcao == '3':
                                atualizarId = input("Qual o ID do usuário que deve ser editado? ")                            
                                nomeUsuario = input("Digite o nome do usuário: ")
                                usernameUsuario = input("Digite o username do usuário: ")
                                emailUsuario = input("Digite o email do usuário: ")
                                setorUsuario = input("Digite o setor do usuário: ")
                                cargoUsuario = input("Digite o cargo do usuário: ")
                                nivelUsuario = input("Digite o nível do usuário: ")

                                sistema.atualizarUsuario(atualizarId, nomeUsuario, usernameUsuario, emailUsuario, setorUsuario, cargoUsuario, nivelUsuario)
                            if opcao == '4':
                                calculadora()
                            
                            if opcao == '5':
                                calculadora_bhaskara()
                                
                            if opcao == '6':
                                calculadora_fisica()
                else:
                    print("Você não pode acessar essa funcionalidade ou ela não existe")
                        
        elif opcao == "0":
            print("Saindo do programa...")
            break

        elif opcao == "2":
            print("\n--- CADASTRAR USUÁRIO ---\n")
            usuario = sistema.novoUsuario()
            sistema.cadastrarUsuario(usuario)
            print("Usuário cadastrado com sucesso!")

        else:
            print("Opção inválida. Tente novamente.")