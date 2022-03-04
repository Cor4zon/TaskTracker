
import APIClient from "../../services/APIClient";


const ProjectForm = () => {
    const client = new APIClient();

    return (
            <form action="" method="get" className="project-form">
                <p>
                    <label htmlFor="title">Project title:</label>
                    <input type="text" name="title" id="title" required />
                </p>
                <p>
                    <label htmlFor="description">Project description:</label>
                    <input type="text" name="description" id="description" required />
                </p>
                <p>
                    <label htmlFor="deadline">Project deadline:</label>
                    <input type="text" name="deadline" id="deadline" required />
                </p>
                <button type="submit" onClick={() => {
                    const title = document.getElementById('title')
                    const description = document.getElementById('description')
                    const deadline = document.getElementById('deadline')

                    if (
                        title.value.trim() === '' ||
                        description.value.trim() === '' ||
                        deadline.value.trim() === ''
                    ) {
                        alert("incorrect input")
                        return ;
                    }

                    client.addProject(title.value, description.value, deadline.value);
                }}>Submit</button>
            </form>
        )

}

export default ProjectForm;