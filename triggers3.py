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
        INSERT INTO projetobancodedados.aluno_turma (aluno_id, turma_id) VALUES
        (3, 1),
        (4, 1),
        (5, 1);
    """)
    con.commit()
    print("Dados inseridos com sucesso!")

except Exception as e:
    con.rollback()
    print("Erro ao inserir dados:", e)

finally:
    cur.close()
    con.close()