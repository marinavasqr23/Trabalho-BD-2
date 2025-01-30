import psycopg

con = psycopg.connect(
    host='200.129.44.249',   
    dbname='496500',         
    user='496500',           
    password='496500'        
)

cur = con.cursor()

try:
    cur.execute("BEGIN;")

    cur.execute("""
        UPDATE projetobancodedados.turma
        SET estado = 'Fechado'
        WHERE codigo = 'CC2024DS1';
    """)

    cur.execute("""
        DELETE FROM projetobancodedados.aluno_turma
        WHERE turma_id = (SELECT id FROM projetobancodedados.turma WHERE codigo = 'CC2024DS1');
    """)

    con.commit()
    print("Transação concluída com sucesso!")

except Exception as e:
    con.rollback()
    print("Erro durante a transação:", e)

finally:
    cur.close()
    con.close()