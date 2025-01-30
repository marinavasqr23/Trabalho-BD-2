import psycopg

# Conexão com o banco de dados
con = psycopg.connect(
    host='200.129.44.249',   
    dbname='496500',        
    user='496500',           
    password='496500'        
)

cur = con.cursor()

try:
    # Criação das tabelas
    cur.execute("""
        CREATE TABLE IF NOT EXISTS projetobancodedados.curso (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            regime VARCHAR(100) NOT NULL,
            duracao INT NOT NULL
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS projetobancodedados.aluno (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            curso_id INT NOT NULL,
            semestre INT NOT NULL,
            FOREIGN KEY (curso_id) REFERENCES projetobancodedados.curso(id)
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS projetobancodedados.professor (
            id SERIAL PRIMARY KEY,  -- Alterado para SERIAL
            nome VARCHAR(100) NOT NULL,
            area_especializacao VARCHAR(100) NOT NULL,
            contato VARCHAR(100),
            curso_id INT,
            FOREIGN KEY (curso_id) REFERENCES projetobancodedados.curso(id)
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS projetobancodedados.disciplina (
            id SERIAL PRIMARY KEY,  -- Alterado para SERIAL
            codigo VARCHAR(10) UNIQUE NOT NULL,
            nome VARCHAR(100) NOT NULL,
            area_especializacao VARCHAR(100) NOT NULL,
            carga_horaria INT NOT NULL,
            curso_id INT,
            FOREIGN KEY (curso_id) REFERENCES projetobancodedados.curso(id)
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS projetobancodedados.turma (
            id SERIAL PRIMARY KEY,  -- Alterado para SERIAL
            codigo VARCHAR(10) UNIQUE NOT NULL,
            disciplina_id INT,
            semestre VARCHAR(20) NOT NULL,
            capacidade_maxima INT NOT NULL,
            estado VARCHAR(20) NOT NULL,
            prof_id INT,
            FOREIGN KEY (disciplina_id) REFERENCES projetobancodedados.disciplina(id),
            FOREIGN KEY (prof_id) REFERENCES projetobancodedados.professor(id)
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS projetobancodedados.aluno_turma (
            aluno_id INT,
            turma_id INT,
            PRIMARY KEY (aluno_id, turma_id),
            FOREIGN KEY (aluno_id) REFERENCES projetobancodedados.aluno(id),
            FOREIGN KEY (turma_id) REFERENCES projetobancodedados.turma(id)
        );
    """)

    con.commit()
    print("Tabelas criadas com sucesso!")

except Exception as e:
    con.rollback()
    print("Erro ao criar tabelas:", e)

finally:
    cur.close()
    con.close()
