import { Component } from "react";
import { Button, TextField } from "@material-ui/core";
import axios from "axios";
import { Link, Redirect } from "react-router-dom";

class Signup extends Component {
  constructor(props) {
    super(props);

    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleUsername = this.handleUsername.bind(this);
    this.handlePassword = this.handlePassword.bind(this);
    this.handleEmail = this.handleEmail.bind(this);
    this.state = {
      username: "",
      email: "",
      password: "",
      redirect: null
    };
  }

  handleUsername(event) {
    this.setState({
      username: event.target.value
    });
  }
  handleEmail(event) {
    this.setState({
      email: event.target.value
    });
  }
  handlePassword(event) {
    this.setState({
      password: event.target.value
    });
  }
  handleSubmit(event) {
    event.preventDefault();
    this.register();
    this.setState({ redirect: "/" });
  }
  async register() {
    const url = "http://127.0.0.1:8000/api/user-register/";
    const params = {
      username: this.state.username,
      email: this.state.email,
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
  }
  render() {
    if (this.state.redirect) {
      return <Redirect to={this.state.redirect} />
    }
    return (
      <form className="Login" onSubmit={this.handleSubmit} autoComplete={"off"}>
        <h1 className="Login-title">Todo</h1>
        <TextField className="Login-input"
          required
          value={this.state.username}
          type="text"
          label="Username"
          variant="outlined"
          onChange={this.handleUsername} />
        <TextField className="Login-input"
          required
          value={this.state.email}
          type="email"
          label="Email"
          variant="outlined"
          onChange={this.handleEmail} />
        <TextField className="Login-input"
          required
          value={this.state.password}
          type="password"
          label="Password"
          variant="outlined"
          onChange={this.handlePassword} />
        <div className="Login-btns">
          <Link to='/'><Button color="primary">Login Here</Button></Link>
          <Button variant="contained" color="primary" type="submit">Sign Up</Button>
        </div>
      </form>
    );
  }
}

export default Signup;