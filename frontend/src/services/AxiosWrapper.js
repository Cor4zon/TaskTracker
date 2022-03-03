"use strict";

import axios from "axios";

class AxiosWrapper {
    constructor(path) {
        this.path = path;
    }

    get() {
        return Promise.resolve(
            axios.get( this.path )
        )
    }

    post(data) {
        return Promise.resolve(
            axios.post(
                this.path,
                data,
                )
        )
    }

    delete() {
        return Promise.resolve(
            axios.delete( this.path )
        )
    }

    patch(data) {
        return Promise.resolve(
            axios.patch(
                this.path,
                data,
                )
        )
    }
}

export default AxiosWrapper;