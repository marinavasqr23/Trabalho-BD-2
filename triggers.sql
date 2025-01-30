-- Gatilho 1 - Capacidade máxima da turma
CREATE OR REPLACE FUNCTION verifica_capacidade_turma()
RETURNS TRIGGER AS $$
BEGIN
    
    IF (SELECT COUNT(*) FROM Aluno_Turma WHERE turma_id = NEW.turma_id) >= 
       (SELECT capacidade_maxima FROM Turma WHERE id = NEW.turma_id) THEN
        RAISE EXCEPTION 'Capacidade máxima da turma atingida.';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER tg_verifica_capacidade_turma
BEFORE INSERT ON Aluno_Turma
FOR EACH ROW
EXECUTE FUNCTION verifica_capacidade_turma();

-- Gatilho 2 - Limite de disciplinas por semestre
CREATE OR REPLACE FUNCTION verifica_limite_disciplinas()
RETURNS TRIGGER AS $$
BEGIN
    
    IF (SELECT COUNT(*) FROM Aluno_Turma at\n
        JOIN Turma t ON at.turma_id = t.id\n
        WHERE at.aluno_id = NEW.aluno_id AND t.semestre = (SELECT semestre FROM Turma WHERE id = NEW.turma_id)) >= 4 THEN
        RAISE EXCEPTION 'Quantidade de disciplinas por semestre excedida';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER tg_verifica_limite_disciplinas
BEFORE INSERT ON Aluno_Turma
FOR EACH ROW
EXECUTE FUNCTION verifica_limite_disciplinas();
