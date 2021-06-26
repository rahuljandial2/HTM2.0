import './App.css';
import Login from './login';
import Home from './home.js';
import { Route, Switch, BrowserRouter as Router } from 'react-router-dom';


function App() {
  return (
    <Router>
      <div className="App">
        <Switch>
          <Route path="/login-page" exact component={Login} />
          <Route path="/home-page" exact component={Home} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
