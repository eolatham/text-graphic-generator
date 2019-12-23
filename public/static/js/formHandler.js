function showLoadingIconAndDisableButton() {
    var loading = document.getElementById('lds-css-loading');
    loading.style.display = 'block';
    loading.scrollIntoView();

    $('#generate-graphic').prop('disabled', true);
}

function hideLoadingIconAndEnableButton() {
    var loading = document.getElementById('lds-css-loading');
    loading.style.display = 'none';

    $('#generate-graphic').prop('disabled', false);
}

function checkQuote(formData) {
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
                window.alert(message);
                hideLoadingIconAndEnableButton();
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
            var a = document.createElement('a');
            a.href = URL.createObjectURL(blob);
            a.rel = 'noopener';
            a.click();
        })
        .catch(response => {
            var message = `An unexpected error occurred... Status code: ${response.status}`;
            window.alert(message);
            hideLoadingIconAndEnableButton();
        });
}

function handleForm() {
    $('#generate-graphic-form').submit((e) => {
        e.preventDefault();
        showLoadingIconAndDisableButton();
        const formData = {
            quote: $('#quote').val(),
            wrap_text: $('#wrap-text').is(':checked'),
            reduce_punctuation: $('#reduce-punctuation').is(':checked'),
            alignment_style: $('input[name=alignment-style-radio]:checked').val(),
            color_template: $('input[name=color-template-radio]:checked').val(),
            watermark_position: $('input[name=watermark-position-radio]:checked').val(),
        }
        checkQuote(formData);
    });
}

$(document).ready(handleForm());
