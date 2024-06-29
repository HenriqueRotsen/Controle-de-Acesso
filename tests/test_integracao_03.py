import pytest
import unittest
from ControleAcesso import Funcionalidades, Usuarios, SistemaGerenciamentoAcesso


class TestSistemaGerenciamentoAcesso(unittest.TestCase):
    def setUp(self):
        self.sistema = SistemaGerenciamentoAcesso()
        
        # Configurar funcionalidades
        self.funcionalidade1 = Funcionalidades(id=1, nome="Cadastrar Usuário", nivel=5)
        self.funcionalidade2 = Funcionalidades(id=2, nome="Remover Usuário", nivel=5)
        self.funcionalidade3 = Funcionalidades(id=3, nome="Editar Usuário", nivel=1)
        self.funcionalidade4 = Funcionalidades(id=4, nome="Calculadora", nivel=2)
        self.funcionalidade5 = Funcionalidades(id=5, nome="Calculadora de Equações", nivel=2)
        self.funcionalidade6 = Funcionalidades(id=6, nome="Calculadora Física", nivel=3)
        
        self.sistema.funcionalidades.append(self.funcionalidade1)
        self.sistema.funcionalidades.append(self.funcionalidade2)
        self.sistema.funcionalidades.append(self.funcionalidade3)
        self.sistema.funcionalidades.append(self.funcionalidade4)
        self.sistema.funcionalidades.append(self.funcionalidade5)
        self.sistema.funcionalidades.append(self.funcionalidade6)

    def teste_atualizacao_usuario(self):
        sistema = SistemaGerenciamentoAcesso()

        # Cadastrar funcionalidades TESTE
        funcionalidade1 = Funcionalidades(id=1, nome="Cadastrar Usuário", nivel=5)
        funcionalidade2 = Funcionalidades(id=2, nome="Remover Usuário", nivel=5)
        funcionalidade3 = Funcionalidades(id=3, nome="Editar Usuário", nivel=1)
        funcionalidade4 = Funcionalidades(id=4, nome="Calculadora", nivel=2)
        funcionalidade5 = Funcionalidades(id=5, nome="Calculadora de Equações", nivel=2)
        funcionalidade6 = Funcionalidades(id=6, nome="Calculadora Física", nivel=3)
        sistema.funcionalidades.extend([funcionalidade1, funcionalidade2, funcionalidade3, funcionalidade4, funcionalidade5, funcionalidade6])

        # Cadastrar um usuário inicial
        usuario_inicial = Usuarios(id=1, nome="João", username="joao", email="joao@example.com", setor="RH", cargo="Analista", nivel=1)
        sistema.cadastrarUsuario(usuario_inicial)

        # Atualizar detalhes do usuário
        novo_nome = "João Silva"
        novo_username = "joao_silva"
        novo_email = "joao.silva@example.com"
        novo_setor = "TI"
        novo_cargo = "Desenvolvedor"
        novo_nivel = 2

        # Atualizar o usuário com ID 1
        atualizacao_sucesso = sistema.atualizarUsuario(id_usuario=1, nome=novo_nome, username=novo_username, email=novo_email, setor=novo_setor, cargo=novo_cargo, nivel=novo_nivel)
        
        # Verificar se a atualização foi bem-sucedida
        if not atualizacao_sucesso:
            print("Falha na atualização do usuário.")
            return

        # Verificar se os dados foram atualizados corretamente
        usuario_atualizado = next((u for u in sistema.usuarios if u.id == 1), None)
        assert usuario_atualizado is not None, "Usuário não encontrado após atualização."
        assert usuario_atualizado.nome == novo_nome, f"Nome não atualizado corretamente. Esperado: {novo_nome}, Obtido: {usuario_atualizado.nome}"
        assert usuario_atualizado.username == novo_username, f"Username não atualizado corretamente. Esperado: {novo_username}, Obtido: {usuario_atualizado.username}"
        assert usuario_atualizado.email == novo_email, f"Email não atualizado corretamente. Esperado: {novo_email}, Obtido: {usuario_atualizado.email}"
        assert usuario_atualizado.setor == novo_setor, f"Setor não atualizado corretamente. Esperado: {novo_setor}, Obtido: {usuario_atualizado.setor}"
        assert usuario_atualizado.cargo == novo_cargo, f"Cargo não atualizado corretamente. Esperado: {novo_cargo}, Obtido: {usuario_atualizado.cargo}"
        assert usuario_atualizado.nivel == novo_nivel, f"Nível não atualizado corretamente. Esperado: {novo_nivel}, Obtido: {usuario_atualizado.nivel}"

        print("Teste de atualização de usuário concluído com sucesso.")

if __name__ == "__main__":
    teste_atualizacao_usuario()