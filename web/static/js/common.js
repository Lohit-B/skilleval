
const showLoadingScreen=()=>{
    let screen = document.getElementById('loading_screen');
    if(!screen) {
        return;
    }
    screen.style.display = 'block';
}
const hideLoadingScreen=()=>{
    let screen = document.getElementById('loading_screen');
    if(!screen) {
        return;
    }
    screen.style.display = 'none';
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

document.onreadystatechange = function() {
    if (document.readyState !== "complete") {
        showLoadingScreen();
    } else {
        hideLoadingScreen();
    }
};

const logout = ()=>{
    document.cookie = `jwt=;path=/;max-age=31536000`
    window.location = '/'
}
