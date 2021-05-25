console.log("-- upload js loaded ")

// actually csrf token already exists on this page
let csrf_upload = document.getElementsByName("csrfmiddlewaretoken")[0].value
let drop_form = document.getElementById("drop_form")

Dropzone.autoDiscover = false  // value from dropzone.js

// Create dropzone programmatically
let myDropzone = new Dropzone('#drop_form', {
    url: '/upload_csv/', // providing url that wil catch the file on upload
    init: function () {
        this.on('sending', function (file, xhr, formData) {
            console.log("-- sending")
            formData.append('csrfmiddlewaretoken', csrf_upload)
        })
    },
    moxFiles: 3,
    maxFilesize: 3, //mb
    acceptedFiles: '.csv'
})
