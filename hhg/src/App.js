import React from 'react';
import logo from './logo.svg';
import './App.css';

class Rail extends React.Component {
  render() {
    return (
		<img src = {require("./assets/rail.png")} alt="" className="img-responsive" />
    );
  }
}

function createLine(length){
	let line = []
	for (let i = 0; i < length; i++) {
		line.push(<Rail />)
	}
	return line
  }



function App() {
  return (
    <div className="App">
      <header className="App-header">
		<div className = "RowOfRails">
			{createLine(15)}
		</div>
		<div className = "RowOfRails">
			{createLine(20)}
		</div>
		<div className = "RowOfRails">
			{createLine(10)}
		</div>
      </header>
    </div>
  );
}

export default App;
