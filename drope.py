# Importando Biblioteca
import psycopg2

# Conectando Python ao PostgreSQL
con = psycopg2.connect(
    host='200.129.44.249',   # Endereço IP do servidor PostgreSQL
    database='496500',       # Nome do banco de dados
    user='496500',           # Nome de usuário
    password='496500'        # Senha
)

# Criando um cursor
cur = con.cursor()

# Executando o comando DROP TABLE na tabelas e nas tabelas associadas
# cur.execute("DROP TABLE IF EXISTS projetobancodedados.turma_aluno")
# cur.execute("DROP TABLE IF EXISTS projetobancodedados.turma_disciplina")
# cur.execute("DROP TABLE IF EXISTS projetobancodedados.projeto_aluno")
# cur.execute("DROP TABLE IF EXISTS projetobancodedados.avaliacao_turma")
# cur.execute("DROP TABLE IF EXISTS projetobancodedados.nota")
# cur.execute("DROP TABLE IF EXISTS projetobancodedados.avaliacao")
cur.execute("DROP TABLE IF EXISTS projetobancodedados.aluno")

# Confirmando a operação
con.commit()  # Isso garante que a operação de exclusão seja confirmada no banco

# Exibindo a mensagem de sucesso
print("Tabela excluída com sucesso!")

# Fechando a conexão
cur.close()
con.close()
