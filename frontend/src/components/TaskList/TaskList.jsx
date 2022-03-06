
import APIClient from "../../services/APIClient";
import Task from "../Task/Task"

const TaskList = ({ taskList, setTaskList }) => {
    const client = new APIClient();

    return (
        <div>
             <ul className="tasksList-items">
                    {
                        taskList.map((task, id) => {
                            return (
                                    <li key={id}>
                                            <Task task={ task } setTaskList={setTaskList}/>
                                    </li>
                            )
                        })
                    }
                </ul>
        </div>
    )
}

export default TaskList;