import './Task.css';
import APIClient from "../../services/APIClient";

const Task = ( { task, setTaskList }) => {
    const client = new APIClient();

    return (
        <div className="task">
            <h5 className="task-item__title"> Title: {task.title}</h5>
            <p className="task-item__description"> Description: {task.description}</p>

            <button className="btn-delete" onClick={() => {
                console.log('delete task');
                client.deleteTask(task.project, task.id);

            }}>Delete
            </button>
        </div>
    );
}

export default Task;