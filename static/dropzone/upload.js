console.log("-- upload js loaded ")

// actually csrf token already exists on this page
let csrf_upload = document.getElementsByName("csrfmiddlewaretoken")[0].value
let drop_form = document.getElementById("drop_form")
let file_alert_box = document.getElementById("file_alert_box");

let file_alert = (type, msg) => {
    file_alert_box.innerHTML = `
        <div class="alert alert-${type}" role="alert">
            ${msg}
        </div>
    `
}

Dropzone.autoDiscover = false  // value from dropzone.js
// Create dropzone programmatically
let myDropzone = new Dropzone('#drop_form', {
    url: '/upload_csv/', // providing url that wil catch the file on upload
    init: function () {
        this.on('sending', function (file, xhr, formData) {
            console.log("-- sending")
            formData.append('csrfmiddlewaretoken', csrf_upload)

            setTimeout(() => {
                file_alert('success', "csv uploaded")
            }, 2000)
        })
    },
    moxFiles: 3,
    maxFilesize: 3, //mb
    acceptedFiles: '.csv'
})
