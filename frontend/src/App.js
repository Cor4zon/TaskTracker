import React, { Component, useState } from "react";
import Modal from "./components/Modal";
import axios from 'axios';

class App extends Component {

	constructor(props) {
		super(props);

		this.state = {

		activeItem: {
			title: "",
			description: "",
			deadline: "",
		},

		projectList: [],
		};
	}

	// const [projectList, setProjectList] = useState([])

	// Lifecycle method
	componentDidMount() {
		this.refreshList();
	}


	refreshList = () => {
		const apiUrl = "http://localhost:8000/api/v1/projects/";
		axios.get(apiUrl).then(res => {
				this.setState({ projectList: res.data });
				console.log(res.data);
			}).catch(err => console.log(err));
	};


	renderProjectList = () => {
		const projectItems = this.state.projectList;

		return (
			projectItems.map((item) => (
				<li key={item.id} className="list-group-item">
					{ item.title }
					{ item.description }
					{ item.deadline }

					<button
						onClick={() => this.editItem(item)}
						className="btn btn-secondary mr-2"
					> Edit </button>

					<button
						onClick={() => this.handleDelete(item)}
						className="btn btn-danger">
					Delete </button>
				</li>
			))
		)
	}

	toggle = () => {
		//add this after modal creation
		this.setState({ modal: !this.state.modal });
	};

	handleSubmit = (item) => {
		this.toggle();
		alert("save" + JSON.stringify(item));
	};

	// Submit an item
	handleSubmit = (item) => {
		this.toggle();

		if (item.id) {
		// if old post to edit and submit
		axios.put(`http://localhost:8000/api/v1/projects/${item.id}/`, item).then((res) => this.refreshList());
		return;
		}
		// if new post to submit
		axios
		.post("http://localhost:8000/api/v1/projects/", item)
		.then((res) => this.refreshList());
	};

	handleDelete = (item) => {
		axios.delete(`http://localhost:8000/api/v1/projects/${item.id}/`).then((res) => this.refreshList());
		alert("delete" + JSON.stringify(item));
	};


	// Create item
	createItem = () => {
		const item = { title: "", description: "" };
		this.setState({ activeItem: item, modal: !this.state.modal });
	};

	//Edit item
	editItem = (item) => {
		this.setState({ activeItem: item, modal: !this.state.modal });
	};


	render() {
		return (
		<main className="content">
			<h1 className="text-success text-uppercase text-center my-4">
			 Task Tracker
			</h1>
			<div className="row ">
			<div className="col-md-6 col-sm-10 mx-auto p-0">
				<div className="card p-3">
					<div className="">
						<button onClick={this.createItem} className="btn btn-info">
						Add task
						</button>
					</div>

					{/*{this.renderTabList()}*/}
					<ul className="list-group list-group-flush">
						{this.renderProjectList()}
					</ul>
				</div>
			</div>
			</div>

			{this.state.modal ? (
			<Modal
				activeItem={this.state.activeItem}
				toggle={this.toggle}
				onSave={this.handleSubmit}
			/>
			) : null}
		</main>
		);
	}
}

export default App;
