import React, { Component } from 'react'
import TrainCar from '../assets/traincar.png'


export class Train extends Component {
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

    render() {

        

        return (
            <div>
                {this.createTrain(this.getRandomNum(10))}
            </div>
        )

        
    }
}

export default Train
