import React from 'react'
import { FaPaperPlane, FaStar, FaStarHalfAlt } from 'react-icons/fa'
import { BsStar } from 'react-icons/bs'
import './styles.css'

const Ratings = () => {
  return (
    <div className='ratings-main'>
        <div className="upper">
          <div className="content">
            <div className="courseImg"><img src='' alt="" /></div>
            <div className='courseDetails'>
              <div className='courseNum'><h1>4.6</h1></div>
              <div className='courseName'><h2>Chemical Engineering</h2></div>
            </div>
          </div>
        </div>

        <div className="middle">
          <div class="middle-row">
              <div class="middle-col">
                  <div className='middle-col-upper'>
                    <h3>Mary Jean</h3>
                  </div>
                  <p>Lorem Ipsum dolor sit amet, consectetur adipiscing elit. </p>
              </div>
          
              <div class="middle-col">
                  <div className='middle-col-upper'>
                    <h3>Mary Jean</h3>
                  </div>
                  <p>Lorem Ipsum dolor sit amet, consectetur adipiscing elit. </p>
              </div>
          </div>
          <div class="middle-row">
              <div class="middle-col">
                  <div className='middle-col-upper'>
                    <h3>Mary Jean</h3>
                  </div>
                  <p>Lorem Ipsum dolor sit amet, consectetur adipiscing elit. </p>
              </div>
          
              <div class="middle-col">
                  <div className='middle-col-upper'>
                    <h3>Mary Jean</h3>
                  </div>
                  <p>Lorem Ipsum dolor sit amet, consectetur adipiscing elit. </p>
              </div>
          </div>
        </div>

        <div className="bottom">
          <div className="bottom-row">
            <div className="bottom-left">
              <h3>Name:</h3>
              <div className='b-ratings'>
                <h4>Ratings:</h4>
                <div className='stars'>
                <FaStar size={20}/>
                <FaStar size={20}/>
                <FaStar size={20}/>
                <FaStarHalfAlt size={20}/>
                <BsStar size={20}/>
                </div>
              </div>
            </div>
            <div className="bottom-right">
              <form action="#" class="typing-area">
              <input type="text" placeholder="Type a review here..."/>
              <button><FaPaperPlane size={30} /></button>
              </form>
            </div>
          </div>
        </div>
    </div>
  )
}

export default Ratings