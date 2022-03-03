import axios from "axios";
import React, { useState, useEffect } from 'react';
import ProjectList from "./components/ProjectList/ProjectList";
import APIClient from "./services/APIClient";

const App = () => {

    const [ projectList, setProjectList ] = useState([]);
    const client = new APIClient();

    useEffect(() => {
        client.fetchProjects().then((result) => {
            setProjectList(result.data);
        });
    }, []);

    // const createProject = (project) => {
    //
    //     axios.post('http://localhost:8000/api/v1/projects/', {
    //         title: project.title,
    //         description: project.description,
    //         deadline: project.deadline
    //     }).then((response) => {
    //         projectList = [...projectList, response.data]
    //         setProjectList(projectList);
    //   });
    // }

    // const DeleteProject = (id) => {
    //         axios.delete(`http://localhost:8000/api/v1/projects/${id}/`).then((response) => {
    //             setProjectList(projectList.filter(project => project.id !== id));
    //         });
    //         alert(`you delete ${id} project.`);
    // }


    return (
        <main>
            <ProjectList projectList={projectList} />
        </main>
    )


}

export default App;