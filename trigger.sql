CREATE OR REPLACE FUNCTION update_tasks_counter()
RETURNS TRIGGER AS
$$
DECLARE update_count INT;
BEGIN

	IF tg_op = 'INSERT' THEN
		SELECT COUNT(*) INTO update_count
		FROM tasks_task
		WHERE project_id = new.project_id;

		UPDATE tasks_project
		SET "tasksCount" = update_count
		WHERE tasks_project.id = new.project_id;

	ELSIF tg_op = 'DELETE' THEN
		SELECT COUNT(*) INTO update_count
		FROM tasks_task
		WHERE project_id = old.project_id;

		UPDATE tasks_project
		SET "tasksCount" = update_count
		WHERE tasks_project.id = old.project_ID;
	END IF;
	RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER count_trigger
AFTER INSERT OR DELETE
ON tasks_task
FOR EACH ROW
EXECUTE PROCEDURE update_tasks_counter();