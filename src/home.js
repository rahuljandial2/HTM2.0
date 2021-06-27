import { Component } from "react";
import Todo from './todo.js';
import { Redirect } from "react-router";

class Home extends Component {
  constructor(props) {
    super(props);
    this.handleLogout = this.handleLogout.bind(this);
  }
  handleLogout() {
    localStorage.removeItem("token");
    this.forceUpdate();
  }
  render() {
    if (localStorage.getItem("token")) {
      return (
        <div className="Home">
          <button onClick={this.handleLogout}>Log Out</button>
          <h1>Todo List</h1>
          <Todo />
        </div>
      );
    }
    return <Redirect to="/" />
  }
}

export default Home;