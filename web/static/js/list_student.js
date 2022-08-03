const edit_form = (username)=>{
    document.getElementById(`info_${username}`).style.display='none'
    document.getElementById(`edit_${username}`).style.display='block'
}

const forms = document.getElementsByClassName('form_student');

for (var i = 0; i <forms.length; i++) {
    let form = forms.item(i)
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
            'method':"PUT",
            'body':data,
            'headers':{
                'Content-Type': 'application/json',
                "X-CSRFToken": getCookie("csrftoken"),
                "Authorization": getCookie("jwt")
            }
        }
        const url = `${API_SERVER_URL}/apis/students`;
        const response = await fetch(url, options);
        if (response.status != 202) {
            let data = await response.json()
            alert(data.message)
            hideLoadingScreen()
        } else {
            window.location.reload()
        }
    });
}

const filter = (select_obj)=>{
    let grade_id = select_obj.value
    if(!grade_id || grade_id== '') {
        return
    }
    window.location=`/students?grade=${grade_id}`
}

const form_add = document.getElementById('form_add_user');
form_add.addEventListener('submit', async (event) => {
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
            "X-CSRFToken": getCookie("csrftoken"),
            "Authorization": getCookie("jwt")
        }
    }
    const url = `${API_SERVER_URL}/apis/students`;
    const response = await fetch(url, options);
    if (response.status != 201) {
        let data = await response.json()
        alert(data.message)
        hideLoadingScreen()
    } else {
        window.location = `/students?grade=${object.grade}`
    }
});
