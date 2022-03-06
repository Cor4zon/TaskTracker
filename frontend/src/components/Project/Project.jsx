import './Project.css';
import APIClient from "../../services/APIClient";
import {useEffect, useState} from "react";
import TaskList from "../TaskList/TaskList";

const Project = ( { project, setProjectUpdateFormVisible }) => {
    const client = new APIClient();
    const [taskList, setTaskList] = useState([]);

    if (!taskList.length) {
        return (
            <div className="project-item">
                <h5 className="project-item__title"> Title: {project.title}</h5>
                <p className="project-item__description"> Description: {project.description}</p>

                <button className="btn-edit" onClick={() => {
                    setProjectUpdateFormVisible(project.id);
                }}>Edit
                </button>

                <button className="btn-delete" onClick={() => {
                    console.log("delete project");
                    client.deleteProject(project.id)
                }}>Delete
                </button>

                <button className="btn-tasks" onClick={() => {
                    if (taskList.length) {
                        setTaskList([])
                    } else {
                        client.fetchTasks(project.id).then((result) => {
                        setTaskList(result.data);
                        });
                        console.log(taskList);
                    }
                }}>Tasks
                </button>

            </div>
        );
    } else {
        return(
            <div>
                <div className="project-item">
                <h5 className="project-item__title"> Title: {project.title}</h5>
                <p className="project-item__description"> Description: {project.description}</p>

                <button className="btn-edit" onClick={() => {
                    // handleUpdateProject(project.id);
                    console.log("handleUpdateProject");
                }}>Edit
                </button>

                <button className="btn-delete" onClick={() => {
                    console.log("delete project");
                    client.deleteProject(project.id)
                }}>Delete
                </button>

                <button className="btn-tasks" onClick={() => {
                    if (taskList.length) {
                        setTaskList([])
                    } else {
                        client.fetchTasks(project.id).then((result) => {
                        setTaskList(result.data);
                        });
                        console.log(taskList);
                    }
                }}>Tasks
                </button>

            </div>
                <TaskList taskList={taskList} setTaskList={setTaskList}/>
        </div>
        )
    }
}

export default Project;