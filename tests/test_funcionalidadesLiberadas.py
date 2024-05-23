import pytest
import io
import sys
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

@pytest.fixture
def funcionalidade_usuario_exemplo():
    return FuncionalidadeUsuarios(id=1, idUsuario=1, idFuncionalidade=1, liberado=True)

def test_mostrar_funcionalidades_liberadas(sistema_gerenciamento_acesso, usuario_exemplo, funcionalidade_exemplo, funcionalidade_usuario_exemplo, capsys):
    sistema_gerenciamento_acesso.cadastrarUsuario(usuario_exemplo)
    sistema_gerenciamento_acesso.funcionalidades.append(funcionalidade_exemplo)
    sistema_gerenciamento_acesso.associarFuncionalidadeUsuarios(funcionalidade_usuario_exemplo)

    sys.stdout = io.StringIO()
    sistema_gerenciamento_acesso.mostrarFuncionalidadesLiberadas(1)
    captured = sys.stdout.getvalue()

    assert "1- Funcionalidade Exemplo" in captured
    assert "0- Sair" in captured

    sys.stdout = sys.__stdout__

def test_mostrar_funcionalidades_liberadas_sem_funcionalidades(sistema_gerenciamento_acesso, usuario_exemplo, capsys):
    sistema_gerenciamento_acesso.cadastrarUsuario(usuario_exemplo)

    sys.stdout = io.StringIO()
    sistema_gerenciamento_acesso.mostrarFuncionalidadesLiberadas(1)
    captured = sys.stdout.getvalue()

    assert "0- Sair" in captured

    sys.stdout = sys.__stdout__
