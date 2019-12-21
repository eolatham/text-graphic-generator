function generateGrapic(quote) {
    fetch($('#generate-graphics-form').attr('action'),
        {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ 'quote': quote })
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
            a.download = `${Date.now()}.png`
            a.href = URL.createObjectURL(blob);
            a.rel = 'noopener';
            a.click();
        })
        .catch(response => {
            handleRequestError(response.status);
        });
}

function generateGraphics() {
    $('#generate-graphics-form').submit((e) => {
        e.preventDefault();

        $('#generate-graphics').prop('disabled', true);

        var loading = document.getElementById('lds-css-loading');
        loading.style.display = 'block';
        loading.scrollIntoView();

        const quotes = $('#quotes').val().split('\n');
        quotes.forEach(quote => {
            if (quote !== '') {
                generateGrapic(quote)
            }
        });

        $('#generate-graphics').prop('disabled', false);

        loading.style.display = 'none';
    });
}

$(document).ready(generateGraphics());
