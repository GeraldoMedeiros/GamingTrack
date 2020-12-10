import React from 'react';
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import { FaGamepad } from 'react-icons/fa';
import './Navhome.css'

function Navuser() {

    return (
        <>
            <Navbar className="purple" variant="dark" sticky="top">
                <Navbar.Brand href="/">
                    <FaGamepad size={30}/>
                    &nbsp; GamingTrack
                </Navbar.Brand>
                <Nav className="ml-auto">
                    <Form inline>
                        <Form.Control type="text" placeholder="Buscar jogos, usuários..." className="mr-sm-2" />
                        <Button variant="outline-light">Buscar</Button>
                    </Form>
                </Nav>
                
                <Nav className="ml-auto">
                    <Button variant="outline-light">Minha conta</Button>
                </Nav>
            </Navbar>
        </>
    )
}

export default Navuser
