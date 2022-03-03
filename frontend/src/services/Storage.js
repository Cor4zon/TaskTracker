"use strict";

class Storage {
    constructor(storage) {
        this.storage = storage;
    }

    get(key) {
        this.storage.getItem(key);
    }

    set(key, value) {
        this.storage.set(key, value);
    }

    remove(key) {
        this.storage.removeItem(key);
    }

    clear() {
        this.storage.clear();
    }
}

export default Storage;