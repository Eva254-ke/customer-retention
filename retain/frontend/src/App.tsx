import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Dashboard from './components/Dashboard';
import ChurnStats from './components/ChurnStats';
import CampaignManager from './components/CampaignManager';

const App: React.FC = () => {
  return (
    <Router>
      <Switch>
        <Route path="/" exact component={Dashboard} />
        <Route path="/churn-stats" component={ChurnStats} />
        <Route path="/campaign-manager" component={CampaignManager} />
      </Switch>
    </Router>
  );
};

export default App;