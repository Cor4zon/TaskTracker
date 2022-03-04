
import {useEffect, useState} from "react";
import Project from "../Project/Project";
import ProjectForm from '../Project/ProjectForm'

import './ProjectList.css';


const ProjectList = ( { projectList }) => {

    const [projectFormVisible, setProjectFormVisible] = useState(false);

    if (projectFormVisible) {
        return (
            <div>
                <ProjectForm />
            </div>
        )
    } else {
        return (
            <div>
                <button className="btn-create" onClick={() => {
                    console.log("create project");
                    setProjectFormVisible(true);
                }}>Add</button>

                 <ul className="projectList-items">
                        {
                            projectList.map((project, id) => {
                                return (
                                        <li key={id}>
                                                <Project project={ project } />
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