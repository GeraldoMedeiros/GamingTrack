import React from 'react'
import Button from 'react-bootstrap/esm/Button'
import Col from 'react-bootstrap/esm/Col'
import Container from 'react-bootstrap/esm/Container'
import Row from 'react-bootstrap/esm/Row'
import './Game.css'
import Navuser from '../Navuser'
import Media from 'react-bootstrap/Media'
import Form from 'react-bootstrap/Form'
import 'react-rater/lib/react-rater.css'

function Game() {
    return (
        <>
            <Navuser />
            <Container fluid="true">
                <Row className="game-header">
                    <Col>
                        <h1 className="game-title">Hades</h1>
                    </Col>
                </Row>
                
                <div className="game-section">
                    <Row>
                        <Col className="game-info">
                            <Media>
                                <img
                                    width={200}
                                    height={266}
                                    className="align-self-start mr-3"
                                    src="https://images.igdb.com/igdb/image/upload/t_cover_big/co1qub.jpg"
                                    alt="game cover"/>
                                <Media.Body>
                                    <h2>Informações</h2>
                                    <hr/>
                                    <h5>Data de lançamento:</h5>
                                    <h6>Sep 17, 2020</h6>
                                    <h5>Genre:</h5>
                                    <h6>Hack and slash/Beat 'em up, Indie</h6>
                                    <h5>Platforms:</h5>
                                    <h6>Mac, PC (Microsoft Windows), Nintendo Switch</h6>
                                </Media.Body>
                            </Media>
                        </Col>
                    </Row>
                    <Row>
                        <Col className="game-info">
                            <h2>Storyline</h2>
                            <hr/>
                            <h6>Zagreus, the son of Hades, has discovered that his mother, which he was led to believe was Nyx, Night Incarnate, is actually someone else, and is outside Hell. He is now attempting to escape his father's domain, with the help of the other gods of Olympus, in an attempt to find his real mother.</h6>
                        </Col>
                    </Row>
                    <Row>
                        <Col className="game-info">
                            <h2>Member Reviews</h2>
                            <hr/>
                            <Form>
                                <Form.Group controlId="reviewBox">
                                    <Form.Label>Review</Form.Label>
                                    <Form.Control type="text" placeholder="Review this game"/>
                                </Form.Group>
                                <Button type="submit">Review</Button>
                            </Form>
                        </Col>
                    </Row>
                    <Row>
                        <Col className="game-info no-reviews">
                            <p>This game hasn't been reviewed yet. Be the first!</p>
                        </Col>
                    </Row>
                </div>
                
            </Container>
        </>
    )
}

export default Game
