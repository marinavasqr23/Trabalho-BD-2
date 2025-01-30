--- Função para verificar status da turma
CREATE OR REPLACE FUNCTION projetobancodedados.status_turma()
RETURNS TRIGGER AS $$
BEGIN
    -- Verifica se a turma atingiu a capacidade máxima 
    IF (SELECT COUNT(*) FROM projetobancodedados.aluno_turma WHERE turma_id = NEW.turma_id) >=
       (SELECT capacidade_maxima FROM projetobancodedados.Turma WHERE id = NEW.turma_id) THEN
        RAISE EXCEPTION 'Capacidade máxima da turma atingida.';
    END IF;
    
    -- Retorna o novo registro caso a capacidade não tenha sido atingida
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;


-- Trigger para verificar antes da inserção acontecer
CREATE TRIGGER tg_status_turma
BEFORE INSERT ON projetobancodedados.aluno_turma
FOR EACH ROW
EXECUTE FUNCTION projetobancodedados.status_turma();