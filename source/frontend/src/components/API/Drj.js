export function getUser() {
    console.log('Fetching...')
    fetch('http://127.0.0.1:8000/GamingTrack/usuario')
    .then(response => response.json())
    .then(response => {
        console.log(response)
    })
}