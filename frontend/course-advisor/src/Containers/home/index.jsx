import React from "react";
import "./styles.css";
import LOGO from '../../images/LOGO.svg'

const Home = () => {

  return (
    <section id="home" className="home">
      <div className="page-image">
        <img src={LOGO} alt="" />
      </div>
      <div className="text-wrapper">
        <h1><span>COURSE</span></h1>
        <div className="text">
          <h1>ADVISOR</h1>
        </div>
        <div className="sub-text">
          <p>Your Friendly Advisor to making better choices</p>
        </div>
      </div>

      <div className="select-input">
        <select className="input">
          <option>Universities</option>
          <option>Univerity 1</option>
          <option>University 2</option>
          <option>University 3</option>
          <option>University 4</option>
        </select>
      </div>

      <div className="navigate">
        <ul className="menu">
          <li><a href="" >Course <br /> 800+ </a></li>
          <li><a href="" >Course <br /> 800+ </a></li>
          <li><a href="" >Course <br /> 800+ </a></li>
          <li><a href="" >Course <br /> 800+ </a></li>
        </ul>
        <button className="hero-btn">Explore</button>
      </div>
    </section>
  );
};

export default Home;
