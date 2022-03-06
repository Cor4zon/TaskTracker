
import APIClient from "../../services/APIClient";
import './ProjectForm.css'

const ProjectUpdateForm = (project) => {
    const client = new APIClient();

    return (
            <div className="input-box">
                <form action="" method="get" className="project-form">
                    <p className="user-box">
                        <input type="text" name="title" id="title" required />
                        <label htmlFor="title">Project title:</label>
                    </p>

                    <button className='submit-btn' type="submit" onClick={() => {
                        const title = document.getElementById('title')

                        // if (
                        //     title.value.trim() === '' ||
                        //     description.value.trim() === '' ||
                        //     deadline.value.trim() === ''
                        // ) {
                        //     alert("incorrect input")
                        //     return ;
                        // }

                        console.log('project ' + project.project)
                        console.log('title ' + title.value)

                        client.updateProject(project.project, title.value);
                    }}>Submit</button>
                </form>
            </div>
        )

}

export default ProjectUpdateForm;