import { Component } from "react";
import { Button, TextField } from "@material-ui/core";

class Login extends Component {
  render() {
    return (
      <form className="Login" action="">
        <h1 className="Login-title">Todo</h1>
        <TextField className="Login-input" label="Username" variant="outlined" />
        <TextField className="Login-input" label="Password" variant="outlined" />
        <div className="Login-btn">
          <Button className="register" color="primary">Register</Button>
          <Button className="Login" variant="contained" color="primary">Login</Button>
        </div>
      </form>
    );
  }
}

export default Login;