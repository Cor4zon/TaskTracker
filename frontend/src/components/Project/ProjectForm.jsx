


const ProjectForm = ({ projectFormVisible, setProjectFormVisible, createProject }) => {

    if (projectFormVisible) {
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

                        const project = {
                            title: title.value,
                            description: description.value,
                            deadline: deadline.value
                        }

                        createProject(project);

                        setProjectFormVisible(false);
                    }}>Submit</button>
                </form>
            )
    }
    return (
        <div></div>
    )
}

export default ProjectForm;