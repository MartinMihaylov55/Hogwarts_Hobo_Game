import React, { Component } from 'react'
import PlayerImage from '../assets/dude.png'

export class Player extends Component {
    render() {
        return (
		<div classname = "PlayerContainer">
            <div classname = "Dude">
				<img src = {PlayerImage} alt="" className="img-responsive" />
            </div>
			<div classname = "ControlField">
				<form>
				<input 
                        type = "text"
                        name = "number" 
                        placeholder = "0"
						size = "3">
                 </input>
				</form>
				<button>Go There!</button>
			</div>
		</div>
        )
    }
}

export default Player