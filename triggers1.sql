-- Função para verificar o status da turma
CREATE OR REPLACE FUNCTION projetobancodedados.status_turma()
RETURNS TRIGGER AS $$
DECLARE -- Declarando as variáveis
    capacidade_maxima INT;
    total_matriculados INT;
BEGIN
    SELECT capacidade_maxima INTO capacidade_maxima -- Pega capacidade e armazena na variavel 
    FROM Turma
    WHERE id = NEW.turma_id; 

    SELECT COUNT(*) INTO total_matriculados -- Pega o total de alunos de cada turma 
    FROM Aluno_Turma
    WHERE turma_id = NEW.turma_id;

    -- Verificando se a sala está cheia
    IF total_matriculados >= capacidade_maxima THEN
        RAISE EXCEPTION 'A turma atingiu sua capacidade máxima!';
    END IF;

    RETURN NEW; -- Seguindo com a inserção se a turma não atingir a capacidade máxima
END;
$$ LANGUAGE plpgsql;

-- Gatinho antes de cada insert na tabela aluno_turma
CREATE TRIGGER trg_capacidade
BEFORE INSERT ON projetobancodedados.Aluno_Turma
FOR EACH ROW
EXECUTE FUNCTION projetobancodedados.status_turma();


