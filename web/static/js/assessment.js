const save = async()=>{
    hideAllError()
    showLoadingScreen()
    let unanswered = false;
    let request_data = {};
    request_data.assessment = data.id
    request_data.performances = []
    data.questions.forEach(question=>{
        let answer = {}
        answer.question = question.id
        answer.choices = []
        let checks = document.getElementsByClassName(`checkbox_${question.id}`)
        for (var i = 0; i <checks.length; i++) {
            let check = checks.item(i)
            if(check.checked) {
                answer.choices.push(check.getAttribute('value'))
            }
        }

        if(answer.choices.length == 0) {
            unanswered=true
            document.getElementById(`error_${question.id}`).style.display = 'block'
        }


        request_data.performances.push(answer)
    })


    if(unanswered){
        error.innerHTML= "Check missing answer"
        error.style.display = 'block'
        hideLoadingScreen()
        return;
    }

    console.log(request_data)
    request_data = JSON.stringify(request_data);
    const options = {
        'method':"POST",
        'body': request_data,
        'headers':{
            'Content-Type': 'application/json',
            "X-CSRFToken": getCookie("csrftoken"),
            "Authorization": getCookie("jwt")
        }
    }
    const url = `${API_SERVER_URL}/apis/performances`;
    const response = await fetch(url, options);
    if (response.status != 201) {
        let data = await response.json()
        alert(data.message)
        hideLoadingScreen()
    } else {
        window.location = `/assessments/home?category=${data.category}`
    }

}

const hideAllError = ()=>{
    let errors = document.getElementsByClassName('error')
    for (var i = 0; i <errors.length; i++) {
        let error = errors.item(i)
        error.style.display = 'none'
    }
}
