CREATE OR REPLACE FUNCTION verificar_capacidade_turma()
RETURNS TRIGGER AS $$
BEGIN
    -- Verifica o número de alunos matriculados na turma
    IF (SELECT COUNT(*) FROM projetobancodedados.aluno_turma WHERE turma_id = NEW.turma_id) >= 
       (SELECT capacidade_maxima FROM projetobancodedados.turma WHERE id = NEW.turma_id) THEN
        RAISE EXCEPTION 'A turma já atingiu a capacidade máxima de alunos.';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Criar o gatilho
CREATE TRIGGER trg_verificar_capacidade_turma
AFTER INSERT ON projetobancodedados.aluno_turma
FOR EACH ROW
EXECUTE FUNCTION verificar_capacidade_turma();




CREATE OR REPLACE FUNCTION verificar_limite_disciplina()
RETURNS TRIGGER AS $$
BEGIN
    -- Verifica o número de disciplinas que o aluno já está matriculado no semestre atual
    IF (SELECT COUNT(*) FROM projetobancodedados.aluno_turma at
        JOIN projetobancodedados.turma t ON at.turma_id = t.id
        WHERE at.aluno_id = NEW.aluno_id AND t.semestre = NEW.semestre) >= 4 THEN
        RAISE EXCEPTION 'O aluno não pode cursar mais de 4 disciplinas no semestre.';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Criar o gatilho
CREATE TRIGGER trg_verificar_limite_disciplina
BEFORE INSERT ON projetobancodedados.aluno_turma
FOR EACH ROW
EXECUTE FUNCTION verificar_limite_disciplina();
