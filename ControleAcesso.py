from dataclasses import dataclass

# Variavel global de número de usuario
contadorId = 0
contadorFunc = 0

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
        if(funcionalidade.nivel > 0):
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
        
    def novoUsuario(self):
        #Id definido automaticamente
        global contadorId
        contadorId += 1
        idUsuario = contadorId
        
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
        #Id definido automaticamente
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
    # Verifica se o ID do usuário existe na lista de usuários
     if not any(usuario.id == id_usuario for usuario in self.usuarios):
        return False
    # Verifica se o novo username já existe para outro usuário
     if any(usuario.username == username and usuario.id != id_usuario for usuario in self.usuarios):
        return False
    # O ID do usuário existe e o novo username não está duplicado, então atualiza os dados
     for usuario in self.usuarios:
         if usuario.id == id_usuario:
             usuario.nome = nome
             usuario.username = username
             usuario.email = email
             usuario.setor = setor
             usuario.cargo = cargo
             if usuario.nivel < 0:
                 return False
             usuario.nivel = nivel
             return True
    # Se o loop terminou sem atualizar, retorna False
    return False



if __name__ == "__main__":
    sistema = SistemaGerenciamentoAcesso()

    ## Cadastrar funcionalidades TESTE
    funcionalidade1 = Funcionalidades(id=1, nome="Cadastrar Usuário", nivel=5)
    funcionalidade2 = Funcionalidades(id=2, nome="Remover Usuário", nivel=5)
    funcionalidade3 = Funcionalidades(id=3, nome="Editar Usuário", nivel=1)
    sistema.cadastrarFuncionalidade(funcionalidade1)
    sistema.cadastrarFuncionalidade(funcionalidade2)
    sistema.cadastrarFuncionalidade(funcionalidade3)
      
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
                sistema.mostrarFuncionalidadesLiberadas(userId)
                opcao = input("Escolha uma opção: ")
                
                if opcao == "0":
                    print("Deslogando...")
                else:
                    print("Opção inválida. Tente novamente.")
                      
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