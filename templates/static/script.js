function change(){
    e.preventDefault()
    var element = document.getElementById("com");
        element.style.backgroundColor = "#00FF00";
}


let url="https://script.google.com/macros/s/AKfycbwdwgG_KNJ6VtOGpo8Mw3R8h79iA3SKKX7Jeuu1qzDJXSGeK_JQXSLruhuEW6fKleNW1g/exec";
let form = document.querySelector("form");
let submit = document.querySelector(".submit");
let message = document.querySelector(".message");
form.addEventListener('submit', (e) => {
    e.preventDefault();
    submit.value = "sending.."
    fetch(url, {
    method: "POST",
    body: new FormData(form)
    })
    .then(res => res.text())
    .then(data => {
        message.innerHTML = data;
        submit.value = "Send Message"
    })
    .catch(err => {
        message.innerHTML = err;
        submit.value = "Send Message"
    })
})



