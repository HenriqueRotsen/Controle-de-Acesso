import pytest
from ControleAcesso import Funcionalidades, Usuarios, SistemaGerenciamentoAcesso

@pytest.fixture
def sistema():
    return SistemaGerenciamentoAcesso()

def test_cadastrarUsuario_sucesso(sistema):
    usuario = Usuarios(id=1, nome="João", username="joao", email="joao@example.com", setor="RH", cargo="Analista", nivel=1, senha=456)
    sistema.cadastrarUsuario(usuario)
    
    # Verifique se o usuário foi adicionado ao sistema
    assert len(sistema.usuarios) == 1
    assert sistema.usuarios[0].username == "joao"
    assert sistema.usuarios[0].email == "joao@example.com"
    assert sistema.usuarios[0].setor == "RH"
    assert sistema.usuarios[0].cargo == "Analista"
    assert sistema.usuarios[0].nivel == 1
    assert sistema.usuarios[0].senha == 456

def test_cadastrarUsuario_nivel_adequado(sistema):
    # Adiciona funcionalidades ao sistema
    funcionalidade1 = Funcionalidades(id=1, nome="Cadastrar Usuário", nivel=5)
    funcionalidade2 = Funcionalidades(id=2, nome="Remover Usuário", nivel=5)
    funcionalidade3 = Funcionalidades(id=3, nome="Editar Usuário", nivel=1)
    sistema.funcionalidades.append(funcionalidade1)
    sistema.funcionalidades.append(funcionalidade2)
    sistema.funcionalidades.append(funcionalidade3)

    usuario = Usuarios(id=2, nome="Maria", username="maria", email="maria@example.com", setor="TI", cargo="Desenvolvedor", nivel=2, senha=789)
    sistema.cadastrarUsuario(usuario)
    
    # Verifique se o usuário foi adicionado ao sistema
    assert len(sistema.usuarios) == 1
    assert sistema.usuarios[0].username == "maria"
    assert sistema.usuarios[0].email == "maria@example.com"
    assert sistema.usuarios[0].setor == "TI"
    assert sistema.usuarios[0].cargo == "Desenvolvedor"
    assert sistema.usuarios[0].nivel == 2
    assert sistema.usuarios[0].senha == 789

    # Verifique as associações de funcionalidades
    func_liberadas = [f.idFuncionalidade for f in sistema.funcionalidadeUsuarios if f.idUsuario == 2 and f.liberado]
    assert func_liberadas == [3]  # Maria deve ter acesso apenas à funcionalidade de nível 1 (Editar Usuário)

def test_cadastrarUsuario_nivel_alto(sistema):
    # Adiciona funcionalidades ao sistema
    funcionalidade1 = Funcionalidades(id=1, nome="Cadastrar Usuário", nivel=5)
    funcionalidade2 = Funcionalidades(id=2, nome="Remover Usuário", nivel=5)
    funcionalidade3 = Funcionalidades(id=3, nome="Editar Usuário", nivel=1)
    sistema.funcionalidades.append(funcionalidade1)
    sistema.funcionalidades.append(funcionalidade2)
    sistema.funcionalidades.append(funcionalidade3)

    usuario = Usuarios(id=3, nome="Admin", username="admin", email="admin@example.com", setor="Administração", cargo="Administrador", nivel=5, senha=1234)
    sistema.cadastrarUsuario(usuario)
    
    # Verifique se o usuário foi adicionado ao sistema
    assert len(sistema.usuarios) == 1
    assert sistema.usuarios[0].username == "admin"
    assert sistema.usuarios[0].email == "admin@example.com"
    assert sistema.usuarios[0].setor == "Administração"
    assert sistema.usuarios[0].cargo == "Administrador"
    assert sistema.usuarios[0].nivel == 5
    assert sistema.usuarios[0].senha == 1234

    # Verifique as associações de funcionalidades
    func_liberadas = [f.idFuncionalidade for f in sistema.funcionalidadeUsuarios if f.idUsuario == 3 and f.liberado]
    assert set(func_liberadas) == {1, 2, 3}  # Admin deve ter acesso a todas as funcionalidades
    