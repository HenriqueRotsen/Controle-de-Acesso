import pytest

from ControleAcesso import Usuarios, Funcionalidades, FuncionalidadeUsuarios, SistemaGerenciamentoAcesso

@pytest.fixture
def sistema_gerenciamento_acesso():
    return SistemaGerenciamentoAcesso()

@pytest.fixture
def usuario_exemplo():
    return Usuarios(id=1, nome="Exemplo", username="exemplo", email="exemplo@example.com", setor="TI", cargo="Desenvolvedor", nivel=3)

@pytest.fixture
def funcionalidade_exemplo():
    return Funcionalidades(id=1, nome="Funcionalidade Exemplo", nivel=3)

def test_verificar_acesso_sucesso(sistema_gerenciamento_acesso, usuario_exemplo, funcionalidade_exemplo):
    sistema_gerenciamento_acesso.cadastrarUsuario(usuario_exemplo)
    sistema_gerenciamento_acesso.funcionalidades.append(funcionalidade_exemplo)

    assert sistema_gerenciamento_acesso.verificarAcesso(1, 1) == True

def test_verificar_acesso_falha(sistema_gerenciamento_acesso, usuario_exemplo, funcionalidade_exemplo):
    funcionalidade_exemplo.nivel = 5
    sistema_gerenciamento_acesso.funcionalidades.append(funcionalidade_exemplo)
    sistema_gerenciamento_acesso.cadastrarUsuario(usuario_exemplo)

    assert sistema_gerenciamento_acesso.verificarAcesso(1, 1) == False

def test_verificar_acesso_usuario_inexistente(sistema_gerenciamento_acesso, funcionalidade_exemplo):
    sistema_gerenciamento_acesso.funcionalidades.append(funcionalidade_exemplo)

    assert sistema_gerenciamento_acesso.verificarAcesso(1, 1) == False

def test_verificar_acesso_funcionalidade_inexistente(sistema_gerenciamento_acesso, usuario_exemplo):
    sistema_gerenciamento_acesso.cadastrarUsuario(usuario_exemplo)

    assert sistema_gerenciamento_acesso.verificarAcesso(1, 1) == False

def test_verificar_acesso_nivel_funcionalidade_menor(sistema_gerenciamento_acesso, usuario_exemplo, funcionalidade_exemplo):
    funcionalidade_exemplo.nivel = 2
    sistema_gerenciamento_acesso.cadastrarUsuario(usuario_exemplo)
    sistema_gerenciamento_acesso.funcionalidades.append(funcionalidade_exemplo)

    assert sistema_gerenciamento_acesso.verificarAcesso(1, 1) == True
