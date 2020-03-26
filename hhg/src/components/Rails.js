import React, { Component } from 'react'

import RailImage from '../assets/rail.png'
import RailEnd from '../assets/pit.png'

export class Rails extends Component {
    state = {
        number: '',
        ids:''
    }


    change = (e) =>{
        this.setState(
            {
                [e.target.name]:e.target.value,
            }
        )
    }

    onSubmit = (e) => {
        e.preventDefault();
        console.log(this.state);
    }
    createLine(length){
        let line = [];
        for (let i = 0; i < length; i++) {
            line.push(<img src = {RailImage} alt="" className="img-responsive" />);
        }
        line.push(<img src = {RailEnd} alt="" className="img-responsive" />);     
        return line
      }

    railID = (num) => {
        let id = []
        for (let i = 0; i < num; i++){
            id.push(i);
        }
        return id
    }
    
    
    createRail = (num) => {
        let rails = []
        for (let i = 0; i < num; i++) {
          rails.push(<div>{this.createLine(27)}</div>)
        }
        console.log(this.state.ids);
        return rails
      }

    render() {
        this.state.ids = this.railID(this.state.number) 
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



  