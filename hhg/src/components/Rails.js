import React, { Component } from 'react'

import RailImage from '../assets/rail.png'

export class Rails extends Component {
    state = {
        number: ''
    }
    
    change = (e) =>{
        this.setState(
            {
                [e.target.name]:e.target.value
            }
        )
    }

    onSubmit = (e) => {
        e.preventDefault();
        console.log(this.state);
    }

    createLine(length){
        let line = []
        for (let i = 0; i < length; i++) {
            line.push(<img src = {RailImage} alt="" className="img-responsive" />)
        }
        return line
      }


    
    createRail = (num) => {
        let rails = []
        for (let i = 0; i < num; i++) {
          rails.push(<div>{this.createLine(27)}</div>)
        }
        return rails
      }

    render() {
        return (
            <div>
                <form>
                    <label htmlFor="fname">Number of rails:</label><br/>
                    <input 
                        type = "text"
                        name = "number" 
                        placeholder = "Enter here ..." 
                        value ={this.state.number} 
                        onChange={e => this.change(e)}>
                    </input>
                    <br/>

                    {/** 
                    <button 
                    type = "submit" 
                    onClick = {(e) => this.onSubmit()} 
                    >
                        Submit
                    </button>
                    */}
                </form>
                <div>
                    {this.createRail(this.state.number)}
                </div>
            </div>
            
        )
    }
}

export default Rails



  