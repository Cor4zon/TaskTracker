import axios from "axios";

const URL = 'http://localhost:8000/api/v1/projects/';


export const getProjects = async () => {
    try {
        const { projects: { projects } } = await axios.get(URL);

        return projects;
    } catch (error) {
        console.log(error);
    }
};