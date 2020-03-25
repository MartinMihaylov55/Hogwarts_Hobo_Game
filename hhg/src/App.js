import React from 'react';
import logo from './logo.svg';
import './App.css';
import Rails from './components/Rails'

<<<<<<< HEAD
class Rail extends React.Component {
  render() {
    return (
		<img src = {require("./assets/rail.png")} alt="" className="img-responsive" />
    );
  }
}



class RailLine extends React.Component {
  
  createLine = (length) => {
	let line = []
	for (let i = 0; i < length; i++) {
		line.push(<Rail />)
	}
	return line
  }
  
  render() {
    return (
		<div className = "RowOfRails">
		    {this.createLine(12)}
		</div>
    );
  }
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
	  <RailLine />
      </header>
    </div>
=======



function App() {
  return (
	<Rails />
>>>>>>> master
  );
}

export default App;
