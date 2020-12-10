import React from 'react'
import Button from 'react-bootstrap/esm/Button'
import { connectWithAPI } from '../API/IGDB.js' 
import { getUser } from '../API/Drj.js'

function Search() {
    return (
        <>
            <Button onClick={getUser}>Testar conexão com API</Button>
        </>
    )
}

export default Search
