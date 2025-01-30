import psycopg

con = psycopg.connect(
    host='200.129.44.249',   
    dbname='496500',         
    user='496500',           
    password='496500'        
)

cur = con.cursor()
try:
cur.execute("""
    SELECT t.codigo, COUNT(at.aluno_id) AS quantidade_alunos
    FROM projetobancodedados.turma t
    LEFT JOIN projetobancodedados.aluno_turma at ON t.id = at.turma_id
    GROUP BY t.codigo;
""")
result_turmas = cur.fetchall()

print("Turmas e Quantidade de Alunos:")
for i in result_turmas:
    print(f"Turma: {i[0]} - Alunos: {i[1]}")

cur.execute("""
    SELECT a.nome
    FROM projetobancodedados.aluno a
    JOIN projetobancodedados.aluno_turma at ON a.id = at.aluno_id
    JOIN projetobancodedados.turma t ON at.turma_id = t.id
    JOIN projetobancodedados.disciplina d ON t.disciplina_id = d.id
    WHERE d.nome = 'Fundamentos de Bancos de Dados';
""")
result_alunos_disciplina = cur.fetchall()

print("\nAlunos matriculados na disciplina 'Fundamentos de Bancos de Dados':")
for i in result_alunos_disciplina:
    print(i[0])

cur.execute("""
    SELECT COUNT(p.id)
    FROM projetobancodedados.professor p
    JOIN projetobancodedados.curso c ON p.curso_id = c.id
    WHERE c.nome = 'Ciências da Computação';
""")
result_qtd_professores = cur.fetchone()

print(f"\nQuantidade de professores do curso 'Ciências da Computação': {result_qtd_professores[0]}")


con.commit()
    print("Consultas realizada com sucesso!")

except Exception as e:
    con.rollback()
    print("Erro ao inserir dados:", e)

finally:
    
cur.close()
con.close()
