document.addEventListener('DOMContentLoaded', initialise);

function initialise() {
    let completeTask = document.querySelectorAll('.complete-task-form');

    completeTask.forEach(function(form) {
        form.addEventListener('submit', formSubmit);
    })
}

function formSubmit(event) {
    event.preventDefault();

    let form = event.target;
    submitTaskToServer(form);
}

function submitTaskToServer(form) {
    let fetchOptions = {
        method: 'POST',
        body: getTaskInfo(form)
    }

    fetch(form.action, fetchOptions)
        .then(function(response) {
            handleResponse(response, form);
        })
}

function getTaskInfo(form) {
    return new URLSearchParams(new FormData(form));
}

function handleResponse(response, form) {
    if (response.status === 204) {
        removeCompletedTask(form);
    } else {
        console.error('Unexpected status:', response.status);
    }
}

function removeCompletedTask(form) {
    form.parentElement.remove();
}
