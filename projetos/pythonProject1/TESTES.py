from graphviz import Digraph

# Criando o Diagrama Entidade-Relacionamento estilo BRModelo para o Problema 1: Sistema de Biblioteca
der1_br = Digraph('ER_Sistema_Biblioteca_BRModelo', format='png')
der1_br.attr(rankdir='LR', size='10')

# Entidade Membro
der1_br.node('Membro', 'Membro', shape='rectangle')
der1_br.node('ID_Membro', 'ID_Membro (PK)', shape='ellipse')
der1_br.node('Nome', 'Nome', shape='ellipse')
der1_br.node('Data_Inscrição', 'Data_Inscrição', shape='ellipse')
der1_br.edge('Membro', 'ID_Membro')
der1_br.edge('Membro', 'Nome')
der1_br.edge('Membro', 'Data_Inscrição')

# Entidade Livro
der1_br.node('Livro', 'Livro', shape='rectangle')
der1_br.node('ID_Livro', 'ID_Livro (PK)', shape='ellipse')
der1_br.node('Título', 'Título', shape='ellipse')
der1_br.node('Autor', 'Autor', shape='ellipse')
der1_br.edge('Livro', 'ID_Livro')
der1_br.edge('Livro', 'Título')
der1_br.edge('Livro', 'Autor')

# Relacionamento Empréstimo
der1_br.node('Empréstimo', 'Empréstimo', shape='diamond')
der1_br.edge('Membro', 'Empréstimo', label='1')
der1_br.edge('Livro', 'Empréstimo', label='N')

der1_br.render('ER_Sistema_Biblioteca_BRModelo')

# Criando o Diagrama Entidade-Relacionamento estilo BRModelo para o Problema 2: Sistema de Gerenciamento de Cursos
der2_br = Digraph('ER_Gerenciamento_Cursos_BRModelo', format='png')
der2_br.attr(rankdir='LR', size='10')

# Entidade Aluno
der2_br.node('Aluno', 'Aluno', shape='rectangle')
der2_br.node('ID_Aluno', 'ID_Aluno (PK)', shape='ellipse')
der2_br.node('Nome_Aluno', 'Nome', shape='ellipse')
der2_br.node('Idade', 'Idade', shape='ellipse')
der2_br.node('Curso_Matriculado', 'Curso_Matriculado', shape='ellipse')
der2_br.edge('Aluno', 'ID_Aluno')
der2_br.edge('Aluno', 'Nome_Aluno')
der2_br.edge('Aluno', 'Idade')
der2_br.edge('Aluno', 'Curso_Matriculado')

# Entidade Curso
der2_br.node('Curso', 'Curso', shape='rectangle')
der2_br.node('ID_Curso', 'ID_Curso (PK)', shape='ellipse')
der2_br.node('Nome_Curso', 'Nome_Curso', shape='ellipse')
der2_br.node('Carga_Horária', 'Carga_Horária', shape='ellipse')
der2_br.node('Departamento_Curso', 'Departamento', shape='ellipse')
der2_br.edge('Curso', 'ID_Curso')
der2_br.edge('Curso', 'Nome_Curso')
der2_br.edge('Curso', 'Carga_Horária')
der2_br.edge('Curso', 'Departamento_Curso')

# Entidade Professor
der2_br.node('Professor', 'Professor', shape='rectangle')
der2_br.node('ID_Professor', 'ID_Professor (PK)', shape='ellipse')
der2_br.node('Nome_Professor', 'Nome', shape='ellipse')
der2_br.node('Especialização', 'Especialização', shape='ellipse')
der2_br.node('Departamento_Professor', 'Departamento', shape='ellipse')
der2_br.edge('Professor', 'ID_Professor')
der2_br.edge('Professor', 'Nome_Professor')
der2_br.edge('Professor', 'Especialização')
der2_br.edge('Professor', 'Departamento_Professor')

# Relacionamento Inscrição
der2_br.node('Inscrição', 'Inscrição', shape='diamond')
der2_br.edge('Aluno', 'Inscrição', label='1')
der2_br.edge('Curso', 'Inscrição', label='N')

# Relacionamento Ensina
der2_br.node('Ensina', 'Ensina', shape='diamond')
der2_br.edge('Professor', 'Ensina', label='N')
der2_br.edge('Curso', 'Ensina', label='N')

der2_br.render('ER_Gerenciamento_Cursos_BRModelo')
