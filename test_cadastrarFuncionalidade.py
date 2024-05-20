import pytest
from ControleAcesso import Funcionalidades, SistemaGerenciamentoAcesso

@pytest.fixture
def sistema():
    return SistemaGerenciamentoAcesso()

def test_cadastrarFuncionalidade_sucesso(sistema):
    funcionalidade = Funcionalidades(id=1, nome="Cadastrar Usuário", nivel=5)
    sistema.cadastrarFuncionalidade(funcionalidade)
    
    # Verifique se a funcionalidade foi adicionada ao sistema
    assert len(sistema.funcionalidades) == 1
    assert sistema.funcionalidades[0].id == 1
    assert sistema.funcionalidades[0].nome == "Cadastrar Usuário"
    assert sistema.funcionalidades[0].nivel == 5

def test_cadastrarFuncionalidade_multiplas(sistema):
    funcionalidade1 = Funcionalidades(id=1, nome="Cadastrar Usuário", nivel=5)
    funcionalidade2 = Funcionalidades(id=2, nome="Remover Usuário", nivel=5)
    funcionalidade3 = Funcionalidades(id=3, nome="Editar Usuário", nivel=1)
    
    sistema.cadastrarFuncionalidade(funcionalidade1)
    sistema.cadastrarFuncionalidade(funcionalidade2)
    sistema.cadastrarFuncionalidade(funcionalidade3)
    
    # Verifique se todas as funcionalidades foram adicionadas ao sistema
    assert len(sistema.funcionalidades) == 3
    assert sistema.funcionalidades[0].id == 1
    assert sistema.funcionalidades[0].nome == "Cadastrar Usuário"
    assert sistema.funcionalidades[0].nivel == 5
    assert sistema.funcionalidades[1].id == 2
    assert sistema.funcionalidades[1].nome == "Remover Usuário"
    assert sistema.funcionalidades[1].nivel == 5
    assert sistema.funcionalidades[2].id == 3
    assert sistema.funcionalidades[2].nome == "Editar Usuário"
    assert sistema.funcionalidades[2].nivel == 1
