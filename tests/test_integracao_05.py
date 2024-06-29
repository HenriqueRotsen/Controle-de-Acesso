import unittest
import pytest
from ControleAcesso import Funcionalidades, Usuarios, SistemaGerenciamentoAcesso

class Funcionalidades:
    def __init__(self, id, nome, nivel):
        self.id = id
        self.nome = nome
        self.nivel = nivel

class Usuarios:
    def __init__(self, id, nome, username, email, setor, cargo, nivel):
        self.id = id
        self.nome = nome
        self.username = username
        self.email = email
        self.setor = setor
        self.cargo = cargo
        self.nivel = nivel

class SistemaGerenciamentoAcesso:
    def __init__(self):
        self.usuarios = []
        self.funcionalidades = []

    def cadastrarUsuario(self, usuario):
        self.usuarios.append(usuario)

    def verificarAcesso(self, usuario_id, funcionalidade_id):
        usuario = next((u for u in self.usuarios if u.id == usuario_id), None)
        funcionalidade = next((f for f in self.funcionalidades if f.id == funcionalidade_id), None)
        if usuario and funcionalidade:
            return usuario.nivel >= funcionalidade.nivel
        return False

class TesteVerificacaoAcessoFuncionalidade(unittest.TestCase):
    def test_verificacao_acesso(self):
        # 1. Inicialize o sistema.
        sistema = SistemaGerenciamentoAcesso()

        # 2. Cadastre funcionalidades de níveis diferentes.
        funcionalidade1 = Funcionalidades(id=1, nome="Funcionalidade Nível 1", nivel=1)
        funcionalidade2 = Funcionalidades(id=2, nome="Funcionalidade Nível 2", nivel=2)
        funcionalidade3 = Funcionalidades(id=3, nome="Funcionalidade Nível 3", nivel=3)
        sistema.funcionalidades.extend([funcionalidade1, funcionalidade2, funcionalidade3])

        # 3. Cadastre um novo usuário com nível 2.
        novo_usuario = Usuarios(id=1, nome="Teste Usuario", username="teste", email="teste@example.com", setor="TI", cargo="Analista", nivel=2)
        sistema.cadastrarUsuario(novo_usuario)

        # 4. Verifique se o sistema retorna o acesso correto (True/False) para cada funcionalidade.
        self.assertTrue(sistema.verificarAcesso(novo_usuario.id, funcionalidade1.id))
        self.assertTrue(sistema.verificarAcesso(novo_usuario.id, funcionalidade2.id))
        self.assertFalse(sistema.verificarAcesso(novo_usuario.id, funcionalidade3.id))

if __name__ == "__main__":
    unittest.main()