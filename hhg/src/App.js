import React, {Fragment} from 'react';
import logo from './logo.svg';
import './App.css';
import Rails from './components/Rails'
import Player from './components/Player'
import Train from './components/Train'

function App() {
  return (
	  	<Fragment>
			<Player />
		  	<Rails />
			
		</Fragment>
	
  );
}

export default App;
