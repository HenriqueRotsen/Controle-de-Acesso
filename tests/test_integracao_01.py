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
    
    def test_cadastro_usuario_associacao_funcionalidades(self):
        # Cadastrar um novo usuário com nível 3
        novo_usuario = Usuarios(id=2, nome="Maria", username="maria", email="maria@example.com", setor="TI", cargo="Dev", nivel=3)
        self.sistema.cadastrarUsuario(novo_usuario)
        
        # Verificar se as funcionalidades com nível <= 3 foram associadas corretamente ao usuário
        funcionalidades_esperadas = [3, 4, 5, 6]  # IDs das funcionalidades que devem ser liberadas
        
        funcionalidades_associadas = self.sistema.mostrarFuncionalidadesLiberadas(novo_usuario.id)
        
        self.assertEqual(set(funcionalidades_esperadas), set(funcionalidades_associadas))

if __name__ == "__main__":
    unittest.main()