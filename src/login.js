import { Component } from "react";
import { Button, TextField } from "@material-ui/core";
import axios from "axios";

class Login extends Component {
  constructor(props) {
    super(props);

    this.login = this.login.bind(this);
    this.handleUsername = this.handleUsername.bind(this);
    this.handlePassword = this.handlePassword.bind(this);
    this.state = {
      username: "",
      password: ""
    };
  }

  handleUsername(event) {
    this.setState({
      username: event.target.value
    });
  }
  handlePassword(event) {
    this.setState({
      password: event.target.value
    });
  }
  async login() {
    const url = "http://localhost:8000/api/auth-token/";
    const params = {
      username: this.state.username,
      password: this.state.password,
    };
    axios.post(url, params)
      .then(data => {
        const token = data.data.token;
        console.log(token);
        localStorage.setItem("token", token);
      })
      .catch(() => {
        console.log("Something went wrong on token url!!!");
      });
  }
  render() {
    return (
      <form className="Login hide" onSubmit={this.login}>
        <h1 className="Login-title">Todo</h1>
        <TextField className="Login-input"
          value={this.state.username}
          type="text"
          label="Username"
          variant="outlined"
          onChange={this.handleUsername} />
        <TextField className="Login-input"
          value={this.state.password}
          type="password"
          label="Password"
          variant="outlined"
          onChange={this.handlePassword} />
        <div className="Login-btns">
          <Button color="primary">Register</Button>
          <Button variant="contained" color="primary" onClick={this.login}>Login</Button>
        </div>
      </form>
    );
  }
}

export default Login;