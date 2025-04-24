class Vaga:
    def __init__(self, nome, semestre, cursos):
        self.nome = nome
        self.semestre = semestre
        self.cursos = {curso.lower() for curso in cursos}  

    def eh_compativel(self, aluno):
        cursos_em_comum = self.cursos & aluno.cursos
        return aluno.semestre >= self.semestre and len(cursos_em_comum) >= 2

class Aluno:
    def __init__(self, nome, semestre, cursos):
        self.nome = nome
        self.semestre = semestre
        self.cursos = {curso.lower().strip() for curso in cursos} 

todas_vagas = [
    Vaga("Desenvolvedor Backend", 3, ["Python", "SQL", "NoSQL"]),
    Vaga("Desenvolvedor Frontend", 2, ["JavaScript", "React", "CSS"]),
    Vaga("Analista de Dados", 4, ["Python", "SQL", "Power BI"]),
    Vaga("Engenheiro de Software", 5, ["Java", "Spring", "SQL"]),
    Vaga("Administrador de Banco de Dados", 3, ["SQL", "NoSQL", "Shell Script"]),
    Vaga("Cientista de Dados", 5, ["Python", "Machine Learning", "SQL"]),
    Vaga("DevOps Engineer", 4, ["Docker", "Kubernetes", "Shell Script"]),
    Vaga("Cybersecurity Analyst", 3, ["Network Security", "Python", "SIEM"]),
    Vaga("QA Tester", 2, ["Selenium", "Python", "Test Automation"]),
    Vaga("Engenheiro de IA", 6, ["Deep Learning", "Python", "TensorFlow"]),
    Vaga("Desenvolvedor Mobile", 3, ["Flutter", "Dart", "Kotlin"]),
    Vaga("Suporte Técnico", 1, ["Windows", "Linux", "Networking"])
]

# Entrada do usuário
nome_aluno = input("Digite seu nome: ")
semestre_aluno = int(input("Digite seu semestre: "))
cursos_aluno = input("Digite seus cursos separados por vírgula: ").split(",")
aluno = Aluno(nome_aluno, semestre_aluno, cursos_aluno)

# Filtra vagas compatíveis
vagas_compativeis = [vaga for vaga in todas_vagas if vaga.eh_compativel(aluno)]

# Exibição formatada das vagas
if vagas_compativeis:
    print("\nVagas compatíveis para você:")
    print("=" * 75)
    print(f"{'Vaga':<35}{'Semestre Mínimo':<18}{'Cursos Exigidos'}")
    print("=" * 75)
    
    for vaga in vagas_compativeis:
        cursos_formatados = ', '.join(sorted(vaga.cursos))  
        print(f"{vaga.nome:<35}{vaga.semestre:<18}{cursos_formatados}")

    print("=" * 75)
else:
    print("\nNenhuma vaga compatível encontrada.")

