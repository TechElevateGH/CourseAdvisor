import React, { useState } from 'react'
import { FaBars } from 'react-icons/fa'
import { HiX } from 'react-icons/hi'
import { Link } from 'react-router-dom'
import Logo from '../../images/Artboard 1.png'
import './styles.css'


const data = [
    {
        label: 'Universities',
        to: '/universities'
    },
    {
        label: 'Ratings',
        to: '/ratings'
    },
    {
        label: 'Contact Us',
        to: '/contact'
    }
]

const NavBar = () => {

    const [toggleIcon, setToggleIcon] = useState(false)

    const handleToggleIcon = () => {
        setToggleIcon(!toggleIcon);
    };

  return (
    <div>
        <nav className='navbar'>
            <div className='container'>
                <Link to={'/'} className='logo'>
                <img src={Logo} title='Home' alt='Home'/>
                </Link>
            </div>
                <ul className={`menu ${toggleIcon ? 'active' : ''}`}>
                    {
                    data.map((item, key) => (
                        <li key={key} className='items'>
                            <Link to={item.to} className="links">
                                {item.label}
                            </Link>
                        </li>
                    ))
                    }
                </ul>
            <div className='nav-icons' onClick={handleToggleIcon}>
                {
                    toggleIcon ? <HiX size={30}/> : <FaBars size={30}/>
                }
            </div>
        </nav>
    </div>
  )
}

export default NavBar