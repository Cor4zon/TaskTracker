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
    }, [client]);

    return (
        <main className="app">
            <ProjectList projectList={projectList} />
        </main>
    )
}

export default App;