import React from 'react';
import logo from './logo.svg';
import './App.css';

class Rail extends React.Component {
  render() {
    return (
		<b>|----LMAO-RAIL----|</b>
    );
  }
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
		<Rail />
		<Rail />
		<Rail />
      </header>
    </div>
  );
}

export default App;
