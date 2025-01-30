
import psycopg

con = psycopg.connect(
    host='200.129.44.249',   
    dbname='496500',         
    user='496500',           
    password='496500'        
)

cur = con.cursor()
# Chamando procedimento inc_semeste com p_semestre=1
try:
    cur.execute("CALL projetobancodedados.inc_semestre(1);") 
    con.commit()
    print("Semestres atualizados com sucesso!")

except Exception as e:
    con.rollback()
    print("Erro durante a execução do procedimento:", e)

finally:
    cur.close()
    con.close()
