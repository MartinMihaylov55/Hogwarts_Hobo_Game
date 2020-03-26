import React, { Component } from 'react'
import ArrowKeysReact from 'arrow-keys-react';
import PlayerImage from '../assets/dude.png'

export class Player extends Component {
	ArrowKeysReact.config({
      left: () => {
        console.log('left key detected.');
      },
      right: () => {
        console.log('right key detected.');
      },
      up: () => {
        console.log('up key detected.');
      },
      down: () => {
        console.log('down key detected.');
      }
    });
    render() {
        return (
<<<<<<< Updated upstream
            <div>
                
=======
            <div {...ArrowKeysReact.events} tabIndex = "1">
				<img src = {PlayerImage} alt="" className="img-responsive" />
>>>>>>> Stashed changes
            </div>
        )
    }
}

export default Rails