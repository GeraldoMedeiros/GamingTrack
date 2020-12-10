import React, { useState } from 'react';
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';
import Form from 'react-bootstrap/Form';
import { FaGamepad } from 'react-icons/fa';
import './Navhome.css'

function Navhome() {

    const [show, setShow] = useState(false);
    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);

    return (
        <>
            <Navbar className="purple" variant="dark" sticky="top">
                <Navbar.Brand href="/">
                    <FaGamepad size={30}/>
                    &nbsp; GamingTrack
                </Navbar.Brand>
                <Nav className="ml-auto">
                    <Button variant="outline-light" onClick={handleShow}>Entrar</Button>
                </Nav>
            </Navbar>

            <Modal show={show} onHide={handleClose} aria-labelledby="contained-modal-title-vcenter" centered>
                <Modal.Header closeButton>
                    <Modal.Title>Acesse sua Conta</Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    <Form>
                        <Form.Group controlId="formLogin">
                            <Form.Label>Login</Form.Label>
                            <Form.Control type="text" placeholder="Insira seu nome de usuário" />
                        </Form.Group>
                        <Form.Group controlId="formSenha">
                            <Form.Label>Senha</Form.Label>
                            <Form.Control type="password" placeholder="Insira sua Senha" />
                        </Form.Group>
                        <Button size="lg" block variant="primary" type="submit" data-toggle="modal" data-target="#modalLogin">
                            Entrar
                        </Button>
                    </Form>
                </Modal.Body>
            </Modal>
        </>
    )
}

export default Navhome
