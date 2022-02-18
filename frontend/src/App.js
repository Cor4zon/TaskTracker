import axios from "axios";


import React, { useState, useEffect } from 'react';
import ProjectList from "./components/ProjectList/ProjectList";


const App = () => {
    let [ projectList, setProjectList ] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:8000/api/v1/projects/').then((response) => {
            // console.log(response.data);
            setProjectList(response.data);

        });
    }, []);

    const createProject = (project) => {

        axios.post('http://localhost:8000/api/v1/projects/', {
            title: project.title,
            description: project.description,
            deadline: project.deadline
        }).then((response) => {
            projectList = [...projectList, response.data]
            setProjectList(projectList);
      });
    }

    const DeleteProject = (id) => {
            axios.delete(`http://localhost:8000/api/v1/projects/${id}/`).then((response) => {
                setProjectList(projectList.filter(project => project.id != id));
            });
            alert(`you delete ${id} project.`);
    }

    const UpdateProject = (id) => {
        return ;
    }

    return (
        <main>
            <ProjectList
                projectList={projectList}
                createProject={createProject}
                DeleteProject={DeleteProject}
            />
        </main>
    )
}

export default App;