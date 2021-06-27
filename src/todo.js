import { Component } from "react";
import { FormControlLabel, Checkbox } from '@material-ui/core';
import axios from "axios";

class Todo extends Component {
  constructor(props) {
    super(props);
    this.handleCheckbox = this.handleCheckbox.bind(this);

    this.state = {
      isCompleted: this.props.task.is_completed
    };
  }
  handleCheckbox() {
    const URL = `http://localhost:8000/api/tasks/${this.props.task.id}/`;
    const TOKEN = localStorage.getItem('token');
    axios({ method: 'put', url: URL, headers: { "Authorization": `Token ${TOKEN}` }, data: { is_completed: !this.state.isCompleted } })
      .then(data => {
        this.setState({ isCompleted: data.data.is_completed })
      })
      .catch((err) => {
        console.log(err);
      });
  }
  render() {
    const task = this.props.task;
    return (
      <div className="Todo">
        <Checkbox
          id={task.id}
          checked={this.state.isCompleted}
          color="primary"
          onChange={this.handleCheckbox}
        />
        <label htmlFor={task.id}>{task.name}</label>
      </div>
    );
  }
}

export default Todo;