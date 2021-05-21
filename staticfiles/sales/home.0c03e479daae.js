/**
 * what is happening here is taking data from report form
 * and saving at the db thru hte ajax request
 * on the way adding some beauty to the frontEnd (like hiding buttons when its needed )
 * */

console.log(" **** static loaded ")

let report_btn = document.getElementById("report_btn");
let img_chart = document.getElementById("img_chart");
let modal_body = document.getElementById("report_modal_body");
let report_form = document.getElementById("report_form");
let report_name = document.getElementById("report_name");
let report_text = document.getElementById("report_text");
let alert_box = document.getElementById("alert_box");
let report_modal = document.getElementById("reportModal");
const csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value


if (img_chart) {
    report_btn.classList.remove("not-visible");
}

let alert_creator = (type, msg) => {
    alert_box.innerHTML = `
        <div class="alert alert-${type}" role="alert">
            ${msg}
        </div>
    `
}

report_btn.addEventListener('click', () => {

    img_chart.setAttribute('class', 'w-100')  // bootstrap sizing
    modal_body.before(img_chart)  // insert at top of form

    report_form.addEventListener('submit', (e) => {
        e.preventDefault();

        const form_data = new FormData();
        form_data.append('csrfmiddlewaretoken', csrf);
        form_data.append('name', report_name.value);
        form_data.append('remarks', report_text.value);
        form_data.append('image', img_chart.src);

        // after getting report from user save it at the db with ajax
        $.ajax({
            type: 'POST',
            url: '/reports/create_report/',
            data: form_data,
            success: function (response) {
                console.log("success ++++++++")
                alert_creator('success', "report created")
                // close modal after 2 sec
                setTimeout(() => {
                    $('#reportModal').modal('toggle');
                }, 2000)

            },
            error: function (error) {
                console.log("ERROR ================")
                alert_creator('danger', "report not created, check with admin !")
                console.log(error)
            },
            // because having an bin img data
            processData: false,
            contentType: false
        })

    });
});
