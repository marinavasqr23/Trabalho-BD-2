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
        INSERT INTO projetobancodedados.aluno_turma (id_aluno, id_turma) VALUES
        (1, 2),
        (1, 3),
        (1, 4);
    """)

    con.commit()
    print("Dados inseridos com sucesso!")

except Exception as e:
    con.rollback()
    print("Erro ao inserir dados:", e)

finally:
    cur.close()
    con.close()