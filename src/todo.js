import { Component } from "react";
import { FormControlLabel, Checkbox } from '@material-ui/core';

class Todo extends Component {
  render() {
    const task = this.props.task;
    return (
      <div className="Todo">
        <FormControlLabel
          control={
            <Checkbox
              checked={task.is_completed}
              name="checkedB"
              color="primary"
            />
          }
          label={task.name}
        />
      </div>
    );
  }
}

export default Todo;