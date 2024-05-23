import pytest
from ControleAcesso import Funcionalidades, Usuarios, SistemaGerenciamentoAcesso

@pytest.fixture
def sistema():
    return SistemaGerenciamentoAcesso()

def test_atualizarUsuario_sucesso(sistema):
    usuario = Usuarios(id=1, nome="João", username="joao", email="joao@email.com", setor="RH", cargo="Analista", nivel=1)
    sistema.atualizarUsuario(usuario.id, "João da Silva", "joao.silva", "joao@email.com", "TI", "Desenvolvedor", 2)
    
    # Verifique se o usuário foi atualizado
    assert len(sistema.usuarios) == 1
    assert sistema.usuarios[0].nome == "João da Silva"
    assert sistema.usuarios[0].username == "joao.silva"
    assert sistema.usuarios[0].email == "joao@email.com"
    assert sistema.usuarios[0].setor == "TI"
    assert sistema.usuarios[0].cargo == "Desenvolvedor"
    assert sistema.usuarios[0].nivel == 2

def test_atualizarUsuario_inexistente(sistema):
    usuario = Usuarios(id=1, nome="João", username="joao", email="joao@email.com", setor="RH", cargo="Analista", nivel=1)
    resultado = sistema.atualizarDadosUsuario(999, "Novo Nome", "novo_username", "novo@email.com", "Novo Setor", "Novo Cargo", 3)

    # Verifique se o usuário não foi atualizado
    assert resultado == False
    

def test_atualizarUsuario_nivel_invalido(sistema):
    usuario = Usuarios(id=1, nome="João", username="joao", email="joao@email.com", setor="RH", cargo="Analista", nivel=1)
    sistema.atualizarUsuario(usuario.id, "João da Silva", "joao.silva", "joao@email.com", "TI", "Desenvolvedor", -1)

    # Verifique se o usuário não foi atualizado