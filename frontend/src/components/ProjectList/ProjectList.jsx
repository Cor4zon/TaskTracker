
import {useEffect, useState} from "react";
import Project from "../Project/Project";
import ProjectForm from '../Project/ProjectForm'

import './ProjectList.css';


const ProjectList = ( { projectList }) => {

    return (
        <div>
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

export default ProjectList;