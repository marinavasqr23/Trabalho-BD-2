# Importando Biblioteca
import psycopg

# Conectando Python ao PostgreSQL
con = psycopg.connect(
    host='200.129.44.249',   # Endereço IP do servidor PostgreSQL
    dbname='496500',       # Nome do banco de dados
    user='496500',           # Nome de usuário
    password='496500'        # Senha
)

# Criando um cursor
cur = con.cursor()

# Executando o comando DROP TABLE na tabelas e nas tabelas associadas que precisam ser excluídas

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


# Confirmando a operação
con.commit()  

# Exibindo a mensagem de sucesso
print("Tabela excluída com sucesso!")

# Fechando a conexão
cur.close()
con.close()
