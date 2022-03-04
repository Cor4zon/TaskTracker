import './Project.css';
import APIClient from "../../services/APIClient";

const Project = ( { project }) => {
    const client = new APIClient();

    return (
        <div className="project-item">
            <h5 className="project-item__title"> Title: {project.title }</h5>
            <p className="project-item__description"> Description: {project.description }</p>

            <button className="btn-edit" onClick={() => {
                 // handleUpdateProject(project.id);
                console.log("handleUpdateProject");
             }} >Edit</button>

            <button className="btn-delete" onClick={() => {
                console.log("delete project");
                client.deleteProject(project.id)
            }}>Delete</button>
        </div>
    );
}

export default Project;