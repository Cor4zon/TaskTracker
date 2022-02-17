import React, { useState, useEffect } from "react";
import Modal from "./components/Modal";
import axios from 'axios';

const App = () => {

	const [activeItem, setActiveItem] = useState({title: "", description: "", deadline: ""});
	const [projectList, setProjectList] = useState([]);
	const [modal, setModal] = useState(null);

	useEffect(() => {
		refreshList();
	})


	const refreshList = () => {
		const apiUrl = "http://localhost:8000/api/v1/projects/";
		axios.get(apiUrl).then(res => {
				// this.setState({ projectList: res.data });
				setProjectList(res.data);
				console.log(res.data);
			}).catch(err => console.log(err));
	};


	const renderProjectList = () => {
		const projectItems = projectList;

		return (
			projectItems.map((item) => (
				<li key={item.id} className="list-group-item">
					{ item.title }
					{ item.description }
					{ item.deadline }

					<button
						onClick={() => editItem(item)}
						className="btn btn-secondary mr-2"
					> Edit </button>

					<button
						onClick={() => handleDelete(item)}
						className="btn btn-danger">
					Delete </button>
				</li>
			))
		)
	}

	const toggle = () => {
		//add this after modal creation
		setModal(!modal);
	};

	// handleSubmit = (item) => {
	// 	this.toggle();
	// 	alert("save" + JSON.stringify(item));
	// };

	// Submit an item
	const handleSubmit = (item) => {
		toggle();

		if (item.id) {
			// if old post to edit and submit
			axios.put(`http://localhost:8000/api/v1/projects/${item.id}/`, item).then((res) => refreshList());
			return;
		}
		// if new post to submit
		axios
		.post("http://localhost:8000/api/v1/projects/", item)
		.then((res) => this.refreshList());
	};

	const handleDelete = (item) => {
		axios.delete(`http://localhost:8000/api/v1/projects/${item.id}/`).then((res) => refreshList());
		alert("delete" + JSON.stringify(item));
	};


	// Create item
	const createItem = () => {
		const item = { title: "", description: "" };
		setActiveItem(item);
		setModal(!modal);
	};

	//Edit item
	const editItem = (item) => {
		setActiveItem(item);
		setModal(!modal);
	};


	return (
		<main className="content">
			<h1 className="text-success text-uppercase text-center my-4">
			 Task Tracker
			</h1>
			<div className="row ">
			<div className="col-md-6 col-sm-10 mx-auto p-0">
				<div className="card p-3">
					<div className="">
						<button onClick={createItem} className="btn btn-info">
						Add task
						</button>
					</div>

					{/*{this.renderTabList()}*/}
					<ul className="list-group list-group-flush">
						{renderProjectList()}
					</ul>
				</div>
			</div>
			</div>

			{modal ? (
			<Modal
				activeItem={activeItem}
				toggle={toggle}
				onSave={handleSubmit}
			/>
			) : null}
		</main>
	);
}


export default App;
