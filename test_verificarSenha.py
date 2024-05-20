import pytest
from ControleAcesso import Usuarios, SistemaGerenciamentoAcesso

@pytest.fixture
def sistema():
    sistema = SistemaGerenciamentoAcesso()

    # Adicionar alguns usuários para teste
    admin = Usuarios(id=0, nome="Admin", username="admin", email="admin@", setor="", cargo="", nivel=5, senha=123)
    usuario1 = Usuarios(id=1, nome="João", username="joao", email="joao@example.com", setor="RH", cargo="Analista", nivel=1, senha=456)
    sistema.cadastrarUsuario(admin)
    sistema.cadastrarUsuario(usuario1)

    return sistema

def test_verificarSenha_sucesso(sistema):
    autenticado, user_id = sistema.verificarSenha("admin", "123")
    assert autenticado == True
    assert user_id == 0

    autenticado, user_id = sistema.verificarSenha("joao", "456")
    assert autenticado == True
    assert user_id == 1

def test_verificarSenha_falha_usuario_incorreto(sistema):
    autenticado, user_id = sistema.verificarSenha("admin", "999")
    assert autenticado == False
    assert user_id == -1

def test_verificarSenha_falha_senha_incorreta(sistema):
    autenticado, user_id = sistema.verificarSenha("joao", "123")
    assert autenticado == False
    assert user_id == -1

def test_verificarSenha_usuario_nao_existente(sistema):
    autenticado, user_id = sistema.verificarSenha("maria", "123")
    assert autenticado == False
    assert user_id == -1
    