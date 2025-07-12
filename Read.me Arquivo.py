# 🎯 Sistema de Recomendação de Vagas por Perfil Acadêmico

Este projeto em Python simula um sistema simples de recomendação de vagas baseado no **semestre atual do aluno** e nos **cursos que ele já realizou**. A partir de uma base de vagas pré-cadastradas, o sistema exibe aquelas mais compatíveis com o perfil do usuário.

---

## 🚀 Tecnologias Utilizadas

- Python 3.x
- Programação orientada a objetos (POO)
- Manipulação de conjuntos (`set`)
- Entrada e saída no terminal

---

## 💡 Funcionalidades

- Cadastro do aluno (nome, semestre e cursos)
- Avaliação de compatibilidade com vagas:
  - Mínimo de **2 cursos em comum**
  - Semestre **maior ou igual** ao exigido pela vaga
- Exibição formatada das vagas compatíveis

---

## 🧠 Lógica de Compatibilidade

```python
aluno.semestre >= vaga.semestre and len(cursos_em_comum) >= 2
🖼️ Exemplo de Uso
bash
Copiar
Editar
Digite seu nome: Felipe
Digite seu semestre: 3
Digite seus cursos separados por vírgula: Python, SQL, JavaScript

Vagas compatíveis para você:
===========================================================================
Vaga                               Semestre Mínimo    Cursos Exigidos
===========================================================================
Administrador de Banco de Dados    3                  nosql, shell script, sql
Desenvolvedor Backend              3                  nosql, python, sql
Desenvolvedor Frontend             2                  css, javascript, react
Cybersecurity Analyst              3                  network security, python, siem
===========================================================================
📦 Como Executar
Clone ou baixe o repositório.

Execute o arquivo .py com Python 3:

bash
Copiar
Editar
python nome_do_arquivo.py
Siga as instruções no terminal.

📚 Possíveis Melhorias Futuras
Interface gráfica (Tkinter, Flask ou web)

Leitura de vagas a partir de um arquivo JSON ou CSV

Sistema de pontuação por relevância (ranking de vagas)

Exportar resultado em PDF ou HTML

👨‍💻 Autor
Felipe Bastos
Estudante de Sistemas de Informação na FIAP
