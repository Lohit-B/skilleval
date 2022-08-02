const form = document.getElementById('login_form');
form.addEventListener('submit', async (event) => {
    showLoadingScreen()
    event.preventDefault();
    const formData = new FormData(event.target);
    const value = Object.fromEntries(formData.entries());
    var object = {};
    formData.forEach(function(value, key){
        object[key] = value;
    });

    var data = JSON.stringify(object);
    const options = {
        'method':"POST",
        'body':data,
        'headers':{
            'Content-Type': 'application/json',
            "X-CSRFToken": getCookie("csrftoken")
        }
    }
    const url = `${API_SERVER_URL}/apis/users/signin`;
    const response = await fetch(url, options);
    if (response.status != 200) {
        let data = await response.json()
        alert(data.message)
        hideLoadingScreen()
    } else {
        saveJWT(await response.json());
        window.location = '/assessments/home'
    }
});

const saveJWT = (resp)=>{
    document.cookie = `jwt=${resp.data.auth_token};path=/;max-age=31536000;`
}
