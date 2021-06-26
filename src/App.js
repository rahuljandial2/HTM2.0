import './App.css';
import Login from './login';
import Home from './home.js';
import { Route, Switch, Redirect, BrowserRouter as Router } from 'react-router-dom';


function App() {
  return (
    <Router>
      <div className="App">
        <Switch>
          <Route path="/login-page" exact component={Login} />
          <Route path="/home-page" exact component={Home} />
          <Redirect to="/login-page" />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
