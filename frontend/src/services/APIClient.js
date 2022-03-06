"use strict";

import AxiosWrapper from "./AxiosWrapper";
import Storage from "./Storage";

class APIClient {
    constructor() {
        this.storage = new Storage(window.localStorage)
    }

    fetchProjects() {
        const wrapper = new AxiosWrapper('http://localhost:8000/api/v1/projects/');
        return Promise.resolve(
            wrapper.get()
                .catch((error) => {
                    this.storage.clear();
                    console.error(error);
                    return Promise.reject(error);
            })
        )
    }

    addProject(title, description, deadline) {
        const wrapper = new AxiosWrapper('http://localhost:8000/api/v1/projects/');
        if (title.length > 0 && description.length > 0) {
            return Promise.resolve(
                wrapper.post(
                    {
                        title: title,
                        description: description,
                        deadline: deadline,
                    }
                ).catch((error) => console.error(error.response) )
            )
        } else {
            return Promise.reject("Please, enter information");
        }
    }

    deleteProject(id) {
        const wrapper = new AxiosWrapper('http://localhost:8000/api/v1/projects/' + id);
        return Promise.resolve(
            wrapper.delete().catch((error) => {
                console.error(error);
                return Promise.reject(error);
            })
        )
    }

    fetchTasks(projectId) {
        const wrapper = new AxiosWrapper('http://localhost:8000/api/v1/projects/' + projectId + '/tasks');
        return Promise.resolve(
            wrapper.get()
                .catch((error) => {
                    this.storage.clear();
                    console.error(error);
                    return Promise.reject(error);
            })
        )
    }

    deleteTask(projectId, taskId) {
        const wrapper = new AxiosWrapper('http://localhost:8000/api/v1/projects/' + projectId + '/tasks/' + taskId);
        return Promise.resolve(
            wrapper.delete().catch((error) => {
                console.error(error);
                return Promise.reject(error);
            })
        )
    }

    updateProject(projectId, title) {
        const wrapper = new AxiosWrapper('http://localhost:8000/api/v1/projects/' + projectId + '/');
        if (title.length > 0) {
            return Promise.resolve(
                wrapper.patch(
                    {
                        title: title,
                    }
                ).catch((error) => console.error(error.response) )
            )
        } else {
            return Promise.reject("Please, enter information");
        }
    }
}

export default APIClient;