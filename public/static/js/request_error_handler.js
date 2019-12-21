function handleRequestError(status_code) {
    var message;
    if (status_code === 204) {
        message = `You entered an invalid quote... Status code: ${status_code}`;
    }
    else {
        message = `An unexpected error occurred... Status code: ${status_code}`;
    }
    window.alert(message);
}
