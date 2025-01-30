import psycopg

con = psycopg.connect(
    host='200.129.44.249',   
    dbname='496500',       
    user='496500',           
    password='496500'        
)

cur = con.cursor()


cur.execute("DROP TABLE IF EXISTS projetobancodedados.turma_aluno")
cur.execute("DROP TABLE IF EXISTS projetobancodedados.turma_disciplina")
cur.execute("DROP TABLE IF EXISTS projetobancodedados.projeto_aluno")
cur.execute("DROP TABLE IF EXISTS projetobancodedados.avaliacao_turma")
cur.execute("DROP TABLE IF EXISTS projetobancodedados.nota")
cur.execute("DROP TABLE IF EXISTS projetobancodedados.avaliacao")
cur.execute("DROP TABLE IF EXISTS projetobancodedados.aluno")
cur.execute("DROP TABLE IF EXISTS projetobancodedados.turma_sala")
cur.execute("DROP TABLE IF EXISTS projetobancodedados.professor_turma")
cur.execute("DROP TABLE IF EXISTS projetobancodedados.material_turma")
cur.execute("DROP TABLE IF EXISTS projetobancodedados.projeto_professor")
cur.execute("DROP TABLE IF EXISTS projetobancodedados.disciplina_material")
cur.execute("DROP TABLE IF EXISTS projetobancodedados.materia_professor")
cur.execute("DROP TABLE IF EXISTS projetobancodedados.aluno")
cur.execute("DROP TABLE IF EXISTS projetobancodedados.professor")
cur.execute("DROP TABLE IF EXISTS projetobancodedados.disciplina")
cur.execute("DROP TABLE IF EXISTS projetobancodedados.turma")
cur.execute("DROP TABLE IF EXISTS projetobancodedados.curso")


con.commit()  

print("Tabela excluída com sucesso!")

cur.close()
con.close()