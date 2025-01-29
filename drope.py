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

cur.execute( SELECT t.id AS turma_id, 
    t.semestre, 
    COUNT(a.id) AS quantidade_alunos
FROM Turma t
LEFT JOIN Aluno_Turma at ON t.aluno_id = at.turma_id
LEFT JOIN Aluno a ON at.id_aluno = a.id
GROUP BY t.id, t.semestre
ORDER BY t.id;
)


# Confirmando a operação
con.commit()  

# Exibindo a mensagem de sucesso
print("Tabela excluída com sucesso!")

# Fechando a conexão
cur.close()
con.close()
