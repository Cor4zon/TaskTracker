
import APIClient from "../../services/APIClient";
import './ProjectForm.css'

const ProjectForm = () => {
    const client = new APIClient();

    return (
            <div className="input-box">
                <form action="" method="get" className="project-form">
                    <p className="user-box">
                        <input type="text" name="title" id="title" required />
                        <label htmlFor="title">Project title:</label>
                    </p>
                    <p className="user-box">
                        <input type="text" name="description" id="description" required />
                        <label htmlFor="description">Project description:</label>
                    </p>
                    <p className="user-box">
                        <input type="text" name="deadline" id="deadline" required />
                        <label htmlFor="deadline">Project deadline:</label>
                    </p>
                    <button className='submit-btn' type="submit" onClick={() => {
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
            </div>
        )

}

export default ProjectForm;