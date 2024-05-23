# Sistema de Gerenciamento de Acesso

## Membros do Grupo

- Henrique Rotsen Santos Ferreira
- Gabriel Castelo
- Bruno Henrique

## Explicação do Sistema

Este é um sistema de gerenciamento de acesso que controla os privilégios de usuários dentro de um sistema. Ele permite que administradores cadastrem usuários e funcionalidades, associando automaticamente funcionalidades aos usuários com base em seus níveis de acesso. Os principais componentes do sistema incluem:

1. **Usuários**: Representa os usuários do sistema, contendo informações como nome, username, email, setor, cargo, nível de acesso e senha.
2. **Funcionalidades**: Representa as funcionalidades disponíveis no sistema, cada uma com um nível mínimo de acesso necessário.
3. **FuncionalidadeUsuarios**: Representa a associação entre usuários e funcionalidades, indicando se o acesso a uma funcionalidade específica é liberado para um usuário.

### Funcionalidades Principais:

- **Cadastro de Usuários**: Administradores podem cadastrar novos usuários fornecendo informações básicas e nível de acesso.
- **Cadastro de Funcionalidades**: Administradores podem cadastrar novas funcionalidades especificando o nome e o nível mínimo de acesso necessário.
- **Autenticação de Usuários**: Usuários podem fazer login fornecendo username e senha.
- **Verificação de Acesso**: O sistema verifica se um usuário tem acesso a uma funcionalidade específica com base no nível de acesso.
- **Listagem de Funcionalidades**: Após o login, os usuários podem ver uma lista de funcionalidades às quais têm acesso.

## Tecnologias Utilizadas

- **Python**: A linguagem principal utilizada para a implementação do sistema.
- **Dataclasses**: Utilizadas para definir as classes `Usuarios`, `Funcionalidades` e `FuncionalidadeUsuarios`, simplificando a criação de classes com atributos.
- **Entrada de Dados via Console**: O sistema interage com o usuário através de entradas e saídas no console, permitindo o cadastro e a autenticação de usuários, além da verificação de funcionalidades.

Este sistema serve como uma demonstração de um controle de acesso básico, adequado para projetos que exigem gerenciamento de permissões e autenticação de usuários.