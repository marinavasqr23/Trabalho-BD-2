CREATE OR REPLACE PROCEDURE inc_semestre(p_semestre INT)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Atualiza o semestre dos alunos que estão no semestre fornecido
    UPDATE projetobancodedados.aluno
    SET semestre = semestre + 1
    WHERE semestre = p_semestre;
END;
$$;
