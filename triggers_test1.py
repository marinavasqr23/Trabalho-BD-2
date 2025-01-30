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
        INSERT INTO Aluno_Turma (aluno_id, turma_id) VALUES
        (3, 1), (5, 1), (4, 1);
    """)
    con.commit()
    print("Alunos inseridos com sucesso na Turma 1.")
except Exception as e:
    con.rollback()
    print("Erro ao inserir alunos na Turma 1:", e)

cur.close()
con.close()
