import pytest
from ControleAcesso import Funcionalidades, Usuarios, SistemaGerenciamentoAcesso

@pytest.fixture
def sistema():
    sistema = SistemaGerenciamentoAcesso()

    # Adicionar algumas funcionalidades para teste
    funcionalidade1 = Funcionalidades(id=1, nome="Funcionalidade Nível 1", nivel=1)
    funcionalidade2 = Funcionalidades(id=2, nome="Funcionalidade Nível 2", nivel=2)
    funcionalidade3 = Funcionalidades(id=3, nome="Funcionalidade Nível 3", nivel=3)
    sistema.funcionalidades.append(funcionalidade1)
    sistema.funcionalidades.append(funcionalidade2)
    sistema.funcionalidades.append(funcionalidade3)

    return sistema

def test_cadastro_e_verificacao_senha(sistema):
    # Cadastrar um novo usuário
    novo_usuario = Usuarios(id=2, nome="Teste", username="teste", email="teste@example.com", setor="TI", cargo="Analista", nivel=2, senha=789)
    sistema.cadastrarUsuario(novo_usuario)

    # Verificar a senha do novo usuário
    autenticado, user_id = sistema.verificarSenha("teste", "789")
    assert autenticado == True
    assert user_id == 2

def test_verificacao_acesso_funcionalidade(sistema):
    # 1. Inicialize o sistema (feito pela fixture)
    
    # 2. Cadastre um novo usuário com nível 2
    novo_usuario = Usuarios(id=1, nome="Usuário Teste", username="usuario_teste", email="teste2@example.com", setor="TI", cargo="Analista", nivel=2, senha=123)
    sistema.cadastrarUsuario(novo_usuario)
    
    # 3. Tente acessar funcionalidades com nível 1, 2, e 3
    acesso_nivel_1 = sistema.verificarAcesso(1, 1)  # Funcionalidade Nível 1
    acesso_nivel_2 = sistema.verificarAcesso(1, 2)  # Funcionalidade Nível 2
    acesso_nivel_3 = sistema.verificarAcesso(1, 3)  # Funcionalidade Nível 3

    # 4. Verifique se o sistema retorna o acesso correto (True/False) para cada funcionalidade
    assert acesso_nivel_1 == True, f"Esperado acesso True para funcionalidade de nível 1, mas obteve {acesso_nivel_1}"
    assert acesso_nivel_2 == True, f"Esperado acesso True para funcionalidade de nível 2, mas obteve {acesso_nivel_2}"
    assert acesso_nivel_3 == False, f"Esperado acesso False para funcionalidade de nível 3, mas obteve {acesso_nivel_3}"

def test_atualizacao_usuario(sistema):
    # 1. Inicialize o sistema (feito pela fixture)
    
    # 2. Cadastre um novo usuário
    novo_usuario = Usuarios(id=1, nome="Usuário Teste", username="usuario_teste", email="teste2@example.com", setor="TI", cargo="Analista", nivel=2, senha=123)
    sistema.cadastrarUsuario(novo_usuario)
    
    # 3. Atualize os detalhes do usuário (nome, username, email, setor, cargo, nível)
    usuario_atualizado = {
        'nome': 'Usuário Teste Atualizado',
        'username': 'usuario_teste_atualizado',
        'email': 'teste2_atualizado@example.com',
        'setor': 'TI Atualizado',
        'cargo': 'Senior Analyst',
        'nivel': 3
    }
    sistema.atualizarUsuario(1, **usuario_atualizado)
    
    # 4. Verifique se as mudanças foram aplicadas corretamente
    usuario = next(user for user in sistema.usuarios if user.id == 1)
    
    assert usuario.nome == usuario_atualizado['nome'], f"Esperado nome {usuario_atualizado['nome']}, mas obteve {usuario.nome}"
    assert usuario.username == usuario_atualizado['username'], f"Esperado username {usuario_atualizado['username']}, mas obteve {usuario.username}"
    assert usuario.email == usuario_atualizado['email'], f"Esperado email {usuario_atualizado['email']}, mas obteve {usuario.email}"
    assert usuario.setor == usuario_atualizado['setor'], f"Esperado setor {usuario_atualizado['setor']}, mas obteve {usuario.setor}"
    assert usuario.cargo == usuario_atualizado['cargo'], f"Esperado cargo {usuario_atualizado['cargo']}, mas obteve {usuario.cargo}"
    assert usuario.nivel == usuario_atualizado['nivel'], f"Esperado nível {usuario_atualizado['nivel']}, mas obteve {usuario.nivel}"
