import pytest
from ControleAcesso import Usuarios, SistemaGerenciamentoAcesso

@pytest.fixture
def sistema():
    return SistemaGerenciamentoAcesso()


def test_removerUsuario_sucesso(sistema):
    usuario = Usuarios(id=1, nome="João", username="joao", email="joao@email.com", setor="RH", cargo="Analista", nivel=1)
    sistema.cadastrarUsuario(usuario)
    resultado = sistema.removerUsuario(1)

    # Verifique se o usuário foi removido
    assert resultado == True
    assert len(sistema.usuarios) == 0

def test_removerUsuario_inexistente(sistema):
    usuario = Usuarios(id=1, nome="João", username="joao", email="joao@email.com", setor="RH", cargo="Analista", nivel=1)
    sistema.cadastrarUsuario(usuario)
    resultado = sistema.removerUsuario(999)

    # Verifique se o usuário não foi removido
    assert resultado == False
    assert len(sistema.usuarios) == 1

def test_removerUsuario_ultimo(sistema):
    usuario = Usuarios(id=1, nome="João", username="joao", email="joao@email.com", setor="RH", cargo="Analista", nivel=1)
    sistema.cadastrarUsuario(usuario)
    resultado = sistema.removerUsuario(1)

    # Verifique se o usuário foi removido
    assert resultado == True
    assert len(sistema.usuarios) == 0

def test_removerUsuario_apos_remocao(sistema):
    usuario = Usuarios(id=1, nome="João", username="joao", email="joao@email.com", setor="RH", cargo="Analista", nivel=1)
    sistema.cadastrarUsuario(usuario)
    sistema.removerUsuario(1)
    resultado = sistema.removerUsuario(1)

    # Verifique se o usuário não foi removido
    assert resultado == False
    assert len(sistema.usuarios) == 0
