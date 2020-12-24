function showLoaderAndDisableButton() {
    $('.loader').css('display', 'block')
    $('#generate').prop('disabled', true);
}

function hideLoaderAndEnableButton() {
    $('.loader').css('display', 'none')
    $('#generate').prop('disabled', false);
}

function beginResponseHandlingChain(response) {
    console.log(response);
    return Promise.resolve(response);
}

function handleResponse(response) {
    if (response.status == 200) {
        return response.blob().then(blob => {
            hideLoaderAndEnableButton()
            var a = document.createElement('a');
            a.href = URL.createObjectURL(blob);
            a.download = 'graphic.png';
            a.type = 'image/png';
            a.rel = 'noopener';
            a.click();
        });
    } else if (response.status == 400) {
        return response.text().then(message => {
            hideLoaderAndEnableButton();
            window.alert(message);
        });
    } else {
        hideLoaderAndEnableButton();
        var message = `An unexpected error occurred... Status code: ${response.status}`;
        window.alert(message);
    }
}

function generateGraphic(formData) {
    console.log(formData);
    fetch('generate',
        {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(formData)
        })
        .then(response => beginResponseHandlingChain(response))
        .then(response => handleResponse(response));
}

function handleEvents() {
    $('#generate').click(function () {
        showLoaderAndDisableButton();
        const formData = {
            text: $('#text').val(),
            wrap_text: $('input[name=text-wrap-radio]:checked').val() == "auto",
            reduce_punctuation: $('input[name=punctuation-style-radio]:checked').val() == "reduce",
            alignment_style: $('input[name=alignment-style-radio]:checked').val(),
            color_template: $('input[name=color-template-radio]:checked').val(),
            watermark_position: $('input[name=watermark-position-radio]:checked').val(),
        }
        generateGraphic(formData);
    });
}

$(document).ready(handleEvents());
