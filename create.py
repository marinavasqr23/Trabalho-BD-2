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