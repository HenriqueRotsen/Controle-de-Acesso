from dataclasses import dataclass

@dataclass
class Usuarios:
    def __init__(self, id, nome, username, email, setor, cargo, nivel, senha=123):
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
    def __init__(self, id, nome, nivel):
        self.id = id
        self.nome = nome
        self.nivel = nivel

@dataclass    
class FuncionalidadeUsuarios:
    def __init__(self, id, idUsuario, idFuncionalidade, liberado):
        self.id = id
        self.idUsuario = idUsuario
        self.idFuncionalidade = idFuncionalidade
        self.liberado = liberado

class SistemaGerenciamentoAcesso:
    def __init__(self):
        self.usuarios = []
        self.funcionalidades = []
        self.funcionalidadeUsuarios = []
    
    def verificarSenha(self, userName, senha):
        for user in self.usuarios:
            if user.username == userName and user.senha == int(senha):
                return (True, user.id)
        return (False, -1)
    
    def cadastrarUsuario(self, usuario):
        self.usuarios.append(usuario)
        
        # Associar automaticamente as funcionalidades com base no nível de acesso do usuário
        for funcionalidade in self.funcionalidades:
            if usuario.nivel >= funcionalidade.nivel:
                funcUsuario = FuncionalidadeUsuarios(id=len(self.funcionalidadeUsuarios) + 1,
                                                      idUsuario=usuario.id,
                                                      idFuncionalidade=funcionalidade.id,
                                                      liberado=True)
                self.funcionalidadeUsuarios.append(funcUsuario)
            else:
                funcUsuario = FuncionalidadeUsuarios(id=len(self.funcionalidadeUsuarios) + 1,
                                                      idUsuario=usuario.id,
                                                      idFuncionalidade=funcionalidade.id,
                                                      liberado=False)
                self.funcionalidadeUsuarios.append(funcUsuario)
                

    def cadastrarFuncionalidade(self, funcionalidade):
        self.funcionalidades.append(funcionalidade)

    def associarFuncionalidadeUsuarios(self, funcionalidadeUsuarios):
        self.funcionalidadeUsuarios.append(funcionalidadeUsuarios)

    def verificarAcesso(self, id_usuario, id_funcionalidade):
        for usuario in self.usuarios:
            if usuario.id == id_usuario:
                for funcionalidadeUsuarios in self.funcionalidadeUsuarios:
                    if funcionalidadeUsuarios.idUsuario == id_usuario and funcionalidadeUsuarios.idFuncionalidade == id_funcionalidade:
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
        for funcUsuario in self.funcionalidadeUsuarios:
            if funcUsuario.idUsuario == id_usuario and funcUsuario.liberado:
                funcionalidadeAssociada = next((funcionalidade for funcionalidade in self.funcionalidades if funcionalidade.id == funcUsuario.idFuncionalidade), None)
                if funcionalidadeAssociada:
                    print(str(funcionalidadeAssociada.id) + "- " + funcionalidadeAssociada.nome)
        print("0- Sair")
        
    
def novoUsuario():
    idUsuario = input("Digite o ID do usuário: ")
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


def novaFuncionalidade():
    idFuncionalidade = input("Digite o ID da funcionalidade: ")
    nomeFuncionalidade = input("Digite o nome da funcionalidade: ")
    nivelFuncionalidade = input("Digite o nível da funcionalidade: ")

    funcionalidade = Funcionalidades(
        id=idFuncionalidade,
        nome=nomeFuncionalidade,
        nivel=nivelFuncionalidade
    )

    return funcionalidade


if __name__ == "__main__":
    sistema = SistemaGerenciamentoAcesso()

    ## Cadastrar funcionalidades
    funcionalidade1 = Funcionalidades(id=1, nome="Cadastrar Usuário", nivel=5)
    funcionalidade2 = Funcionalidades(id=2, nome="Remover Usuário", nivel=5)
    funcionalidade3 = Funcionalidades(id=3, nome="Editar Usuário", nivel=1)
    sistema.cadastrarFuncionalidade(funcionalidade1)
    sistema.cadastrarFuncionalidade(funcionalidade2)
    sistema.cadastrarFuncionalidade(funcionalidade3)
      
    ## Cadastrar usuários
    admin = Usuarios(id=0, nome="Admin", username="admin", email="admin@", setor="", cargo="", nivel=5)
    usuario1 = Usuarios(id=1, nome="João", username="joao", email="joao@example.com", setor="RH", cargo="Analista", nivel=1)
    #usuario2 = Usuarios(id=2, nome="Maria", email="maria@example.com", setor="TI", cargo="Desenvolvedor", nivel=2)
    
    sistema.cadastrarUsuario(admin)
    sistema.cadastrarUsuario(usuario1)
       
    print("Bem vindo, esse é um sistema para demonstrar o controle de acesso de vários usuários no sistema")
    while True:
        print("\n----- MENU -----\n")
        print("1- Login")
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
                sistema.mostrarFuncionalidadesLiberadas(userId)
                opcao = input("Escolha uma opção: ")
                
                if opcao == "0":
                    print("Deslogando...")
                else:
                    print("Opção inválida. Tente novamente.")
                      
        elif opcao == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")