
import { useState } from "react";
import Project from "../Project/Project";
import ProjectForm from '../Project/ProjectForm'

import './ProjectList.css';


const ProjectList = ( { projectList, createProject, DeleteProject, setProjectListVisible }) => {

    const [projectFormVisible, setProjectFormVisible] = useState(false);

    return (
        <div>

            <ProjectForm
                projectFormVisible={projectFormVisible}
                setProjectFormVisible={setProjectFormVisible}
                createProject={createProject}
            />

            <button className="btn-add" onClick={() => {
                setProjectFormVisible(true);
            }}>New</button>


                <ul className="projectList-items">
                    {
                        projectList.map((project, id) => {
                            return (
                                    <li key={id}>
                                            <Project project={ project } DeleteProject={DeleteProject}/>
                                    </li>
                            )
                        })
                    }
                </ul>
        </div>
    )
}

export default ProjectList;