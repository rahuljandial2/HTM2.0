import { Component } from "react";
import Todo from './todo.js';
import { Redirect } from "react-router";
import { Button } from "@material-ui/core";
import { Link } from "react-router-dom";
import axios from "axios";

class Home extends Component {
  constructor(props) {
    super(props);
    this.handleLogout = this.handleLogout.bind(this);
    this.getTasks = this.getTasks.bind(this);
    this.state = {
      tasks: []
    }
  }
  getTasks() {
    const URL = "http://localhost:8000/api/tasks/";
    const TOKEN = localStorage.getItem('token');
    axios({ method: 'get', url: URL, headers: { "Authorization": `Token ${TOKEN}` } })
      .then(data => {
        this.setState({ tasks: data.data });
      })
      .catch((err) => {
        console.log(err);
      });
  }
  componentDidMount() {
    this.getTasks();
  }
  handleLogout() {
    localStorage.removeItem("token");
    this.forceUpdate();
  }
  render() {
    if (localStorage.getItem("token")) {
      return (
        <div className="Home">
          <nav className="Home-nav">
            <h1 className="Home-nav-title">Whatodo</h1>
            <Link to='/create-task'><Button variant="contained" color="primary">Create Task</Button></Link>
            <Button variant="contained" color="primary" onClick={this.handleLogout}>Log Out</Button>
          </nav>
          <h1 className="Home-title">Todo List</h1>
          <div className="Home-tasks">
            {this.state.tasks.map(task => <Todo key={task.id} task={task} />)}
          </div>
        </div>
      );
    }
    return <Redirect to="/" />
  }
}

export default Home;