import React, { Component } from 'react'
import TrainCar from '../assets/traincar.png'



export class Train extends Component {

    
    i = 0;
    timeout() {
        setTimeout(() => {
            document.getElementById('trains').style.left = this.i*2+'px';
            this.i++;
            if(this.i < 1000){
                this.timeout();
            }
        },10);
    }

    //---------------------------------------------
    getRandomNum = (max) => {
        return Math.floor(Math.random() * Math.floor(max));
    }
    createTrain = (length) =>{
        let trains = [];
        for (let i = 0; i < length; i++) {
            trains.push(<img src = {TrainCar} alt="" className="img-responsive" />);
        }  
        return trains
      }
    //-------------------------------------------------

    render() {
    {this.timeout()}
        return (
            
                <div
                style = {{
                    position:"absolute",
                    display:"flex"
                }}
                id = 'trains'
                >
                    {this.createTrain(this.getRandomNum(10))}
                </div>

           
        )

        
    }
}

export default Train
