import psycopg

# Conectar ao banco de dados
con = psycopg.connect(
    host='200.129.44.249',
    dbname='496500',
    user='496500',
    password='496500'
)

# Função para executar uma transação
def executar_transacao():
    try:
        with con.cursor() as cursor:
            # Iniciar transação
            cursor.execute("BEGIN;")
            
            # 1. Atualizar o estado da turma "CC2024DS1" para "Fechado"
            cursor.execute("""
                UPDATE projetobancodedados.turma
                SET estado = 'Fechado'
                WHERE codigo = 'CC2024DS1';
            """)
            
            # 2. Remover todas as matrículas de alunos na turma "CC2024DS1"
            cursor.execute("""
                DELETE FROM projetobancodedados.aluno_turma
                WHERE turma_id = (SELECT id FROM projetobancodedados.turma WHERE codigo = 'CC2024DS1');
            """)
            
            # Confirmar as alterações (commit)
            con.commit()
            print("Transação realizada com sucesso!")
    
    except Exception as e:
        # Se algo der errado, reverter as alterações (rollback)
        con.rollback()
        print("Erro na transação. Todas as alterações foram revertidas:", e)

# Executando a transação
executar_transacao()
