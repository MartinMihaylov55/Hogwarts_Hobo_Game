import React, { Component } from 'react'
import PlayerImage from '../assets/dude.png'

export class Player extends Component {
    render() {
        return (
		<div className = "PlayerContainer">
            <div className = "Dude">
				<img src = {PlayerImage} alt="" className="img-responsive" />
            </div>
			<div className = "ControlField">
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