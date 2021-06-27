import { Component } from "react";
import { Button, TextField } from "@material-ui/core";
import axios from "axios";
import { Redirect, Link } from "react-router-dom";

class Login extends Component {
  constructor(props) {
    super(props);

    this.handleSubmit = this.handleSubmit.bind(this);
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
  handleSubmit(event) {
    event.preventDefault();
    this.login();
  }
  async login() {
    const url = "http://localhost:8000/api/auth-token/";
    const params = {
      username: this.state.username,
      password: this.state.password,
    };
    await axios.post(url, params)
      .then(data => {
        const token = data.data.token;
        console.log(token);
        localStorage.setItem("token", token);
      })
      .catch(() => {
        console.log("Something went wrong while logging in!!");
      });
    this.forceUpdate();
  }
  render() {
    if (localStorage.getItem("token")) {
      return (
        <Redirect to="/home-page" />
      );
    }
    return (
      <form className="Login" onSubmit={this.handleSubmit}>
        <h1 className="Login-title">Whatodo</h1>
        <TextField className="Login-input"
          required
          value={this.state.username}
          type="text"
          label="Username"
          variant="outlined"
          onChange={this.handleUsername} />
        <TextField className="Login-input"
          required
          value={this.state.password}
          type="password"
          label="Password"
          variant="outlined"
          onChange={this.handlePassword} />
        <div className="Login-btns">
          <Link to='/signup'><Button color="primary">Register Here</Button></Link>
          <Button variant="contained" color="primary" type="submit">Login</Button>
        </div>
      </form>
    );
  }
}

export default Login;