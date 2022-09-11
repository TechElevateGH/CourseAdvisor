import './App.css';
import {Routes, Route } from 'react-router-dom'
import Home from './Components/home'
import Universites from './Components/universities'
import Ratings from './Components/ratings'
import Contact from './Components/contact'
import NavBar from './Components/navBar';

function App() {

  return (
    <div className="App">
      
        {/* NavBar */}
        <NavBar/>

        {/* Main Page Content */}
        <div className='main-page-content'>
        <Routes>
          <Route index path='/' element={<Home/>}/>
          <Route path='/universities' element={<Universites/>}/>
          <Route path='/ratings' element={<Ratings/>}/>
          <Route path='/contact' element={<Contact/>}/>
        </Routes>
      </div>
      
    </div>
  );
}

export default App;
