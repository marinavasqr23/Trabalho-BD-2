import psycopg

import psycopg

con = psycopg.connect(
    host='200.129.44.249',   
    dbname='496500',       
    user='496500',           
    password='496500'        
)


def executar_consulta(consulta, parametros=None):
    try:
        with con.cursor() as cursor:
            cursor.execute(consulta, parametros)
            return cursor.fetchall()
    except Exception as e:
        print("Erro ao executar consulta:", e)
        return []

# Todas as turmas e a quantidade de alunos participantes de cada turma
consulta_1 = """
    SELECT t.id AS turma_id, t.semestre, COUNT(at.aluno_id) AS quantidade_alunos
    FROM projetobancodedados.turma t
    LEFT JOIN projetobancodedados.aluno_turma at ON t.id = at.turma_id
    GROUP BY t.id, t.semestre
    ORDER BY t.id;
"""

# Alunos matriculados na disciplina de “Fundamentos de Bancos de Dados”
consulta_2 = """
    SELECT a.nome 
    FROM projetobancodedados.aluno a
    JOIN projetobancodedados.aluno_turma at ON a.id = at.aluno_id
    JOIN projetobancodedados.turma t ON at.turma_id = t.id
    JOIN projetobancodedados.disciplina d ON t.disciplina_id = d.id
    WHERE d.nome = 'Fundamentos de Bancos de Dados';
"""

# 3. Quantidade de professores do curso de “Ciências da Computação”
consulta_3 = """
    SELECT COUNT(DISTINCT p.id) 
    FROM projetobancodedados.professor p
    JOIN projetobancodedados.turma t ON p.id = t.prof_id
    JOIN projetobancodedados.disciplina d ON t.disciplina_id = d.id
    JOIN projetobancodedados.curso c ON d.curso_id = c.id
    WHERE c.nome = 'Ciências da Computação';
"""

# Executando as consultas e exibindo os resultados 
print("1. Todas as turmas e a quantidade de alunos participantes:")
for resultado in executar_consulta(consulta_1):
    print(f"Turma ID: {resultado[0]}, Semestre: {resultado[1]}, Quantidade de alunos: {resultado[2]}")

print("\n2. Alunos matriculados na disciplina 'Fundamentos de Bancos de Dados':")
for resultado in executar_consulta(consulta_2):
    print(f"Aluno: {resultado[0]}")

print("\n3. Quantidade de professores do curso 'Ciências da Computação':")
print(f"Quantidade de professores: {executar_consulta(consulta_3)[0][0]}")
