export function connectWithAPI() {

    const acess_token = "Bearer bbivztcyn25o5xamrrfe9n6faj016t";

    const url = 'https://cors-anywhere.herokuapp.com/https://api.igdb.com/v4/games/'
    return fetch(url, {
        method:'POST',
        headers:{
            "Client-ID": "1ohymffiv6n925q0ll6z6hmxd0ryr7",
            "Authorization": "Bearer 2tqzayue7178r3c8jtya4dtehjq8al",
        },
        body: "fields *;",
    }).then((response => response.json()))
    .then(data => data)
    .catch((error) => console.log(error))
}