let form_delete = document.getElementById("form_delete");
let transfer = document.getElementById("transfer");
const csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value


let user_redirect = () => {
    location.replace("https://django-one.herokuapp.com/reports/list/")
}


form_delete.addEventListener("submit", e => {
    e.preventDefault()

    const form_data = new FormData();
    form_data.append('csrfmiddlewaretoken', csrf)
    form_data.append("pk", transfer.innerText)

    $.ajax({
        type: 'POST',
        url: '/reports/delete/',
        data: form_data,
        success: function (res) {
            console.log("ajax ok +++")
            $('#exampleModal').modal('toggle');
            user_redirect()
        },
        error: function (err) {
            console.log("========== ERROR")
            console.log(err)
        },
        processData: false,
        contentType: false
    })

})
