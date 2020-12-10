import React from 'react';
import Button from 'react-bootstrap/Button';
import Container from 'react-bootstrap/Container'
import Col from 'react-bootstrap/Col'
import Row from 'react-bootstrap/Row'
import './Homepage.css'
import Navhome from '../Navhome';
import { FaGamepad } from 'react-icons/fa';
import { Link } from 'react-router-dom';
import { getCookie } from '../API/CorsHeaders.js'

function Homepage() {
    
    return (
        <>
            <Navhome />
            <Container fluid="true">
                <Row className='section1'>
                    <Col md={{span: 4, offset: 1}}>
                        <div className = 'text-wrapper' >
                            <h6 className='top-line'>EM BREVE</h6>
                            <h1 className='heading'>
                                Todas as suas conquistas em um lugar só. 
                            </h1>
                            <p className='subtitle'>
                                Acompanhe seu progresso e interaja com outros jogadores nessa rede social gratuita para Gamers. 
                            </p>
                            <Link to="/register">
                                <Button className='bttn btn--wide blue'>CRIE SUA CONTA</Button>
                            </Link>
                        </div>
                    </Col>
                    <Col md={{span: 4, offset: 2}}>
                        <div className="img-wrapper">
                            <FaGamepad size={900} className='img'/>
                        </div>
                    </Col>
                </Row>
            </Container>
        </>
    )
}

export default Homepage