import { Component } from "react";
import Todo from './todo.js';

class Home extends Component {
  render() {
    return (
      <div className="Home">
        <h1>Todo List</h1>
        <Todo />
      </div>
    );
  }
}

export default Home;