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
        (1, 2), (1, 3), (1, 4);
    """)
    con.commit()
    print("Aluno 1 matriculado em disciplinas com sucesso.")
except Exception as e:
    con.rollback()
    print("Erro ao matricular o aluno 1 em disciplinas:", e)

cur.close()
con.close()
