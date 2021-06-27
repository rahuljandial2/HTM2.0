import './App.css';
import Login from './login';
import Home from './home.js';
import { Route, Switch, Redirect, BrowserRouter as Router } from 'react-router-dom';
import Signup from './signup';


function App() {
  return (
    <Router>
      <div className="App">
        <Switch>
          <Route path="/login" exact component={Login} />
          <Route path="/home-page" exact component={Home} />
          <Route path="/signup" exact component={Signup} />
          <Redirect to="/login" />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
