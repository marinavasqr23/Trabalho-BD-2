-- Função para verificar o limite de disciplina dos alunos
CREATE OR REPLACE FUNCTION projetobancodedados.limite_disciplinas()
RETURNS TRIGGER AS $$
BEGIN
    -- Verifica se o aluno já está matriculado em 4 ou mais disciplinas no mesmo semestre
    IF (SELECT COUNT(*) 
        FROM projetobancodedados.Aluno_Turma at
        JOIN projetobancodedados.Turma t ON at.turma_id = t.id
        WHERE at.aluno_id = NEW.aluno_id
        AND t.semestre = (SELECT semestre FROM projetobancodedados.Turma WHERE id = NEW.turma_id)
    ) >= 4 THEN
        RAISE EXCEPTION 'Quantidade de disciplinas por semestre excedida';
    END IF;

    -- Retorna o novo registro se o aluno está matriculado em menos de 4 disciplinas
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Trigger para verificar antes da inserção acontecer
CREATE TRIGGER tg_limite_disciplinas
BEFORE INSERT ON projetobancodedados.Aluno_Turma
FOR EACH ROW
EXECUTE FUNCTION projetobancodedados.limite_disciplinas();