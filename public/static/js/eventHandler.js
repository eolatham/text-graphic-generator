function showLoaderAndDisableButton() {
    $('.loader').css('display', 'block')
    $('#generate').prop('disabled', true);
}

function hideLoaderAndEnableButton() {
    $('.loader').css('display', 'none')
    $('#generate').prop('disabled', false);
}

function checkText(formData) {
    fetch('check',
        {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(formData)
        })
        .then(response => response.text()
            .then(message => {
                if (message !== '') {
                    return Promise.reject(message);
                } else {
                    return Promise.resolve(formData);
                }
            })
            .then(formData => generateGraphic(formData))
            .catch(message => {
                hideLoaderAndEnableButton();
                window.alert(message);
            }));
}

function generateGraphic(formData) {
    fetch('generate',
        {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(formData)
        })
        .then(response => {
            console.log(response);
            if (response.status !== 200) {
                return Promise.reject(response);
            } else {
                return Promise.resolve(response);
            }
        })
        .then(response => response.blob())
        .then(blob => {
            hideLoaderAndEnableButton()
            var a = document.createElement('a');
            a.href = URL.createObjectURL(blob);
            a.type = 'image/png';
            a.rel = 'noopener';
            a.click();
        })
        .catch(response => {
            hideLoaderAndEnableButton();
            var message = `An unexpected error occurred... Status code: ${response.status}`;
            window.alert(message);
        });
}

function handleEvents() {
    $('#generate').click(function () {
        showLoaderAndDisableButton();
        const formData = {
            text: $('#text').val(),
            text_wrap: $('input[name=text-wrap-radio]:checked').val(),
            punctuation_style: $('input[name=punctuation-style-radio]:checked').val(),
            alignment_style: $('input[name=alignment-style-radio]:checked').val(),
            color_template: $('input[name=color-template-radio]:checked').val(),
            watermark_position: $('input[name=watermark-position-radio]:checked').val(),
        }
        checkText(formData);
    });
}

$(document).ready(handleEvents());
