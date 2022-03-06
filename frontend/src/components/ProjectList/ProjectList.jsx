import {useEffect, useState} from "react";
import Project from "../Project/Project";
import ProjectForm from '../Project/ProjectForm'
import ProjectUpdateForm from "../Project/ProjectUpdateForm";
import './ProjectList.css';

const ProjectList = ( { projectList }) => {

    const [projectFormVisible, setProjectFormVisible] = useState(false);
    const [projectUpdateFormVisible, setProjectUpdateFormVisible] = useState(0);

    if (projectFormVisible) {
        return (
            <div>
                <ProjectForm />
            </div>
        )
    } else if (projectUpdateFormVisible) {
        return (
            <div>
                <ProjectUpdateForm project={projectUpdateFormVisible}/>
            </div>
        )
    } else {
        return (
            <div>
                <button className="btn-create" onClick={() => {
                    setProjectFormVisible(true);
                }}>Add</button>

                 <ul className="projectList-items">
                        {
                            projectList.map((project, id) => {
                                return (
                                        <li key={id}>
                                                <Project project={ project } setProjectUpdateFormVisible={setProjectUpdateFormVisible} />
                                        </li>
                                )
                            })
                        }
                    </ul>
            </div>
        )
    }
}

export default ProjectList;