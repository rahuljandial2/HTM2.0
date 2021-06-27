import { Component } from "react";
import { TextField, Button } from "@material-ui/core";
import { Link } from "react-router-dom";
import axios from "axios";
import { Redirect } from "react-router-dom";

class CreateTask extends Component {
  constructor(props) {
    super(props);

    this.state = {
      task: ''
    };
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleTask = this.handleTask.bind(this);
  }
  handleTask(event) {
    this.setState({ task: event.target.value })
  }
  handleSubmit(event) {
    event.preventDefault();
    const URL = "https://todoapi86.azurewebsites.net/api/tasks/";
    const TOKEN = localStorage.getItem('token');
    axios({ method: 'post', url: URL, headers: { "Authorization": `Token ${TOKEN}` }, data: { name: this.state.task } })
      .then(() => {
        console.log(`"${this.state.task}" Task Created`);
        this.setState({ task: "" });
      })
      .catch((err) => {
        console.log(err);
      });
  }
  render() {
    if (localStorage.getItem('token')) {
      return (
        <form className="Login" onSubmit={this.handleSubmit}>
          <h1 className="Login-title">Whatodo</h1>
          <TextField className="Login-input"
            required
            value={this.state.task}
            type="text"
            label="Title"
            variant="outlined"
            onChange={this.handleTask} />
          <div className="Login-btns">
            <Link to='/home-page'><Button color="primary">Back to home</Button></Link>
            <Button variant="contained" color="primary" type="submit">Create task</Button>
          </div>
        </form>
      );
    }
    return <Redirect to="/" />
  }

}

export default CreateTask;