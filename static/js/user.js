// function get_user_data(){
//     return fetch('/get_user')
//     .then(response => {response.json()})
// }

function communicate(route, data_json){
    return fetch(route, {
        method : 'POST',
        headers : {
            'Content-Type' : 'application/json'
        },
        body : JSON.stringify(data_json)
    })
    .then(response => {return response.json()})
    }