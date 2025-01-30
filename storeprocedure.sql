
-- Criando procedimento inc_semestre 
CREATE OR REPLACE PROCEDURE inc_semestre(p_semestre INT) 
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE projetobancodedados.aluno
    SET semestre = semestre + 1
    WHERE semestre = p_semestre;
END;
$$;
