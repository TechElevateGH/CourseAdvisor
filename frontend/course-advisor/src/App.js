import './App.css';
import {Routes, Route } from 'react-router-dom'
import Home from './Containers/home'
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
        </Routes>
      </div>
      
    </div>
  );
}

export default App;
